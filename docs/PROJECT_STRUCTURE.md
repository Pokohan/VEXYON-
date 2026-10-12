# VEXYON

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white" alt="Python 3.10+" />
  <img src="https://img.shields.io/badge/OpenCV-4.x-5C3EE8?logo=opencv&logoColor=white" alt="OpenCV" />
  <img src="https://img.shields.io/badge/MediaPipe-Hands-00C7B7?logo=google&logoColor=white" alt="MediaPipe" />
  <img src="https://img.shields.io/badge/ML-Scikit%20Learn-F7931E?logo=scikitlearn&logoColor=white" alt="Scikit Learn" />
</p>

<p align="center">
  <strong>AI-assisted robotic grasping through computer vision and machine learning</strong>
</p>

VEXYON is a research project focused on understanding how hand landmarks, pressure labels, and machine learning can support adaptive robotic grasping. The objective is to estimate a suitable grip level from visual hand features and to explore a decision pipeline that could later be adapted to real-world robotic manipulation.

## Why this project?

- Capture hand posture data from a webcam using MediaPipe.
- Translate visual gesture information into pressure-related classes.
- Train a model that predicts the most appropriate grip intensity.
- Simulate an autonomous decision-making loop around grasping.
- Explore a realistic robotics workflow, while staying honest about validation limits.

## Project status

This project is currently a research prototype and an experimental exploration. It is useful for learning, prototyping, and validating ideas, but it does not replace real-world physical validation or industrial-grade force control.

## Architecture at a glance

```text
VEXYON/
├── README.md                  # Project overview and setup guide
├── main.py                    # Webcam data capture
├── pipeline.py                # End-to-end ML pipeline entry point
├── config.py                  # Central configuration and thresholds
├── train_model.py             # Model training
├── test_model.py              # Evaluation
├── detection.py               # Detection logic
├── robot_autonome.py          # Autonomous decision logic
├── simulate_robot_visual.py   # Visual simulation
├── clean_dataset.py           # Data cleaning
├── merge_csv.py               # CSV fusion
├── analyse.py                 # Analysis and plots
├── Augment_dataset.py         # Optional augmentation utilities
├── udp_protocol.py            # Communication helper
├── feature_utils.py           # Feature helpers
├── listener.py                # Listener utilities
├── demo_webcam.py            # Demo utilities
├── export_secure.py           # Export helper
├── src/                      # Future package/module structure
├── docs/                     # Project documentation and organization
├── data/                     # Dataset folders and notes
├── logs/                     # Runtime logs and generated reports
├── models/                   # Saved trained models and metadata
├── .gitignore                # Git ignore rules
└── LICENSE                   # Licensing information (if present)
```

## Workflow

1. Capture hand motion and landmark data from the webcam.
2. Merge and clean the collected CSV datasets.
3. Train and validate a model to infer pressure-related classes.
4. Evaluate predictions on unseen data.
5. Use the autonomous logic to simulate robotic decisions.

## Quick start

### 1) Clone the repository

```bash
git clone https://github.com/Pokohan/VEXYON-.git
cd VEXYON-
```

### 2) Install dependencies

```bash
python -m pip install opencv-python mediapipe scikit-learn pandas numpy matplotlib joblib
```

### 3) Capture a dataset

```bash
python main.py
```

Follow the in-app instructions to label the object and record samples.

### 4) Run the full pipeline

```bash
python pipeline.py
```

### 5) Train / evaluate the model

```bash
python train_model.py
python test_model.py
```

## Data and privacy

This repository does not ship a public dataset. The dataset is intentionally kept private to protect the effort spent collecting and annotating it.

This is perfectly reasonable for a research project, but it also means you need to generate your own data if you want to reproduce the workflow locally.

## Important limitations

- Hand landmarks are not direct measurements of real grip force.
- Labels are approximations derived from a controlled setup, not a certified physical measurement.
- Simulation behavior does not automatically transfer to a real robot.
- Real-world validation is required before deploying this in production or on hardware.

## Roadmap

- [ ] Improve dataset consistency and annotation quality
- [ ] Standardize the codebase into a cleaner module layout
- [ ] Add reproducible training and evaluation scripts
- [ ] Improve documentation and examples for newcomers
- [ ] Explore deployment paths toward real robotic validation

## Recommended project organization

The repository is already functional, but the project is easier to maintain when each concern has a dedicated place:

- `main.py` and other root scripts: entry points and workflow scripts
- `docs/`: technical notes, architecture, and usage documentation
- `data/`: raw or processed datasets
- `logs/`: generated logs and analysis outputs
- `models/`: trained models and model metadata
- `src/`: future library/package code

For the full structure and documentation layout, see `docs/PROJECT_STRUCTURE.md`.

## License

This project is currently distributed under its repository license terms. If a specific license file is added later, it should be respected as the authoritative legal document.

## Contact

- Project: VEXYON
- GitHub: https://github.com/Pokohan/VEXYON-
- Email: youssefmiled20@gmail.com

---

VEXYON is an experimental project at the intersection of computer vision, machine learning, and adaptive robotic grasping.

