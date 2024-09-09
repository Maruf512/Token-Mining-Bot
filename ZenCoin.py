import cv2
import numpy as np
from PIL import ImageGrab


def zenCoin_Click_Location(tempImage, screenShotArea):
    # load symble
    template = cv2.imread(tempImage)
    # take a screenshot of the screen
    if screenShotArea == "Screen":
        screenshot = np.array(ImageGrab.grab())
    else:
        screenshot = np.array(ImageGrab.grab(bbox=(screenShotArea[0],screenShotArea[1],screenShotArea[2],screenShotArea[3])))
    
    screenshot_np = np.array(screenshot)
    main_image = cv2.cvtColor(screenshot_np, cv2.COLOR_RGB2BGR)

    # Convert both images to grayscale
    main_gray = cv2.cvtColor(main_image, cv2.COLOR_BGR2GRAY)
    template_gray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)

    # Get the width and height of the template
    w, h = template_gray.shape[::-1]

    # Perform template matching
    result = cv2.matchTemplate(main_gray, template_gray, cv2.TM_CCOEFF_NORMED)

    # Define a threshold to determine a match
    threshold = 0.8
    locations = cv2.minMaxLoc(result)

    # Get the best match position
    _, max_val, _, max_loc = cv2.minMaxLoc(result)

    if max_val >= threshold:
        # print(f"Symbol found at location: {max_loc} with matching confidence: {max_val:.2f}")
        # Draw a rectangle around the matched region
        top_left = max_loc
        bottom_right = (top_left[0] + w, top_left[1] + h)
        cv2.rectangle(main_image, top_left, bottom_right, (0, 255, 0), 2)
        

        return [max_loc[0], max_loc[1]]
        
    else:
        # print("Symbol not found with sufficient confidence.")
        return False



    # Display the result
    # cv2.imshow('Detected Symbol', main_image)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

# for i in range(10):
#     print(f"CountDown: {i}")
#     time.sleep(1)

# zenCoin_Click_Location()