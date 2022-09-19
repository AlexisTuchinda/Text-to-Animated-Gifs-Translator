import streamlit as st
from image_to_text import get_text
from gen_image import create_series
#from model.py import --> use model.py as the official model file; use the jupyter notebook (ipynb) as the "testing area"

def create_gif(series):
    #follow the tutorial for iterating through the images to create an "animation"...
        #concern for having the same context... depending on output, see if it makes sense to make animated or to display side by side
    pass

def home():
    st.title("[software studio project title]")
    st.write("Create images from instructions to help decipher manuals.")

    image = st.camera_input("Take a photo") #there is a problem with enabling camera in the laptop preferences - is this something that Nueva has restricted on this laptop specifically?

    #model to read text from photo
    #model/algorithm to take that text and segment it
    #model to generate images based on text
    #process images into animation

home()