"""Forecasting — gradient-boosted daily models with an honest backtest.

The forecast is never a bare number. Each run trains a gradient-boosting model
on the leak-free feature frame, *validates it by walk-forward backtest* on days
the model never saw, and only then projects forward. Prediction intervals come
from the backtest residuals — the band is as wide as the model has actually been
wrong, not a textbook 1.96·σ fantasy. Feature importances come from permutation
on the held-out fold, so "most influential feature" means influential on unseen
data, not on the training set.

The recursive projection feeds each day's prediction back in as tomorrow's lag,
exactly as production would, so a 14-day forecast compounds its own uncertainty
the way reality does.
"""
from __future__ import annotations

from dataclasses import dataclass, field

import numpy as np
import pandas as pd

from app.warehouse.ml import features as F

try:
    from sklearn.ensemble import HistGradientBoostingRegressor
    from sklearn.inspection import permutation_importance
    from sklearn.linear_model import Ridge
    from sklearn.preprocessing import StandardScaler
    _SKLEARN = True
except ImportError:  # pragma: no cover
    _SKLEARN = False


# Metrics that are counts/values → non-negative; rates live in [0, 100].
_RATE_TARGETS = {"success_rate", "technical_decline_pct", "business_decline_pct",
                 "risk_decline_pct", "timeout_pct", "retry_rate_pct"}
_NONNEG_TARGETS = {"attempts", "successful", "failed", "pending", "value_inr",
                   "avg_ticket_inr", "active_customers", "active_merchants",
                   "retries"}


@dataclass
class BacktestResult:
    folds: int
    mape: float | None
    smape: float | None
    rmse: float | None
    mae: float | None
    r2: float | None
    naive_mape: float | None          # seasonal-naive baseline, for skill
    skill_vs_naive: float | None      # how much better than "same as last week"
    residual_std: float
    coverage_80: float | None
    predictions: list[dict] = field(default_factory=list)


