import numpy as np
from PIL import ImageGrab
import cv2
import time

x_value = 22
y_value = 5
height_value = 600
width_value = 290

def screen_record():
    last_time = time.time()
    while(True):
        printScreen = np.array(ImageGrab.grab(bbox=(806-x_value,178-y_value,874+width_value,192+height_value)))
        current_time = time.time()
        print("loop took {} seconds".format(current_time-last_time))
        last_time = time.time()
        cv2.imshow('window', cv2.cvtColor(printScreen, cv2.COLOR_BGR2RGB))
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break


screen_record()

