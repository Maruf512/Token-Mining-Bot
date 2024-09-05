import numpy as nm   
import pytesseract
import cv2 
from PIL import ImageGrab


def imToString(x, y, width, height):

    pytesseract.pytesseract.tesseract_cmd = r'C:\Users\maruf\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

    cap = ImageGrab.grab(bbox =(x,y,width,height))
    tesstr = pytesseract.image_to_string( 
            cv2.cvtColor(nm.array(cap), cv2.COLOR_BGR2GRAY),  
            lang ='eng') 
    print(tesstr)



