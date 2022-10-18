#use pytesseract (follow tutorials) --> create function which will pass in the camera input from app

import pytesseract
import cv2
import numpy as np
import streamlit as st

pytesseract.tesseract_cmd = r"C:/opt/anaconda3/envs/streamlit/bin"

def get_text(image):

    #currently the resizing seems to work, but the tesseract data box is not doing it around the text... 
    #img= clear_image(transform(image)) 

    resize_text(image)
    img = clear_image(np.array(image))

    #account for "waviness" / perspective on image?: https://stackoverflow.com/questions/64099248/pytesseract-improve-ocr-accuracy
    config = '--oem 3 --psm %d' % 3 #psm = page segmentation; "single character recognition" = psm 10 --> but we want full page (see resource below)
    #https://pyimagesearch.com/2021/11/15/tesseract-page-segmentation-modes-psms-explained-how-to-improve-your-ocr-accuracy/

    text = pytesseract.image_to_string(img, config = config, lang='eng')
    st.write(text)

    return text

def transform(image):
   pass

def clear_image(img):
    
    #clearing noise and turning image to gray to better isolate
    noiseless_image_bw = cv2.fastNlMeansDenoising(img, None, 10, 7, 21) 
    im_gray = cv2.cvtColor(noiseless_image_bw, cv2.COLOR_BGR2GRAY)

    st.image(noiseless_image_bw)
    st.image(im_gray)

    return im_gray 
