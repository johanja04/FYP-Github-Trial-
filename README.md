# Cricket Ball Detection (YOLOv8)

A computer vision project for detecting a cricket ball in video using a YOLOv8 model.
Model trained on videos taken from Bat360 Fareham.

## Project Structure

- `training.py` — trains and validates a YOLOv8 model.
- `testing.py` — runs inference on a video and saves detection results.
- `data.yaml` — dataset configuration for YOLO training.
- `yolo_dataset/` — images and labels for training/validation.
- `runs/` — training checkpoints and detection outputs.

## Requirements

- Python 3.10+
- `pip`
- A virtual environment (`venv`)

## Setup

### Windows

1. Install Python from [python.org/downloads](https://www.python.org/downloads).
2. During installation, enable **Add Python.exe to PATH**.
3. Create and activate a virtual environment:

```bash
python -m venv .venv
.venv\Scripts\activate
```

4. Install dependencies:

```bash
pip install -r requirements.txt
```

### macOS

1. Install Python from [python.org/downloads](https://www.python.org/downloads).
2. Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

### Linux (Ubuntu/Mint)

1. Install Python and venv:

```bash
sudo apt update
sudo apt install -y python3 python3-venv python3-pip
```

2. Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

### 1) Train a model

```bash
python training.py
```

Training outputs are saved under `runs/`.

### 2) Run detection on a video

Before running inference, update the input paths in `testing.py`:

- `model = YOLO('.../best.pt')`
- `source='...your_video.mp4'`

Then run:

```bash
python testing.py
```

Detections are saved under `runs/detect/`.

## Notes

- The current scripts are configured for CPU by default.
- If you move the project folder, update any absolute paths in `testing.py`.