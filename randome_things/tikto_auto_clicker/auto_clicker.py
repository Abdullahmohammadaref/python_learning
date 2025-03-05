
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
"""
print("Move the mouse to the target position...")
while True:
    x, y = pyautogui.position()
    print(f"X: {x}, Y: {y}", end="\r")
"""
import pyautogui

print("Move your mouse to the FIRST corner (e.g., top-left) and press Enter.")
input()  # Wait for Enter key press
x1, y1 = pyautogui.position()  # Get first corner coordinates

print("Move your mouse to the SECOND corner (e.g., bottom-right) and press Enter.")
input()
x2, y2 = pyautogui.position()  # Get second corner coordinates

# Calculate box properties
x = min(x1, x2)
y = min(y1, y2)
width = abs(x2 - x1)
height = abs(y2 - y1)

print(f"Box Region:\nX: {x}\nY: {y}\nWidth: {width}\nHeight: {height}")
