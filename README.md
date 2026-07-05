# Driver Drowsiness Detection System using YOLOv8

## Overview

The **Driver Drowsiness Detection System** is a real-time computer vision application that detects driver fatigue using a webcam and a custom-trained YOLOv8 model. The system identifies signs of drowsiness such as closed eyes and yawning, helping improve road safety by providing timely detection.

---

## Features

- Real-time driver monitoring using a webcam
- Detects **Eyes Opened**
- Detects **Eyes Closed**
- Detects **Yawning**
- Confidence score displayed for each detection
- Fast and accurate object detection using YOLOv8
- Easy to train with custom datasets

---

## Technologies Used

- Python
- YOLOv8 (Ultralytics)
- OpenCV
- NumPy
- PyTorch

---

## Project Structure

```
Driver-Drowsiness-Detection-System/
│
├── confidence.py
├── confidence_log.txt
├── data.yaml
├── requirements.txt
├── resume_train.py
├── test.py
├── train.py
├── webcam.py
├── webcam_confidence.py
├── .gitignore
└── README.md
```

---

## Installation

### Clone the Repository

```bash
git clone https://github.com/SAIDEEPUBALARAJU-2003/Driver-Drowsiness-Detection-System.git
```

### Move into the Project Directory

```bash
cd Driver-Drowsiness-Detection-System
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Training the Model

Train the YOLOv8 model using:

```bash
python train.py
```

---

## Resume Training

If training is interrupted, continue training with:

```bash
python resume_train.py
```

---

## Testing the Model

```bash
python test.py
```

---

## Real-Time Detection

Start webcam detection:

```bash
python webcam.py
```

For confidence-based detection:

```bash
python webcam_confidence.py
```

---

## Dataset Classes

The model is trained to detect the following classes:

- Eyes Opened
- Eyes Closed
- Yawning

---

## Applications

- Driver Safety Systems
- Intelligent Transportation Systems
- Fleet Monitoring
- Accident Prevention
- Automotive AI Solutions

---

## Future Enhancements

- Audio alarm for drowsiness detection
- Mobile application integration
- Cloud-based monitoring
- Night vision support
- Face recognition for multiple drivers
- Eye Aspect Ratio (EAR) integration

---

## Requirements

- Python 3.10+
- OpenCV
- Ultralytics YOLOv8
- PyTorch
- NumPy

---

## Author

**Saideepu Balaraju**
