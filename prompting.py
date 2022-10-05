import spacy 

rec = spacy.load("en_core_web_sm")  

def get_prompts(tokens, current = None, prompts = [], i = 0):
    #recursive function to generate prompts
  
    if i > len(tokens)-1:
        return prompts
    if tokens[i] is not None: 
        if tokens[i].pos_ == "VERB": #still needs to parse for adverbs
            if current: 
                prompts.append(current)
            #prompts.append(str(tokens[i]))
            current = str(tokens[i])
        else:
            if not current:
                current=""
            current += " " #spacing purposes
            current+=str(tokens[i])
    #print (current)
    return get_prompts(tokens, current, prompts, i+1)

def process(text):

    #print ("start")
    tokens = rec(text.rstrip()) #remove format?
    filter = ["ADJ", "AUX", "CONJ", "CCONJ", "DET", "INTJ", "PART", "PRON", "PUNCT", "SCONJ", "SYM", "X"] #which tags not to process: https://machinelearningknowledge.ai/tutorial-on-spacy-part-of-speech-pos-tagging/ 
    new = []
    for token in tokens:
        if token.pos_ not in filter:
            new.append(token)

    #print (new) #has \n (next line commands) - need to filter out
    return get_prompts(new)