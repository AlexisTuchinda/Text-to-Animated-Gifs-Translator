import re
import streamlit as st

def make_prompts(text):
    
    #somewhat dependent on tesseract's translations, but depending on the different manuals that need to be tested on this code, this splicing might need to be changed. 
    prompts = re.split("[,:.!?]", str(text)) #the only problem by parsing with commas is in case ingredient listings are separated by commas, e.g. "butter, flour, and egg"

    return prompts