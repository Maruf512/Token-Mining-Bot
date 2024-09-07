import numpy as np
from PIL import ImageGrab
import cv2
import time


def detect_window(x,y):
    last_time = time.time()
    printScreen = np.array(ImageGrab.grab(bbox=(x,y, x+100, y+50)))
    current_time = time.time()
    print("loop took {} seconds".format(current_time-last_time))
    last_time = time.time()
    cv2.imshow('window', cv2.cvtColor(printScreen, cv2.COLOR_BGR2RGB))
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()


