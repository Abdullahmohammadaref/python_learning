
import pyautogui
import time
"""
# Safety feature: fail-safe if you move the mouse to the top-left corner
pyautogui.FAILSAFE = True

# Delay before the script starts (gives you time to open TikTok)
time.sleep(5)

try:
    while True:
        # Example: Click the "unlike" button (replace x, y with your button's coordinates)
        # To find coordinates, use pyautogui.displayMousePosition()
        like_button_pos = (40, 1035)  # ⚠️ Replace x, y with actual coordinates
        pyautogui.click(like_button_pos)
        time.sleep(1)  # Wait for the action to complete

        # Scroll down to load more videos
        pyautogui.scroll(-500)  # Negative value scrolls down
        time.sleep(4)  # Adjust delay based on app loading time

except KeyboardInterrupt:
    print("Script stopped by user.")
822  92
818  680

1176  396        1372   400

1007 664
"""
print("Move the mouse to the target position...")
while True:
    x, y = pyautogui.position()
    print(f"X: {x}, Y: {y}", end="\r")
