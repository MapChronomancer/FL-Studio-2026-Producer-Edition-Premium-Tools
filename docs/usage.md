# Usage

This is a starter scaffold for **FL-Studio-2026-Producer-Edition-Premium-Tools**, not a finished implementation of the supplied project theme. The example CLI reports its targets.

## Install

```bash
pip install -e .
```

## Basic example

```python
from fl_studio_2026_producer_edition_premium_tools.core import Config, run

cfg = Config(verbose=True, targets=["alpha", "beta"])
run(cfg)
```

## CLI

```bash
fl_studio_2026_producer_edition_premium_tools alpha beta -v
```

## Tests

```bash
pytest
```

## Theme

Project theme label: Advanced preset manager and workflow enhancer for FL Studio 2026 Producer Edition. Includes mixing templates, plugin chain presets, chord packs, and productivity shortcuts for music producers..
