# Driver Drowsiness Detection using YOLOv8

## Overview

This project detects driver drowsiness in real time using a webcam and a custom-trained YOLOv8 model.

## Features

- Detects Eyes Opened
- Detects Eyes Closed
- Detects Yawning
- Real-time webcam detection
- Alerts for drowsiness

## Technologies

- Python
- OpenCV
- Ultralytics YOLOv8
- NumPy

## Dataset

Custom dataset with three classes:

- Eyes Opened
- Eyes Closed
- Yawning

## Installation

```bash
pip install ultralytics
pip install opencv-python
pip install numpy
```

## Run

```bash
python webcam.py
```

## Project Structure

```
Driver-Drowsiness-Detection/
│
├── dataset/
├── runs/
├── webcam.py
├── train.py
├── predict.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Author

Saideepu Balaraju
