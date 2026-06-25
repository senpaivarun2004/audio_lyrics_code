# Sahiba - Animated Lyrics Player

A Python script that plays the song **Sahiba** and displays synchronized, typewritten lyrics in the terminal in real-time.

## Features

- **Audio Playback**: Plays the background track (`sahiba_audio.mp3.mp3`) using `pygame`.
- **Synchronized Typing Effect**: Automatically scrolls and typewrites the lyrics matching the song's specific timestamps.
- **Terminal Animation**: Custom character-by-character typing speed based on duration between timestamps.

## Prerequisites

Make sure you have Python installed, along with the `pygame` library:

```bash
pip install pygame
```

## Setup & Running

1. Ensure the audio file `sahiba_audio.mp3.mp3` is in the same directory as the script.
2. Run the script:

```bash
python sahiba.py
```

## Customizing Timestamps

The script uses a hardcoded list of timestamps under `timed_lyrics`:
```python
timed_lyrics = [
    (0.5,  "Baato-baato me hi, Khwabo-khwabo me hi mere qareeb hai tu"),
    ...
]
```
To adjust the timing or generate new timestamps, you can use the **Calibration Tool** located in the `calibrate/` directory.
