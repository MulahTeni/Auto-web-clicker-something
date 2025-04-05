# detecet.py

import pyautogui
import time

while True:
    x, y = pyautogui.position()
    print(f"Mouse konumu: ({x}, {y})", end='\r')
    time.sleep(1)
