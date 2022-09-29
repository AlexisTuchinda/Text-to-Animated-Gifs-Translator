#use pytesseract (follow tutorials) --> create function which will pass in the camera input from app

from PIL import Image
import pytesseract

pytesseract.tesseract_cmd = r"C:/opt/anaconda3/envs/streamlit/bin" #it's in anaconda navigator!!!!

def get_text(image): #see if this will work without path input
    text = pytesseract.image_to_string(image)
    return text

# IT WORKS --> now try plugging this into the image scrape... 