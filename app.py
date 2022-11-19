import os
os.environ['KMP_DUPLICATE_LIB_OK']='True' #bypasses an error in local accessing. 

import streamlit as st
import streamlit.components.v1 as components
from PIL import Image
from image_to_text import get_text
from image_scrape import load_images
from prompts import make_prompts
from testing import current_tests


def pipeline(image_file_buffer):
    image = Image.open(image_file_buffer)

    #generate testing cases
    #image.save("Testing/Unit-Tests/sample-5.jpg")
    
    #image to text
    full_text=get_text(image) 
   
    #segment by sentence and use that to look for gifs
    prompts = make_prompts (full_text)

    #Temporary image scrape & display
    urls = []
    _carousel = components.declare_component("image_carousel", path="carousel/build")

    for prompt in prompts:
        prompt.replace("\n","")
        temp = load_images(1, prompt)
        urls.append(temp[0])
        
    if len(urls) == len(prompts):
        _carousel(urls=urls, prompts=prompts, height=800) # needs a the urls and prompts, they need to be the same length, and the height of the carousel
    else:
        st.write("error")




    #HOW TO DO IMAGE CAROUSEL OR IMAGE SLIDER TO CONTROL IMAGE DISPLAY 
    #WITHOUT MAKING CODE RUN FOREVER OR HAVING WIDGETS BE RESET EVERY SINGLE TIME?
    #formatting would be nice


def home():
    st.title("[software studio project title]")
    st.write("Finds images from Google Search to help decipher instructions from manuals.")

    #camera input
    image_file_buffer = st.camera_input("Take a photo")
    if image_file_buffer is not None:
        pipeline(image_file_buffer)

    

    




        
        


home()
current_tests()