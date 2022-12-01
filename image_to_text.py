#use pytesseract (follow tutorials) --> create function which will pass in the camera input from app

import pytesseract
import cv2
import numpy as np
import streamlit as st

#this is the exe file for tesseract
pytesseract.tesseract_cmd = r"C:/opt/anaconda3/envs/streamlit/bin"

def get_text(image):

    img = clear_image(np.array(image))

    # https://stackoverflow.com/questions/64099248/pytesseract-improve-ocr-accuracy
    config = '--oem 3 --psm %d' % 3 #psm = page segmentation; "single character recognition" = psm 10 --> but we want full page (see resource below)
    #https://pyimagesearch.com/2021/11/15/tesseract-page-segmentation-modes-psms-explained-how-to-improve-your-ocr-accuracy/

    text = pytesseract.image_to_string(img, config = config, lang='eng')
    st.write(text)

    return text

def clear_image(img):
    #debugging purposes
    st.image(img)

    cut_away()

    #clearing noise 
    #the third attribute should be played around between 10 - 15; seems to be good range to at least make the image clearer for tesseract to interpret... 
    noiseless_image_bw = cv2.fastNlMeansDenoising(np.array(img), None, 15, 7, 21) 
    
    #turning to gray to isolate letters & inverting to make lettering more clear
    im_gray = cv2.cvtColor(noiseless_image_bw, cv2.COLOR_BGR2GRAY)
    gray = cv2.bitwise_not(im_gray)

    #debugging
    st.image(noiseless_image_bw)
    st.image(im_gray)
    st.image(gray)
    
    return gray 

def cut_away():
    #https://learnopencv.com/automatic-document-scanner-using-opencv/#Getting-Started-with-OpenCV-Document-Scanner
    pass