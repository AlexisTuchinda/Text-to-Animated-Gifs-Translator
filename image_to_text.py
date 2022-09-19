#use pytesseract (follow tutorials) --> create function which will pass in the camera input from app

from pillow import Image
from pytesseract import pytesseract

pytesseract.tesseract_cmd = r"C:/opt/homebrew/bin/tesseract.exe"

def get_text(image):
    #return text 

    text = pytesseract.image_to_string(image)
    return text[:-1]

    