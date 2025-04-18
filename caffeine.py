import time
import keyboard
from datetime import datetime

INTERVAL = 59  # seconds between key presses

def keep_active():
    print(" Python Caffeine is running – simulating activity every", INTERVAL, "seconds.")
    print("Press Ctrl+C to stop.\n")

    try:
        while True:
            keyboard.press_and_release('f15')  # Harmless key
            print(f"[{datetime.now().strftime('%H:%M:%S')}] F15 key press simulated.")
            time.sleep(INTERVAL)
    except KeyboardInterrupt:
        print("\n Caffeine stopped by user.")

if __name__ == "__main__":
    keep_active()
