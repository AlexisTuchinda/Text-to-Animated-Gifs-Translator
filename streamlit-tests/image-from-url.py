#testing to see if it is possible to display an image from url on streamlit (instead of having to download the image locally)

import streamlit as st

def display_images(images):
    for url in images: 
        st.markdown("![Image]("+url+")") #successful in displaying from url