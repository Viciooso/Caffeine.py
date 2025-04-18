# Python Caffeine – Keep Your PC Active

This lightweight Python script simulates keyboard activity to prevent your system (and Microsoft Teams) from going into "Away" status.

It works similarly to the app [Caffeine](https://www.zhornsoftware.co.uk/caffeine/) by sending a harmless key press (`F15`) at regular intervals.

---

## Features

- Keeps your status active by pressing `F15` every 59 seconds.
- Simple terminal output to monitor activity.
- Can be turned into a `.exe` file for double-click use.
- No real impact on system or applications.

---

## Getting Started

### 1. Clone or download the script

```bash
git clone https://github.com/your-repo/python-caffeine-lite.git
cd python-caffeine-lite

### 2. Install the required library
pip install keyboard

### 3. Run the script
python caffeine.py
