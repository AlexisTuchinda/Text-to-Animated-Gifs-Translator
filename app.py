import os

os.environ['KMP_DUPLICATE_LIB_OK']='True' #bypasses an error in local accessing. 

import streamlit as st
#import streamlit.components.v1 as components
from PIL import Image
from image_to_text import get_text
from image_scrape import load_images
from prompts import make_prompts
from testing import current_tests


def pipeline(image_file_buffer):
    urls = []

    image = Image.open(image_file_buffer)

    #generate testing cases
    #image.save("Testing/Unit-Tests/sample-5.jpg")
    
    #image to text
    full_text=get_text(image) 
   
    #segment by sentence and use that to look for gifs
    prompts = make_prompts (full_text)

    #Temporary image scrape & display
    for prompt in prompts:
        temp = load_images(1, prompt)
        for url in temp:
            st.image(url, prompt, 500) #display from url
            urls.append(url) #just in case needs to be referenced for future "saving" capabilities

    #HOW TO DO IMAGE CAROUSEL OR IMAGE SLIDER TO CONTROL IMAGE DISPLAY 
    #WITHOUT MAKING CODE RUN FOREVER OR HAVING WIDGETS BE RESET EVERY SINGLE TIME?
    #formatting would be nice


def home():
    st.title("[software studio project title]")
    st.write("Finds images from Google Search to help decipher instructions from manuals.")

    #camera input
    image_file_buffer = st.camera_input("Take a photo")

    #see testing.py for module testing

    #access the image_file as a pillow image
    # double-check https://docs.streamlit.io/library/api-reference/widgets/st.camera_input --> something wrong with this processing of the image
    if image_file_buffer is not None:
        pipeline(image_file_buffer)

    
home()
current_tests()