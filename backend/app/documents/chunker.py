"""Paragraph-aware text chunking for embeddings.

Chunks break on paragraph boundaries where possible so an embedded chunk is
a coherent thought, not a window that slices a sentence in half. Overlap
carries context across boundaries; a chunk smaller than the minimum merges
into its neighbour rather than polluting the vector store with fragments.
"""
from __future__ import annotations

MIN_CHUNK_CHARS = 200


def chunk_text(text: str, target_chars: int = 1600,
               overlap: int = 200) -> list[str]:
    """Split ``text`` into chunks of roughly ``target_chars`` characters."""
    text = (text or "").strip()
    if not text:
        return []
    if len(text) <= target_chars:
        return [text]

    paragraphs = [p.strip() for p in text.split("\n\n") if p.strip()]
    if not paragraphs:
        paragraphs = [text]

    chunks: list[str] = []
    current = ""
    for paragraph in paragraphs:
        # A paragraph larger than a whole chunk is split by size.
        while len(paragraph) > target_chars:
            if current:
                chunks.append(current)
                current = ""
            chunks.append(paragraph[:target_chars])
            paragraph = paragraph[max(target_chars - overlap, 1):]
        if len(current) + len(paragraph) + 2 > target_chars and current:
            chunks.append(current)
            current = current[-overlap:] if overlap else ""
        current = f"{current}\n\n{paragraph}".strip() if current else paragraph
    if current:
        if chunks and len(current) < MIN_CHUNK_CHARS:
            chunks[-1] = f"{chunks[-1]}\n\n{current}"
        else:
            chunks.append(current)
    return chunks
