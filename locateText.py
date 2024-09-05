import numpy as np   
import pytesseract
import cv2 
from PIL import ImageGrab
from generateText import imToString
import pyautogui, time

# Make sure to point pytesseract to the location of your installed Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\maruf\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'  # Modify this path for your system

# Load the image where you want to find the text

def SearchEngine():
    screenshot = pyautogui.screenshot()
    screenshot_np = np.array(screenshot)
    image = cv2.cvtColor(screenshot_np, cv2.COLOR_RGB2BGR)
    
    # Convert image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Use pytesseract to extract text data
    data = pytesseract.image_to_data(gray, output_type=pytesseract.Output.DICT)

    # Loop through detected text and its position
    for i in range(len(data['text'])):
        if int(data['conf'][i]) > 60:  # Confidence threshold
            x, y, w, h = data['left'][i], data['top'][i], data['width'][i], data['height'][i]
            text = data['text'][i]
            print(f"Text: {text} located at ({x}, {y}) with width {w} and height {h}")

            if "ZenCoin" in text:
                print("++++++++++++++++++++++++++++++++++++++++++")
                imToString(x,y,width=x+w + 5,height=y+h + 5)
                print(f"location({x},{y},{x+w},{y+h})")
                print("++++++++++++++++++++++++++++++++++++++++++")
                

            # Draw rectangle around the text
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)



# main loop
while True:
    SearchEngine()
    time.sleep(1)
    

# Display the image with detected text highlighted
# cv2.imshow('Detected Text', image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
