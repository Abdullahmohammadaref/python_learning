import time
import numpy as np
from PIL import ImageGrab
import pyautogui

# Target colors in RGB format (active states)
ACTIVE_COLORS = {
    "like": (255, 59, 92),  # Red color
    "favorite": (250, 206, 21)  # Yellow color
}

# Screen region coordinates (X, Y, Width, Height)
BUTTON_REGION = (1555, 240, 268, 163)
X, Y, WIDTH, HEIGHT = BUTTON_REGION

# Coordinates for the scroll down click
SCROLL_CLICK = (1463, 560)


def get_screen_region():
    """Capture the specified screen region."""
    return ImageGrab.grab(bbox=(X, Y, X + WIDTH, Y + HEIGHT))


def find_color_positions(img):
    """Find if either/both colors are present in the image"""
    img_np = np.array(img)
    found = {}

    # Check for each color independently
    for name, color in ACTIVE_COLORS.items():
        mask = np.all(img_np == color, axis=-1)
        if np.any(mask):
            # Get the first matching position (you can modify this to get center if needed)
            y, x = np.argwhere(mask)[0]
            found[name] = (X + x, Y + y)

    return found


def perform_clicks(positions):
    """Click each found position once"""
    for pos in positions.values():
        pyautogui.click(pos)
        time.sleep(1)  # Short pause between different button clicks

def fixer():
    pyautogui.click(822, 92)
    time.sleep(10)
    pyautogui.click(818, 680)
    time.sleep(10)
    pyautogui.click(1372, 400)#1176  396        1372   400
    time.sleep(10)
    pyautogui.click(1007 ,664)
    time.sleep(10)

def main_loop():
    """Main program loop with efficient clicking"""
    time_till_error = time.time()
    while True:

        # fixes the screen back incase an error happens
        if time.time() - time_till_error > 20.0:
            fixer()
            time_till_error = time.time()

        # Capture screen once per iteration
        screen_img = get_screen_region()
        color_positions = find_color_positions(screen_img)

        # Perform clicks only if colors are found
        if color_positions:
            perform_clicks(color_positions)
            time.sleep(1)  # Wait for UI to update after clicking
            time_till_error = time.time()

        # Scroll down regardless of clicks
        pyautogui.click(*SCROLL_CLICK)
        time.sleep(2)  # Adjust this based on your network speed/loading time


if __name__ == "__main__":
    time.sleep(5)
    try:
        print("Starting automation... Press Ctrl+C to stop.")
        main_loop()
    except KeyboardInterrupt:
        print("\nAutomation stopped.")