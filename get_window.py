import numpy as np
from PIL import ImageGrab
import cv2
import time


def detect_window():
    last_time = time.time()
    printScreen = np.array(ImageGrab.grab(bbox=(0,1032,1760,1079)))
    current_time = time.time()
    print("loop took {} seconds".format(current_time-last_time))
    last_time = time.time()

    # Display the result
    cv2.imshow('window', cv2.cvtColor(printScreen, cv2.COLOR_BGR2RGB))
    cv2.waitKey(0)
    cv2.destroyAllWindows()


detect_window()
