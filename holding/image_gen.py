import openai

#remember to remove API key when pushing!
openai.api_key = 'API Key'

def gen_images(prompt):
    try:
        response = openai.Image.create(
            prompt=prompt,
            n=1, # increase for more sample images
            size="1024x1024" # increase for higher resolution
        )
        image_url = response['data'][0]['url']
    except:
        return ['https://media.tenor.com/x8v1oNUOmg4AAAAM/rickroll-roll.gif']
    
    return [image_url]
