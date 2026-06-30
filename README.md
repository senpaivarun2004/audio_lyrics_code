# 🎵 SyncLyrics & Audio Analyzer 🎵

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Library](https://img.shields.io/badge/pygame-v2.0%2B-darkgreen?style=for-the-badge&logo=python&logoColor=white)](https://www.pygame.org/)
[![Library](https://img.shields.io/badge/librosa-audio-orange?style=for-the-badge&logo=scipy&logoColor=white)](https://librosa.org/)
[![License](https://img.shields.io/badge/license-MIT-red?style=for-the-badge)](https://opensource.org/licenses/MIT)

An interactive, synchronized terminal lyrics player, dynamic calibrator, and audio feature analysis toolkit built in Python. Experience music and lyrics side-by-side in your terminal, calibrate timestamps in real-time, or analyze audio waveforms for tempo, beats, and vocal onsets.

---

## ✨ Features

- 🎹 **Animated Lyrics Player (`sahiba/`)**: Plays background tracks and outputs synchronized, typewritten lyrics in real-time. Typing speed is dynamically calculated to match song pacing.
- ⏱️ **Lyric Calibration Tool (`calibrate/`)**: Press `ENTER` to the beat or vocals to record precise, real-time timestamps for any track and auto-generate copy-pasteable Python lyric structures.
- 📊 **Audio Waveform Analyzer (`analyze_audio.py`)**: Uses DSP (Digital Signal Processing) to detect tempo (BPM), calculate RMS energy boundaries, and locate acoustic/vocal onset transitions.

---

## 📂 Project Structure

```directory
lyrics_audio_code/
├── 📄 analyze_audio.py       # Audio analysis (BPM, onsets, RMS energy)
├── 🎵 sahiba_audio.mp3.mp3   # Background audio file
├── 📂 sahiba/                # Lyrics Player Component
│   ├── 📄 sahiba.py          # Typographic synced player
│   └── 📄 README.md          # Player-specific documentation
└── 📂 calibrate/             # Lyric Calibrator Component
    ├── 📄 calibrate.py       # Interactive timing recorder
    └── 📄 README.md          # Calibrator-specific documentation
```

---

## 🚀 Quick Start

### 1. Installation

Install all required audio processing and playback dependencies:

```bash
pip install pygame librosa numpy
```

> [!NOTE]
> `librosa` requires system-level audio decoders (like `ffmpeg`) to load MP3 files on some platforms.

---

## 🛠️ Usage Guides

### 🎵 1. Run the Synced Lyrics Player
Play the song **Sahiba** with typing terminal animation matching the song vocals.

```bash
cd sahiba
python sahiba.py
```

### ⏱️ 2. Calibrate New Timestamps
If you want to sync lyrics for a different song or re-calibrate the current lyrics:

```bash
cd calibrate
python calibrate.py
```
- Listen to the music.
- Press `ENTER` when you hear the beginning of the displayed lyric line.
- Copy the generated `timed_lyrics` array and paste it into [sahiba.py](file:///c:/Users/senpq/Projects/lyrics_audio_code/sahiba/sahiba.py).

### 📊 3. Analyze Audio Attributes
Extract features such as estimated tempo, beat counts, and onset locations:

```bash
python analyze_audio.py
```

---

## 🎨 Tech Stack & Libraries

- **[Pygame Mixer](https://www.pygame.org/docs/ref/mixer.html)**: Low-latency audio playback control.
- **[Librosa](https://librosa.org/)**: Music and audio analysis, onset detection, and beat tracking.
- **[NumPy](https://numpy.org/)**: Fast mathematical operations on audio arrays.

---

<div align="center">
  Developed with ❤️ for music and terminals.
</div>
