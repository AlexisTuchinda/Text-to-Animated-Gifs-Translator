import openai

openai.api_key = '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'

def gen_images(prompt):
    response = openai.Image.create(
        prompt=prompt,
        n=1,
        size="1024x1024"
    )
    image_url = response['data'][0]['url']

    return [image_url]
