from image_gen import gen_images
from image_to_text import clear_image, get_text
from image_scrape import load_images
from prompts import make_prompts
import streamlit as st

image_file_buffer = "Testing/Unit-Tests/sample-5.jpg" #change image here

def test_generate():
    st.write("testing image generation corresponding to prompts")
    prompts = [""] #input random prompts that follow from a manual
    gen_images(prompts)

def test_preprocessing():
    st.write("testing preprocessing")
    clear_image(image_file_buffer)

def test_tesseract():
    st.write("testing tesseract")
    get_text(image_file_buffer)

def test_scrape():
    st.write("testing scrape correspond to prompts")
    prompts = [""] #input random prompts that follow from a manual
    load_images(prompts)

def test_prompts():
    text = "" #this may just work from taking one of the outputs from a non-testing run
    make_prompts(text)

def test_pipeline():
    for prompt in make_prompts(get_text(image_file_buffer)):
        temp = load_images(1, prompt)
        for url in temp:
            st.image(url, prompt, 500) #display from url

def current_tests():
    #insert desired tests to run here - this function is passed to app.py and run all the time
    pass