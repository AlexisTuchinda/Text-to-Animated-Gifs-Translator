import spacy 

rec = spacy.load("en_core_web_sm")  

def get_prompts(tokens):
    prompts = []
    current = None
    for token in tokens:
        if token.pos_ == "VERB":
            if current:
                prompts.append(current)
            current=str(token)
        elif token.pos_ == "PUNCT":
            if current:
                prompts.append(current)
                current = None
        else:
            if current: 
                current += " "+str(token)
    return prompts            

def process(text):

    tokens = rec(text.rstrip()) #remove format?
    filter = ["ADJ", "AUX", "CONJ", "CCONJ", "DET", "INTJ", "PART", "PRON", "SCONJ", "SYM", "X"] #which tags not to process: https://machinelearningknowledge.ai/tutorial-on-spacy-part-of-speech-pos-tagging/ 
    new = []
    for token in tokens:
        if token.pos_ not in filter:
            new.append(token)

    return get_prompts(new)