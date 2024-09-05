import pyautogui
import time

target = 850
current = 0

time.sleep(5)

while target > current:
    pyautogui.click(button='left')
    current += 1
    print(current)