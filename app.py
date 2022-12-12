import os

os.environ["KMP_DUPLICATE_LIB_OK"] = "True"  # bypasses an error in local accessing.

import streamlit as st
import streamlit.components.v1 as components
from PIL import Image
from holding.image_gen import gen_images
from image_to_text import get_text
from image_scrape import load_images #Replaced with gen_images
from prompts import make_prompts
from Testing.testing import current_tests



def pipeline(image_file_buffer):
    image = Image.open(image_file_buffer)

    # image to text
    full_text = get_text(image)

    # segment by sentence and use that to look for gifs
    prompts = make_prompts(full_text)

    # Temporary image scrape & display
    urls = []

    _carousel = components.declare_component("image_carousel", path="carousel/build")

    for prompt in prompts:
        prompt.replace("\n", " ")

        #Google Search Option
        temp = load_images(1, prompt)

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
    

    image = st.file_uploader("Upload photo of page / document", [".png", ".jpg", ".jpeg"])    
    if image is not None:
        pipeline(image)


home()
current_tests()
