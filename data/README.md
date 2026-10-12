# Project structure

This repository is a research prototype. It already contains the core workflow, but it benefits from a clearer separation between entry points, generated artifacts, and documentation.

## Current organization

```text
VEXYON/
├── README.md
├── main.py
├── pipeline.py
├── config.py
├── train_model.py
├── test_model.py
├── detection.py
├── robot_autonome.py
├── simulate_robot_visual.py
├── clean_dataset.py
├── merge_csv.py
├── analyse.py
├── Augment_dataset.py
├── udp_protocol.py
├── feature_utils.py
├── listener.py
├── demo_webcam.py
├── export_secure.py
├── src/
├── docs/
├── data/
├── logs/
├── models/
└── .gitignore
```

## Recommended usage

- Keep scripts at the root for quick execution and compatibility.
- Use `docs/` for architecture, notes, and methodology.
- Store datasets in `data/` instead of mixing them with source code.
- Keep logs and generated output in `logs/`.
- Store trained models in `models/`.
- Use `src/` for future modularization or package extraction.

## Suggested future evolution

A production-ready version of the project would likely look like this:

```text
VEXYON/
├── README.md
├── pyproject.toml
├── src/
│   └── vexyon/
│       ├── __init__.py
│       ├── config.py
│       ├── capture/
│       ├── data/
│       ├── models/
│       ├── robotics/
│       └── utils/
├── data/
│   ├── raw/
│   ├── processed/
│   └── README.md
├── docs/
│   ├── architecture.md
│   └── dataset.md
├── models/
│   └── README.md
├── logs/
├── tests/
└── .gitignore
```

The important point is not to mix experimentation, data, logs, and packaged code in the same layer.

