import os

os.environ['KMP_DUPLICATE_LIB_OK']='True'

import streamlit as st
from PIL import Image
from image_to_text import get_text
from prompting import process
from image_scrape import load_images

def home():
    st.title("[software studio project title]")
    st.write("Finds images from instructions to help decipher manuals.")

    image_file_buffer = st.camera_input("Take a photo")

    #access the image_file as a pillow image
    # double-check https://docs.streamlit.io/library/api-reference/widgets/st.camera_input --> something wrong with this processing of the image
    if image_file_buffer is not None:
        pipeline(image_file_buffer)
    
def pipeline(image_file_buffer):
    urls_in_use = []

    image = Image.open(image_file_buffer)
    
    #image to text
    text=get_text(image) 
    print (text)
    
    #prompting.py
    prompts = process(text)
    print(prompts)

    #image scrape & display
    for prompt in prompts:
        temp = load_images(3, prompt, "gif")
        for url in temp:
            st.markdown("![Image]("+url+")")#display from url
            urls_in_use.append(url)



home()