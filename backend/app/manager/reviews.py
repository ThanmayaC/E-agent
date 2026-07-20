"""Report Review Center.

Status tracking for every generated report: draft → review → approved /
rejected → archived. A new report version registers in ``review`` state and
raises a notification; transitions are validated and fully historied.
"""
from __future__ import annotations

from app.communication.notifications import NotificationCenter
from app.manager.store import ManagerStore, new_id, now_iso

STATUSES = ("draft", "review", "approved", "rejected", "archived")
TRANSITIONS: dict[str, tuple[str, ...]] = {
    "draft": ("review", "archived"),
    "review": ("approved", "rejected", "archived"),
    "approved": ("archived",),
    "rejected": ("review", "archived"),
    "archived": (),
}


class ReportReviewCenter:
    def __init__(self, store: ManagerStore,
                 notifications: NotificationCenter | None = None):
        self.store = store
        self.notifications = notifications
        # Optional EventBus, attached by the autonomy runtime. An approved
        # report is an enterprise event the Trigger Engine acts on (executive
        # summary); without a bus the review center behaves exactly as before.
        self.bus = None

    def register(self, project_id: str, report_version: int, title: str,
                 health_score: float | None = None) -> dict | None:
        """Track a newly generated report version (idempotent per
        project+version). New registrations enter ``review``."""
        ref = f"{project_id}:v{report_version}"
        if any(r.get("ref") == ref for r in self.store.read("report_reviews")):
            return None
        review = {"review_id": new_id("rev"), "ref": ref,
                  "project_id": project_id,
                  "report_version": report_version, "title": title[:200],
                  "health_score": health_score, "status": "review",
                  "history": [{"status": "review", "at": now_iso(),
                               "by": "system", "note": "report generated"}],
                  "created_at": now_iso()}
        self.store.append("report_reviews", review)
        if self.notifications is not None:
            self.notifications.notify(
                "new_report", f"New report ready for review: {title}",
                detail=f"Report v{report_version}"
                       + (f" — health score {health_score:.0f}"
                          if health_score is not None else ""),
                project_id=project_id, ref=ref)
        return review

    def set_status(self, review_id: str, status: str, by: str = "",
                   note: str = "") -> dict:
        if status not in STATUSES:
            raise ValueError(f"Unknown review status: {status}")
        current = next((r for r in self.store.read("report_reviews")
                        if r["review_id"] == review_id), None)
        if current is None:
            raise KeyError(f"Unknown review: {review_id}")
        if status not in TRANSITIONS[current["status"]]:
            raise ValueError(
                f"Invalid transition {current['status']} → {status}")
        history = current.get("history", []) + [
            {"status": status, "at": now_iso(), "by": by, "note": note[:300]}]
        updated = self.store.update("report_reviews", "review_id", review_id,
                                    {"status": status, "history": history})
        if status == "approved" and self.bus is not None:
            self.bus.publish("ReportApproved",
                             {"review_id": review_id,
                              "project_id": current["project_id"],
                              "report_version": current["report_version"],
                              "title": current["title"], "by": by,
                              "detail": f"Report approved: {current['title']}"},
                             project_id=current["project_id"],
                             source="report_review_center")
        return updated

    def reviews(self, status: str = "", limit: int = 50) -> list[dict]:
        items = self.store.read("report_reviews")
        if status:
            items = [r for r in items if r["status"] == status]
        return list(reversed(items))[:limit]

    def pending(self, limit: int = 20) -> list[dict]:
        return [r for r in self.reviews(limit=200)
                if r["status"] in ("draft", "review")][:limit]

    def stats(self) -> dict:
        counts: dict[str, int] = {s: 0 for s in STATUSES}
        for r in self.store.read("report_reviews"):
            counts[r["status"]] = counts.get(r["status"], 0) + 1
        return counts
