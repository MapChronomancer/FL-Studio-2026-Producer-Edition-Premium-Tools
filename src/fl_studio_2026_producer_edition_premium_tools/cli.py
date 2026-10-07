"""
Advanced preset manager and workflow enhancer for FL Studio 2026 Producer Edition.

This module provides a command-line interface for managing presets and enhancing workflow
in FL Studio. It includes functionality for mixing templates, plugin chain presets,
chord packs, and productivity shortcuts.
"""

import argparse
from typing import List, Optional

from core import Config, run

def main(argv: Optional[List[str]] = None) -> None:
    """
    Parse command line arguments and run the core functionality.

    Args:
        argv: List of command line arguments. If None, uses sys.argv.
    """
    parser = argparse.ArgumentParser(
        description='Advanced preset manager and workflow enhancer for FL Studio 2026 Producer Edition.'
    )
    parser.add_argument(
        '--mixing-template',
        type=str,
        help='Path to the mixing template file.'
    )
    parser.add_argument(
        '--plugin-preset',
        type=str,
        help='Path to the plugin preset file.'
    )
    parser.add_argument(
        '--chord-pack',
        type=str,
        help='Path to the chord pack file.'
    )
    parser.add_argument(
        '--shortcuts',
        type=str,
        help='Path to the productivity shortcuts file.'
    )

    args = parser.parse_args(argv)

    config = Config(
        mixing_template=args.mixing_template,
        plugin_preset=args.plugin_preset,
        chord_pack=args.chord_pack,
        shortcuts=args.shortcuts
    )

    run(config)

if __name__ == '__main__':
    main()
