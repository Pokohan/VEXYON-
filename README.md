# VEXYON — AI-Assisted Robotic Grasping

**An AI robotics project exploring adaptive grasping through computer vision and machine learning.**

[Watch the Project Presentation](https://youtu.be/nXF1zteT9B8)

VEXYON explores how computer vision and machine learning can help a robotic system estimate an appropriate grip level when handling different objects.

The project uses hand landmarks extracted with MediaPipe, a machine learning pipeline, and a simulated decision-making system to investigate adaptive grasping.

---

## Table of Contents

- [Project Overview](#project-overview)
- [How It Works](#how-it-works)
- [Project Architecture](#project-architecture)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Dataset and Privacy](#dataset-and-privacy)
- [Limitations](#limitations)
- [Roadmap](#roadmap)
- [License](#license)
- [Contact](#contact)

---

## Project Overview

VEXYON is an experimental project focused on the relationship between human grasping, computer vision, and robotic decision-making.

The main objectives are to:

- Capture hand landmark data using a webcam.
- Associate recorded hand configurations with grip-pressure labels.
- Prepare and analyze collected data.
- Train and evaluate a machine learning model.
- Explore object detection and autonomous decision-making.
- Simulate parts of a future robotic grasping workflow.

The long-term objective is to investigate how these components could contribute to safer, more adaptive robotic manipulation.

## How It Works

The software is organized around the following workflow:

1. **Data collection** — Capture hand landmarks using a webcam and MediaPipe.
2. **Data preparation** — Merge, clean, and organize CSV datasets.
3. **Model training** — Train a machine learning model using the prepared data.
4. **Evaluation** — Test the model and analyze its predictions.
5. **Simulation** — Explore decision-making and autonomous behavior in software.

### Important distinction

The current approach estimates a label learned from the training data. Hand landmarks alone do not directly measure physical grip force.

Reliable force control on a physical robot would require additional validation, appropriate reference measurements, and integration with suitable hardware.

## Project Architecture

```text
robot_project/
├── config.py                  # Centralized configuration
├── main.py                    # Webcam data collection
├── merge_csv.py               # Dataset merging
├── clean_dataset.py           # Dataset cleaning
├── analyse.py                 # Statistical analysis and graphics
├── train_model.py             # Model training
├── test_model.py              # Model evaluation and testing
├── detection.py               # Object detection with OpenCV
├── robot_autonome.py          # Decision-making (FSM + ML)
├── simulate_robot_visual.py   # Visual simulation
├── bridge_gazebo.py           # ROS/Gazebo integration
├── pipeline.py                # Automated data pipeline
└── logs/                      # Logs and generated reports
```

*This tree describes the intended project structure. The availability and status of individual files may vary between versions.*

## Requirements

The project uses Python and computer vision / machine learning libraries.

- Python
- OpenCV
- MediaPipe
- scikit-learn
- NumPy
- pandas
- Matplotlib
- joblib

Some optional components may require additional robotics software, such as ROS and Gazebo.

## Installation

Clone the repository:

```bash
git clone https://github.com/Pokohan/VEXYON-.git
cd VEXYON-
```

Install the Python dependencies:

```bash
python -m pip install opencv-python mediapipe scikit-learn pandas numpy matplotlib joblib
```

**Note:** Run the commands from the directory containing the project files. Depending on the repository structure and your Python environment, you may need to adjust the working directory or dependency versions.

## Usage

### 1. Capture data

Run the data collection script:

```bash
python main.py
```

Follow the prompts displayed by the application to name the object and record hand landmark samples.

The documented keyboard controls are:

| Key | Action |
|---|---|
| `8` | Increase the pressure label |
| `2` | Decrease the pressure label |
| `SPACE` | Pause recording |
| `Q` | Quit |

These controls describe the label-recording workflow; they do not constitute direct physical force measurement.

### 2. Run the data pipeline

```bash
python pipeline.py
```

The intended pipeline performs dataset merging, cleaning, analysis, and model training.

### 3. Evaluate the model

Run batch evaluation:

```bash
python test_model.py --batch
```

Or launch the interactive test:

```bash
python test_model.py
```

Use the evaluation results to assess model performance rather than relying solely on successful execution.

### 4. Explore the simulation

Run the visual simulation:

```bash
python simulate_robot_visual.py
```

Explore the autonomous decision-making workflow:

```bash
python robot_autonome.py
```

### 5. Optional ROS integration

If the ROS bridge is configured and the required ROS environment is running, sensor data may be published to the relevant topic.

Example command documented for the project:

```bash
rostopic pub /sensor/landmarks std_msgs/Float64MultiArray "data: [...]" -r 10
```

Replace the placeholder data with valid values matching the configured message format. This command alone does not establish a complete connection to a physical robot.

## Dataset and Privacy

VEXYON's training dataset is not publicly distributed.

Keeping the dataset private helps protect the time and effort invested in data collection and preparation.

The repository can still document the methodology, software workflow, limitations, and evaluation approach without exposing the underlying data.

Dataset privacy does not, by itself, guarantee ownership of every underlying idea or provide complete intellectual-property protection.

## Limitations

VEXYON is an experimental software project. Important limitations include:

- Predictions depend on the quality and coverage of the training data.
- Hand landmarks are not direct measurements of grip force.
- Manually assigned labels may not correspond to objectively measured physical pressure.
- Performance must be evaluated on data that was not used for training.
- Simulation results do not automatically translate to real-world robotic performance.
- Physical force control and safe manipulation require additional testing and validation.

## Roadmap

Potential future development goals include:

- [ ] Improve dataset quality and labeling consistency.
- [ ] Evaluate generalization to unfamiliar objects and hand configurations.
- [ ] Document reproducible evaluation metrics.
- [ ] Improve the object-detection and decision-making pipeline.
- [ ] Expand simulation and robotics integration.
- [ ] Investigate physical force sensing and real-world robotic validation.

These items are development goals, not claims of completed functionality.

## License

**Copyright © 2026 Youssef Miled / VEXYON.**

All rights reserved, subject to the terms of any license explicitly published with this repository.

For commercial licensing, enterprise integration, or other inquiries, contact:

**youssefmiled20@gmail.com**

No permission to redistribute, modify, or commercially exploit the project should be inferred beyond the permissions expressly granted by the applicable license.

## Contact

For project-related inquiries, commercial licensing, or collaboration:

- **Project:** VEXYON
- **GitHub:** [Pokohan/VEXYON-](https://github.com/Pokohan/VEXYON-)
- **Email:** youssefmiled20@gmail.com

---

*VEXYON is an ongoing exploration of computer vision, machine learning, and adaptive robotic grasping.*
