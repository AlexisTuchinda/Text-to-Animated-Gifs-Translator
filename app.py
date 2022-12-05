import os

os.environ["KMP_DUPLICATE_LIB_OK"] = "True"  # bypasses an error in local accessing.

import streamlit as st
import streamlit.components.v1 as components
from PIL import Image
from image_gen import gen_images
from image_to_text import get_text
from image_scrape import load_images #Replaced with gen_images
from prompts import make_prompts
from testing import current_tests



def pipeline(image_file_buffer):
    image = Image.open(image_file_buffer)

    # image to text
    full_text = get_text(image)

    # segment by sentence and use that to look for gifs
    prompts = make_prompts(full_text)

    # Temporary image scrape & display
    urls = []

    # SEE CAROUSSEL.md
    _carousel = components.declare_component("image_carousel", path="carousel/build")


    for prompt in prompts:
        prompt.replace("\n", " ")

        #Google Search Option
        temp = load_images(1, prompt)

        #Image Generation Option --> remember to put api key in if used
#        temp = gen_images(prompt) 

        try:
            urls.append(temp[0])
        except:
            urls.append(temp)

    if len(urls) == len(prompts):
        _carousel(
            urls=urls, prompts=prompts, height=500
        )  # needs the urls and prompts, they need to be the same length, and the height of the carousel
    else:
        st.write("error")


def home():
    #logo
    st.title("Text to Animated GIFs (TAG)")

    #instructions - find a way to make this section a drop down?
    with st.expander("Instruction"):
        st.image("res/instructions-tag.gif") 

    #camera input
    image_file_buffer = st.camera_input("Take a photo")
    if image_file_buffer is not None:
       pipeline(image_file_buffer)

    # Testing Image - this is messing me up, the clarity of the image is making tesseract seem better than it is
    #pipeline("Testing/Unit-Tests/Phone/phone-pic.jpg")
    #pipeline("Testing/Unit-Tests/Computer/sample-5.jpg")
    


home()
current_tests()
