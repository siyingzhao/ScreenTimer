# ScreenTimer

# Transparent Multi-functional Timer

This is a simple multi-functional timer application with the following features:

- Transparent background
- Always stays on top (visible even during PowerPoint presentations)
- Supports both count-up and countdown modes
- Includes start/pause, reset, and mode switching functions
- Can be dragged to any position on the screen

## How to Use

### Count-up Mode

1. When you run the program, it defaults to count-up mode with time display initialized as "00:00:00" (hours:minutes:seconds)
2. Click the "Start" button to begin counting
3. Click the "Pause" button to pause, and "Continue" to resume
4. Click the "Reset" button to reset the timer to zero

### Countdown Mode

1. Click the "Switch to Countdown" button to switch to countdown mode
2. Set hours, minutes, and seconds in the dialog that appears
3. Click the "Start" button to begin the countdown
4. Click the "Pause" button to pause, and "Continue" to resume
5. Click the "Reset" button to set a new countdown time
6. When the countdown finishes, the time display turns red as an alert

### Other Features

- Click the "Exit" button to close the program
- You can drag the interface anywhere on screen with the left mouse button
- Click the "Switch to Count-up/Switch to Countdown" button to toggle between modes

## How to Compile

1. Make sure you have the required Python libraries: `pip install PyQt5 pyinstaller`
2. Run the packaging script: `python build_exe.py`
3. Find the generated executable file in the dist folder

[中文版](README.md)
