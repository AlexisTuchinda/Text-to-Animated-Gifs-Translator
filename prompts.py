import re
import streamlit as st
#borrowed from ML last year
import nltk
from nltk.corpus import stopwords
#divides text into segments called "tokens" --> using word and sentence tokenizers
from nltk.tokenize import word_tokenize, sent_tokenize

nltk.download("stopwords")
nltk.download("punkt")

stops = set(stopwords.words("english"))

def make_prompts(text):
    
    #somewhat dependent on tesseract's translations, but depending on the different manuals that need to be tested on this code, this splicing might need to be changed. 
    prompts = re.split("[.!?]", str(text)) #the only problem by parsing with commas is in case ingredient listings are separated by commas, e.g. "butter, flour, and egg"

    #removing empty captions
    for prompt in prompts:
        #st.write(prompt)
        if len(prompt) <1:
            prompts.remove(prompt)

    selected = ranking(str(text), prompts, 0.8)
    #st.write(selected)

    return selected

# rendition of extractive summarization
def ranking(text, prompts, limit, freqTable = None):
    if not freqTable: 
        freqTable = getFreq(text)
    
    prompts_rank = dict()

    for prompt in prompts:
        for word, freq in freqTable.items():
            if word in prompt.lower():
                if prompt in prompts_rank:
                    prompts_rank[prompt]+=freq
                else:
                    prompts_rank[prompt]=freq

    #get average score for overall text to act as threshold for prioritizing text
    sumAv = 0
    for val in prompts_rank.values():
        sumAv += val
    average = sumAv/len(prompts)

    relevant = []

    for prompt in prompts: 
        if (prompt in prompts_rank) and (prompts_rank[prompt] > (limit*average)):
            relevant.append(prompt)
    
    return relevant
    

def getFreq(text):
    words = word_tokenize(text)
    punctuation = ".!?,"
    
    #get word frequency
    freqTable = dict()
    for word in words: #parses words
        #remove stops
        if word.lower() in stops or word.lower() in punctuation: 
            continue
        elif word.lower() in freqTable:
            freqTable[word.lower()]+=1
        else:
            freqTable[word.lower()] = 1
    
    return freqTable

  