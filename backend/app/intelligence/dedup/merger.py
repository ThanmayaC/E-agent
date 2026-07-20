"""Duplicate dataset detection & partition merging.

Tables with (near-)identical schemas — monthly/yearly partitions, snapshots,
incremental extracts — are detected via schema signatures and merged into one
logical dataset automatically.
"""
from __future__ import annotations

import pandas as pd

from app.core.logging import get_logger
from app.intelligence.connectors.excel import ExtractedTable
from app.intelligence.profiling.profiler import normalize_name

logger = get_logger(__name__)


class DatasetMerger:
    def __init__(self, similarity_threshold: float = 0.90):
        self.similarity_threshold = similarity_threshold

    def merge(self, tables: list[ExtractedTable]) -> tuple[list[ExtractedTable], dict[str, list[str]]]:
        """Group tables by schema similarity; concat each group. Returns
        (merged tables, {merged_name: [source table names]})."""
        groups: list[list[ExtractedTable]] = []
        for table in tables:
            placed = False
            for group in groups:
                if self._similarity(table, group[0]) >= self.similarity_threshold:
                    group.append(table)
                    placed = True
                    break
            if not placed:
                groups.append([table])

        merged: list[ExtractedTable] = []
        lineage: dict[str, list[str]] = {}
        for group in groups:
            if len(group) == 1:
                merged.append(group[0])
                lineage[group[0].name] = [group[0].name]
                continue
            base = group[0]
            frames = []
            for t in group:
                df = t.df.copy()
                df.columns = [normalize_name(c) for c in df.columns]
                df["_source_table"] = t.name
                frames.append(df)
            combined = pd.concat(frames, ignore_index=True, sort=False)
            before = len(combined)
            combined = combined.drop_duplicates(subset=[c for c in combined.columns if c != "_source_table"])
            name = self._common_name([t.name for t in group])
            logger.info("Merged %d partitions into '%s' (%d rows, %d exact duplicates removed)",
                        len(group), name, len(combined), before - len(combined))
            merged.append(ExtractedTable(
                name=name, source_file=f"{len(group)} files/sheets",
                source_sheet="merged", header_row=0, df=combined.reset_index(drop=True),
            ))
            lineage[name] = [t.name for t in group]
        return merged, lineage

    @staticmethod
    def _similarity(a: ExtractedTable, b: ExtractedTable) -> float:
        ca = {normalize_name(c) for c in a.df.columns}
        cb = {normalize_name(c) for c in b.df.columns}
        if not ca or not cb:
            return 0.0
        return len(ca & cb) / len(ca | cb)

    @staticmethod
    def _common_name(names: list[str]) -> str:
        """jan_sales, feb_sales -> sales ; sales_2023, sales_2024 -> sales"""
        token_lists = [n.split("_") for n in names]
        common = set(token_lists[0])
        for toks in token_lists[1:]:
            common &= set(toks)
        ordered = [t for t in token_lists[0] if t in common and not t.isdigit()]
        return "_".join(ordered) if ordered else names[0] + "_merged"
