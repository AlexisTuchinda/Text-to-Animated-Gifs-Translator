import openai

openai.api_key = '[insert api key (ofc i wont give you mine)]'

def gen_images(prompt):
    response = openai.Image.create(
        prompt=prompt,
        n=1, # increase for more sample images
        size="1024x1024" # increase for higher resolution
    )
    image_url = response['data'][0]['url']

    return [image_url]
