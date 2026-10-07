"""Small utility helpers used across fl_studio_2026_producer_edition_premium_tools."""

from __future__ import annotations

import os
from typing import Iterable


def chunked(items: Iterable, size: int = 50) -> Iterable[list]:
    """Yield lists of up to ``size`` items from ``items``."""
    buf: list = []
    for it in items:
        buf.append(it)
        if len(buf) >= size:
            yield buf
            buf = []
    if buf:
        yield buf


def env_bool(name: str, default: bool = False) -> bool:
    """Parse a truthy boolean out of the environment."""
    v = os.environ.get(name)
    if v is None:
        return default
    return v.strip().lower() in ("1", "true", "yes", "on")
