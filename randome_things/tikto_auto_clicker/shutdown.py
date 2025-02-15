import pyautogui
import time
import sys

start_time = time.time()
with open("error.txt", "a") as f:
    f.write(f"{time.time() - start_time}\n")
pyautogui.moveTo(583, 1079)
time.sleep(1)
pyautogui.click(709, 1049)
time.sleep(1)
pyautogui.click(1270, 961)
time.sleep(1)
pyautogui.click(1258, 869)
pyautogui.click(1258, 869)
sys.exit()
