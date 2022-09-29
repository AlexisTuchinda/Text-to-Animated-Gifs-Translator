import os

os.environ['KMP_DUPLICATE_LIB_OK']='True'

import streamlit as st
from PIL import Image
from image_to_text import get_text
from prompting import *
#from model.py import --> use model.py as the official model file; use the jupyter notebook (ipynb) as the "testing area"

def create_gif(series):
    #follow the tutorial for iterating through the images to create an "animation"...
        #concern for having the same context... depending on output, see if it makes sense to make animated or to display side by side
    pass

def home():
    st.title("[software studio project title]")
    st.write("Create images from instructions to help decipher manuals.")

    image_file_buffer = st.camera_input("Take a photo")

    #access the image_file as a pillow image
    # double-check https://docs.streamlit.io/library/api-reference/widgets/st.camera_input --> something wrong with this processing of the image
    if image_file_buffer is not None:
        image = Image.open(image_file_buffer)
        text=get_text(image)
        print (text)
    


home()