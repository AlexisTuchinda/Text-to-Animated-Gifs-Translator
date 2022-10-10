#use pytesseract (follow tutorials) --> create function which will pass in the camera input from app

import pytesseract
import cv2
import numpy as np

pytesseract.tesseract_cmd = r"C:/opt/anaconda3/envs/streamlit/bin"

def get_text(image): #NOT GOOD ENOUGH --> https://tesseract-ocr.github.io/tessdoc/ImproveQuality.html
    #figure out what from the link above I can do to improve based on the sample images
    #https://towardsdatascience.com/image-processing-using-streamlit-d650fb0ccf8

    img= clear_image(image)

    text = pytesseract.image_to_string(img)
    return text


def clear_image(image):
    #fix skew


    #get better clarity - binarization method to gray so better isolation of words. 
    im_gray = cv2.cvtColor(np.array(image), cv2.COLOR_BGR2GRAY)

    return im_gray