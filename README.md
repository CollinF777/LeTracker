# LeBron Expression Tracker

A computer vision project that mirrors your facial expressions with matching LeBron reactions in real-time

<img width="1532" height="973" alt="image" src="https://github.com/user-attachments/assets/e8f5aac8-a717-4159-a45e-fc4b4895db73" />


## What It Does

This application uses your webcam to detect your facial expressions and displays corresponding LeBron images based on what you're doing:

- **Screaming/Shouting** → LeBron srceam if you love
- **Wide-eyed/Surprised** → LeBron grinning
- **Squinting/Focused** → LeBron locked in
- **Smiling** → LeSunshine
- **Neutral** → LeBron with his kids watching cartoons

## Requirements

- Python 3.7+
- Webcam
- LeBron images (see Image Setup below)

## Installation

1. Clone this repository
2. Install the required dependencies:

```bash
pip install opencv-python mediapipe
```

## Image Setup

Create a folder named `LeImages` in the same directory as `main.py` and add the following images:

- `lebron_scream_if_you_love.jpg` - LeBron screaming
- `lebron_grin.jpg` - LeBron with a big grin
- `lebron_locked_in.jpg` - LeBron with intense focus
- `lebron_sunshine.jpg` - LeBron smiling blessed in holy light
- `lebron_serious.jpg` - LeBron with a neutral expression

## Usage

Run the application:

```bash
python main.py
```

Two windows will appear:
- **LeTracker**: Your webcam feed with facial landmark tracking
- **Live LeBron Reaction**: LeBron's matching expression

Press `ESC` to exit the application.

## How It Works

The application uses MediaPipe's Face Mesh to detect 468 facial landmarks in real-time. It analyzes specific landmarks to determine:

- **Mouth opening**: Distance between upper and lower lips
- **Eye opening**: Distance between upper and lower eyelids
- **Smile width**: Distance between mouth corners
- **Face proportions**: Uses facial width for relative scaling

These measurements are compared against thresholds to classify your expression and select the matching LeBron image.

## Customization

You can adjust the detection sensitivity by modifying the threshold values (note some have been moved around for certain fixes) in `main.py`:

```python
eye_opening_thresh = 0.036  # Wide eyes detection
squinting_thresh = 0.02     # Squinting detection
```

Additional thresholds for mouth expressions are calculated dynamically based on your face width for better accuracy.

## Troubleshooting

- **Camera not working**: Ensure your webcam is connected and not being used by another application
- **Missing image errors**: Check that all images are in the `LeImages` folder with correct filenames
- **Poor detection**: Ensure good lighting and face the camera directly
- **Mediapipe errors**: Ensure you have the correct version installed, I was having this problem a lot and it turns out pycharm was installing the wrong version
