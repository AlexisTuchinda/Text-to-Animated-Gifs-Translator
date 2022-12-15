#use pytesseract (follow tutorials) --> create function which will pass in the camera input from app

import pytesseract
import numpy as np
import streamlit as st
import imutils


#this is connection to exe file, originally supported for local hosting of this app
pytesseract.tesseract_cmd = "holding/tesseract_exe/tesseract"
#there is a packages txt for utilizing tesseract on the streamlit app (public)

def get_text(image):
    
    image = imutils.rotate(np.array(image), angle=-90)

    st.image(image)

    config = '--oem 3 --psm %d' % 3 #psm = page segmentation; "single character recognition" = psm 10 --> but we want full page (see resource below)
    text = pytesseract.image_to_string(image, config = config, lang='eng')

    st.write(text)

    return text

