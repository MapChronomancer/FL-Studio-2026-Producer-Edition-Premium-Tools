"""Core implementation for FL-Studio-2026-Producer-Edition-Premium-Tools.

Advanced preset manager and workflow enhancer for FL Studio 2026 Producer Edition.
Handles mixing templates, plugin chain presets, chord packs, and productivity shortcuts.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, List, Optional


@dataclass
class Config:
    """Runtime configuration for the preset manager."""

    preset_dir: Path = Path("./presets")
    template_dir: Path = Path("./templates")
    chord_pack: str = "basic_progressions"
    plugin_chains: Dict[str, List[str]] = field(default_factory=dict)
    shortcuts_enabled: bool = True
    verbose: bool = False


def _discover_presets(preset_dir: Path, extension: str = ".fst") -> List[Path]:
    """Return sorted list of preset files with the given extension."""
    if not preset_dir.is_dir():
        return []
    return sorted(p for p in preset_dir.glob(f"*{extension}") if p.is_file())


def _select_chain(config: Config, target: str) -> Optional[List[str]]:
    """Return the plugin chain for a target, or None if unavailable."""
    chain = config.plugin_chains.get(target)
    if chain and config.shortcuts_enabled:
        return chain
    return None


def run(config: Config) -> int:
    """Execute the preset workflow and return a process exit code."""
    presets = _discover_presets(config.preset_dir)
    templates = _discover_presets(config.template_dir, ".flp")

    if config.verbose:
        print(f"Discovered {len(presets)} presets, {len(templates)} templates.")

    if not presets and not templates:
        print("No presets or templates found. Check configured paths.")
        return 1

    active_chain = _select_chain(config, "mix_bus")
    if active_chain:
        if config.verbose:
            print("Applying mix bus plugin chain:", ", ".join(active_chain))
    elif config.verbose:
        print("No mix bus plugin chain configured.")

    # Simulate loading the chord pack
    chord_map: Dict[str, List[int]] = {
        "basic_progressions": [[0, 4, 7], [5, 9, 0], [7, 11, 2]],
        "jazz_voicings": [[0, 4, 7, 11], [2, 5, 9, 0]],
    }
    chords = chord_map.get(config.chord_pack, [])
    if config.verbose:
        print(f"Loaded chord pack '{config.chord_pack}' with {len(chords)} progressions.")

    # Workflow shortcut simulation
    if config.shortcuts_enabled:
        for preset in presets[:2]:
            if config.verbose:
                print(f"Quick-load preset: {preset.stem}")

    return 0
