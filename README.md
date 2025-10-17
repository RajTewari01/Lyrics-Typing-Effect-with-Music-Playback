# 🎵 Lyrics Typing Effect with Music Playback

![Python](https://img.shields.io/badge/Python-3.10+-blue) ![Rich](https://img.shields.io/badge/Rich-Yes-green) ![Pygame](https://img.shields.io/badge/Pygame-Yes-green)

Welcome to the **Lyrics Typing Effect** project! 🖥️🎶 This Python script displays song lyrics in a **typewriter-style animation** directly in your terminal while playing the song in the background. Lyrics are dynamically colored using the `rich` library, and music playback is handled with `pygame`. Perfect for music lovers, Python enthusiasts, or anyone wanting a cool console-based music visualizer! 🌈✨

---

### 🎬 Demo

![Lyrics Typing Effect Demo](demo.gif)

> The GIF above shows the typewriter animation with cycling colors while the song plays in the background.

---

### ✨ Features

- 🎹 Typewriter-style printing of lyrics, character by character.  
- 🌈 Multi-color cycling for letters or lines.  
- 🎵 Background music playback (MP3 supported via `pygame`).  
- ⏱ Adjustable typing speed and line delays.  
- 💻 Works on Windows, macOS, and Linux terminals.  

---

### 🛠️ Requirements

- Python 3.10+  
- Libraries:  
  - `pygame` → `pip install pygame`  
  - `rich` → `pip install rich`  

---

### 🚀 Usage

1. Place your MP3 song in the same folder or provide the full path.  
2. Define your lyrics as a list of strings, each representing a line:  

```python
lyrics_list_5_words = [
    "This night is cold in",
    "the kingdom I can feel",
    "you fade away From the",
    # ... add all lines here
]
song_path = "D:/song/song.mp3"
song_name = "Let Me Down Slowly"
