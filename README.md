AI Grip Pressure Estimation for Robotic Grasping

AI-powered robotic grasping: estimate grip pressure from a webcam using MediaPipe + machine learning — no force sensor required.

Documentation An AI robotics project capable of interacting with its physical environment and performing adaptive grasping tasks.Project Architecturerobot_project/
├── config.py                  # ⚙️  Centralized configuration (paths, parameters)
├── main.py                    # 📷  Dataset capture (webcam + MediaPipe)
├── merge_csv.py               # 🔀  CSV merging by object
├── clean_dataset.py           # 🧹  Dataset cleaning and preparation
├── analyse.py                 # 📊  Statistical analysis + graphics
├── train_model.py             # 🧠  ML model training
├── test_model.py              # ✅  Model testing and validation
├── detection.py               # 👁️  Object detection via camera (OpenCV)
├── robot_autonome.py          # 🦾  Decision-making brain (FSM + ML)
├── simulate_robot_visual.py   # 🎮  Interactive visual simulation
├── pipeline.py                # 🚀  Full automated pipeline
└── logs/                      # 📁  Logs, graphics, reports
Recommended WorkflowStep 1 — Capture DataBashpython main.py
# Enter the object name (e.g., water_bottle)
# [8] increase pressure  [2] decrease pressure  [SPACE] pause  [Q] quit

Step 2 — Run the Full PipelineBashpython pipeline.py
This executes the following sequence: merge → clean → analyze → train.Step 3 — Test the ModelBashpython test_model.py --batch      # evaluation on the entire dataset
python test_model.py              # interactive test

Step 4 — Simulate the RobotBashpython simulate_robot_visual.py   # visual simulation
python robot_autonome.py          # decision-making simulation

# Terminal 2 (optional): Publish sensor data
rostopic pub /sensor/landmarks std_msgs/Float64MultiArray "data: [...]" -r 10
For the complete installation and configuration guide: see GAZEBO_SETUP.mdDependenciesBashpip install opencv-python mediapipe scikit-learn pandas numpy matplotlib joblib


License

Copyright (c) 2026 Vexyon / Youssef Miled. All rights reserved.
For commercial licensing, enterprise integration, or inquiries, please contact: youssefmiled20@gmail.com

You are free to:

    Share: copy and redistribute the material in any medium or format.
    
    Adapt: remix, transform, and build upon the material.

Under the following terms:

    Attribution: You must give appropriate credit, provide a link to the license, and indicate if changes were made.

    NonCommercial: You may not use the material for commercial purposes.

    ShareAlike: If you remix, transform, or build upon the material, you must distribute your contributions under the same license as the original.
