# ServerEye: A-Eye Tracker

**A-Eye Tracker** is a low-cost, innovative software designed to track and analyze pupil movements to assist in diagnosing eye defects. The project integrates neural networks and web applications to deliver precise data visualization and enhance the efficiency of eye-related diagnostics.

---

## Features

- **Neural Network-based Pupil Tracking**: Tracks oscillating pupil positions and generates precise pixel coordinates (X, Y).
- **Web Application Integration**: Visualizes data in a user-friendly interface for analysis and reporting.
- **Low-Cost Solution**: Offers effective tracking without expensive hardware requirements.
- **Impactful Insights**: Aids in better treatment planning by providing accurate tracking results.

---

## Problem Statement

Existing systems face the following challenges:![Eye Defect Tracking    Analyzing-images-18](https://github.com/user-attachments/assets/f42a954f-aafc-4e5a-b3d4-c894c1eed55e)
![Eye Defect Tracking    Analyzing-images-14](https://github.com/user-attachments/assets/224fbab2-73f6-4198-aa95-264f593fae6f)
![Eye Defect Tracking    Analyzing-images-5](https://github.com/user-attachments/assets/ebc89b51-3e4e-4e2d-bdba-2758754ab567)


- Long calibration times.
- Fixed head positioning requirements.
- Difficulty in extracting usable data.

---

## Objectives

- Develop a neural network model for pupil tracking.
- Integrate the model into a scalable web application.
- Provide intuitive data visualization tools for analysis.

---

## Technology Stack

- **Front-End**: Web-based application with data visualization capabilities.
- **Back-End**: Neural networks for image processing.
- **Tools & Libraries**:
  - Python (Neural Network Development)
  - Web technologies (Visualization)

---

## High-Level Architecture

The project architecture focuses on:

- Capturing high-quality video input for eye tracking.
- Analyzing complex eye movements through neural networks.
- Presenting the processed data in a user-friendly manner.

---

## Output Data

The software provides outputs in pixel positions (X, Y) for the following parameters:

- **Right Eye**: RR, RL, RPR, RPL
- **Left Eye**: LL, LR, LPL, LPR

---

## Evaluation

- **Model Testing**: Conducted using various test trials to assess accuracy.
- **Quality of Service (QoS)**: Benchmarked against existing standards in the field.

---

## Limitations

- Accuracy is influenced by environmental factors.
- Complex eye movements may present challenges.
- High-quality video input is necessary for optimal results.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
