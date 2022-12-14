#use pytesseract (follow tutorials) --> create function which will pass in the camera input from app

import pytesseract
import cv2
import numpy as np
import streamlit as st

from holding.scanner import scan

#this is connection to exe file, originally supported for local hosting of this app
pytesseract.tesseract_cmd = "holding/tesseract_exe/tesseract"

def get_text(image):
    selected = False #just to regulate sync between drop down option and the pipeline 

    option = st.selectbox("", ("Are you using a phone 📱 or a computer 💻?", "Phone 📱", "Computer 💻"))
    
    if option == "Computer 💻":
        selected = True
        img = clear_image(np.array(image))
    elif option == "Phone 📱":
        selected = True
        img = clear_phone_image(np.array(image))
    else:
        selected = False

    if selected: 
        # https://stackoverflow.com/questions/64099248/pytesseract-improve-ocr-accuracy
        config = '--oem 3 --psm %d' % 3 #psm = page segmentation; "single character recognition" = psm 10 --> but we want full page (see resource below)
        #https://pyimagesearch.com/2021/11/15/tesseract-page-segmentation-modes-psms-explained-how-to-improve-your-ocr-accuracy/

        text = pytesseract.image_to_string(img, config = config, lang='eng')
        st.write(text)

        return text
    else:
        return "- Waiting -"

def clear_image(img):

    #test = scan(img)
    #st.image(test)

    #clearing noise 
    #the third attribute should be played around between 10 - 15; seems to be good range to at least make the image clearer for tesseract to interpret... 
    noiseless = cv2.fastNlMeansDenoising(np.array(img), None, 15, 7, 21) 
    
    #turning to gray to isolate letters & inverting to make lettering more clear
    gray = cv2.cvtColor(noiseless, cv2.COLOR_BGR2GRAY)

    inv = cv2.bitwise_not(gray)

    return inv 

def clear_phone_image(img):

    #FILL
    
    return img