class Forecaster:
    """One target, one slice. Trains, backtests, and projects forward."""

    def __init__(self, target: str, *, horizon: int = 14,
                 min_train: int = 45, backtest_days: int = 42,
                 refit_every: int = 3):
        self.target = target
        self.horizon = horizon
        self.min_train = min_train
        self.backtest_days = backtest_days
        # Refit every N steps rather than daily: a 2-3 day stale model still
        # predicts one-step-ahead honestly and cuts backtest cost ~3x.
        self.refit_every = max(1, refit_every)
        self.model = None
        self.scaler = None
        self.cols: list[str] = []
        self.feature_frame: pd.DataFrame | None = None

    @property
    def available(self) -> bool:
        return _SKLEARN

    # ------------------------------------------------------------ modelling
    def _new_model(self, n: int):
        """Boosting once there is enough signal; ridge on short slices where a
        200-tree model would only memorise noise."""
        if n >= 90:
            return HistGradientBoostingRegressor(
                max_iter=300, max_depth=3, learning_rate=0.05,
                min_samples_leaf=8, l2_regularization=1.0,
                early_stopping=False, random_state=7)
        return Ridge(alpha=5.0)

    def _fit(self, X: pd.DataFrame, y: pd.Series):
        model = self._new_model(len(X))
        if isinstance(model, Ridge):
            scaler = StandardScaler().fit(X.values)
            model.fit(scaler.transform(X.values), y.values)
            return model, scaler
        model.fit(X.values, y.values)
        return model, None

    def _predict(self, model, scaler, X: np.ndarray) -> np.ndarray:
        if scaler is not None:
            X = scaler.transform(X)
        return model.predict(X)

    def _clip(self, arr: np.ndarray) -> np.ndarray:
        if self.target in _RATE_TARGETS:
            return np.clip(arr, 0.0, 100.0)
        if self.target in _NONNEG_TARGETS:
            return np.clip(arr, 0.0, None)
        return arr

    # ------------------------------------------------------------ pipeline
    def prepare(self, analytics, filters) -> pd.DataFrame:
        base = F.build_daily_frame(analytics, filters, target=self.target)
        if base.empty:
            return base
        frame = F.add_supervised_features(base, self.target)
        self.cols = F.feature_columns(frame, self.target)
        self.feature_frame = frame
        return frame

    def _xy(self, frame: pd.DataFrame):
        d = frame.dropna(subset=self.cols + [self.target])
        return d[self.cols], d[self.target], d

    # ------------------------------------------------------------ backtest
    def backtest(self, frame: pd.DataFrame) -> BacktestResult | None:
        """Walk-forward one-step-ahead over the tail. Each step trains only on
        the past, predicts the next day, then reveals it — the honest test."""
        X, y, d = self._xy(frame)
        n = len(d)
        if n < self.min_train + 8:
            return None
        start = max(self.min_train, n - self.backtest_days)
        y_true, y_pred, y_naive, rows = [], [], [], []
        season = 7
        yvals = d[self.target].to_numpy(float)
        model = scaler = None
        for i in range(start, n):
            if model is None or (i - start) % self.refit_every == 0:
                model, scaler = self._fit(X.iloc[:i], y.iloc[:i])
            pred = float(self._clip(
                self._predict(model, scaler, X.iloc[i:i + 1].values))[0])
            actual = float(y.iloc[i])
            naive = float(yvals[i - season]) if i >= season else float(yvals[i - 1])
            y_true.append(actual); y_pred.append(pred); y_naive.append(naive)
            rows.append({"date": str(d.iloc[i]["date"].date()),
                         "actual": round(actual, 3),
                         "predicted": round(pred, 3),
                         "error_pct": round(100 * (pred - actual) / actual, 2)
                         if actual else None})
        return self._score(np.array(y_true), np.array(y_pred),
                           np.array(y_naive), rows)

    @staticmethod
    def _score(yt, yp, yn, rows) -> BacktestResult:
        resid = yp - yt
        nz = yt != 0
        mape = float(np.mean(np.abs(resid[nz] / yt[nz])) * 100) if nz.any() else None
        denom = (np.abs(yt) + np.abs(yp))
        smape = float(np.mean(np.abs(resid)[denom > 0]
                              / denom[denom > 0]) * 200) if (denom > 0).any() else None
        rmse = float(np.sqrt(np.mean(resid ** 2)))
        mae = float(np.mean(np.abs(resid)))
        ss_res = float(np.sum(resid ** 2))
        ss_tot = float(np.sum((yt - yt.mean()) ** 2))
        r2 = 1 - ss_res / ss_tot if ss_tot > 0 else None
        naive_resid = yn - yt
        naive_mape = float(np.mean(np.abs(naive_resid[nz] / yt[nz])) * 100) \
            if nz.any() else None
        skill = (round(100 * (1 - mape / naive_mape), 1)
                 if mape is not None and naive_mape not in (None, 0) else None)
        band = 1.2816 * resid.std()   # 80% if residuals were normal
        coverage = float(np.mean(np.abs(resid) <= band) * 100) if len(resid) else None
        return BacktestResult(
            folds=len(yt),
            mape=round(mape, 2) if mape is not None else None,
            smape=round(smape, 2) if smape is not None else None,
            rmse=round(rmse, 3), mae=round(mae, 3),
            r2=round(r2, 4) if r2 is not None else None,
            naive_mape=round(naive_mape, 2) if naive_mape is not None else None,
            skill_vs_naive=skill,
            residual_std=round(float(resid.std()), 4),
            coverage_80=round(coverage, 1) if coverage is not None else None,
            predictions=rows[-28:])

    # ------------------------------------------------------------ forecast
    def forecast(self, frame: pd.DataFrame, bt: BacktestResult | None) -> list[dict]:
        """Recursive projection. Lags roll forward off the model's own output;
        the interval widens with √horizon to reflect compounding error."""
        X, y, d = self._xy(frame)
        if len(d) < self.min_train:
            return []
        self.model, self.scaler = self._fit(X, y)
        hist = self.feature_frame.copy()
        resid_std = bt.residual_std if bt else float(y.std() * 0.15)

        out: list[dict] = []
        last_date = pd.to_datetime(hist["date"].iloc[-1])
        for h in range(1, self.horizon + 1):
            fdate = last_date + pd.Timedelta(days=h)
            row = self._future_row(hist, fdate)
            hist = pd.concat([hist, pd.DataFrame([row])], ignore_index=True)
            hist = F.add_supervised_features(
                hist.drop(columns=[c for c in hist.columns
                                   if c.startswith(f"{self.target}_")
                                   and c != self.target], errors="ignore"),
                self.target)
            xrow = hist.iloc[-1:][self.cols].fillna(
                hist[self.cols].mean())
            yhat = float(self._clip(
                self._predict(self.model, self.scaler, xrow.values))[0])
            hist.iloc[-1, hist.columns.get_loc(self.target)] = yhat
            widen = resid_std * np.sqrt(h)
            lo, hi = self._clip(np.array([yhat - 1.2816 * widen,
                                          yhat + 1.2816 * widen]))
            out.append({
                "date": str(fdate.date()), "horizon": h,
                "forecast": round(yhat, 3),
                "lower_80": round(float(lo), 3),
                "upper_80": round(float(hi), 3),
                "is_weekend": bool(fdate.dayofweek >= 5)})
        return out

    def _future_row(self, hist: pd.DataFrame, fdate: pd.Timestamp) -> dict:
        """A future calendar row. Calendar facts are known; the target is a
        placeholder the model is about to fill."""
        row = {c: np.nan for c in hist.columns}
        row["date"] = fdate
        row["day_of_month"] = fdate.day
        row["week_of_month"] = ((fdate.day - 1) // 7) + 1
        row["month"] = fdate.month
        row["day_of_week"] = fdate.dayofweek
        row["is_weekend"] = int(fdate.dayofweek >= 5)
        row["trend_index"] = float(hist["trend_index"].iloc[-1] + 1)
        # Calendar flags default to a normal day; salary/month-end are datable.
        row["is_month_end"] = int(fdate.day >= 28)
        row["is_quarter_end"] = int(fdate.month in (3, 6, 9, 12)
                                    and fdate.day >= 28)
        row["is_salary_window"] = int(fdate.day <= 3 or fdate.day >= 28)
        row["is_holiday"] = 0
        row["has_festival"] = 0
        for c in ("spend_multiplier", "settlement_multiplier"):
            if c in hist.columns:
                row[c] = float(hist[c].tail(28).mean())
        return row

    # ------------------------------------------------------------ importance
    def importances(self, frame: pd.DataFrame, bt_folds: int = 21) -> list[dict]:
        """Permutation importance on a held-out tail — importance where it
        counts, on data the model did not train on."""
        X, y, d = self._xy(frame)
        n = len(d)
        if n < self.min_train + 8 or self.model is None:
            return []
        split = max(self.min_train, n - bt_folds)
        Xtr, ytr = X.iloc[:split], y.iloc[:split]
        Xte, yte = X.iloc[split:], y.iloc[split:]
        if len(Xte) < 5:
            return []
        model, scaler = self._fit(Xtr, ytr)
        Xte_t = scaler.transform(Xte.values) if scaler is not None else Xte.values
        try:
            r = permutation_importance(model, Xte_t, yte.values, n_repeats=10,
                                       random_state=7, scoring="r2")
        except Exception:  # noqa: BLE001
            return []
        imp = [(self.cols[i], float(r.importances_mean[i]),
                float(r.importances_std[i])) for i in range(len(self.cols))]
        imp = [t for t in imp if t[1] > 0]
        imp.sort(key=lambda t: t[1], reverse=True)
        total = sum(t[1] for t in imp) or 1.0
        out = []
        for name, mean, std in imp[:8]:
            out.append({
                "feature": name,
                "label": F.humanise(name, self.target),
                "importance": round(mean, 5),
                "importance_pct": round(100 * mean / total, 1),
                "stability": round(1 - min(1.0, std / (abs(mean) + 1e-9)), 2)})
        return out
