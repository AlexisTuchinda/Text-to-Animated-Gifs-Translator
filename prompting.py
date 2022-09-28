import spacy 

rec = spacy.load("en_core_web_sm")  

def get_prompts(tokens, current = None, prompts = [], i = 0):
    #recursive function to generate prompts
  
    if i > len(tokens)-1:
        return prompts

    if tokens[i].pos_ == "VERB":
        if current: 
            prompts.append(current)
        prompts.append(str(tokens[i]))
        current = ""
    else:
        current+=str(tokens[i])+" "

    return get_prompts(tokens, current, prompts, i+1)

def process(text):
    tokens = rec(text)
    filter = ["AUX", "CONJ", "CCONJ", "DET", "INTJ", "PART", "PRON", "PUNCT", "SCONJ", "SYM", "X"] #which tags not to process: https://machinelearningknowledge.ai/tutorial-on-spacy-part-of-speech-pos-tagging/ 
    new = []
    for token in tokens:
        if token.pos_ not in filter:
            new.append(token)

    return get_prompts(new)