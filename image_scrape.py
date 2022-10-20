#from https://serpapi.com/blog/scrape-google-images-with-python/

from bs4 import BeautifulSoup
import requests
import re, json

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36"
}

def grab_soup(prompt): #have to pass in that I want the image scraped to be a gif
    
    params = {
        "q": prompt+" gif", # search query
        "tbm": "isch",                # image results
        "hl": "en",                   # language of the search
        "gl": "us",                   # country where search comes from
        "ijn": "0"                    # page number
    }

    html = requests.get("https://www.google.com/search", params=params, headers=headers, timeout=30)
    soup = BeautifulSoup(html.content, "html.parser")

    return soup

def get_original_images(prompt):

    soup = grab_soup(prompt)
    google_images = []

    #print ("script tags")
    all_script_tags = soup.select("script")
   # print (all_script_tags)
    
    #filter through script tages for google javascript callback that contains the original images
    matched_images_data = "".join(re.findall(r"AF_initDataCallback\(([^<]+)\);", str(all_script_tags)))
    
    #interpret the matched_images_data with json
    matched_images_data_fix = json.dumps(matched_images_data)
    matched_images_data_json = json.loads(matched_images_data_fix)

    #print (matched_images_data_json)
        
    # the matched_images_data_json is a bunch of elements in a list following the format described in the regex... this I suppose filters these out. 
    #sometimes this is a bit weird (like it doesn't work), so you have to replace from source above sometimes
    matched_google_image_data = re.findall(r'\"b-GRID_STATE0\"(.*)sideChannel:\s?{}}', matched_images_data_json)
    #print (matched_google_image_data)

    # thumbnails? (like on youtube videos, but for google search photos?)
    matched_google_images_thumbnails = ", ".join(
        re.findall(r'\[\"(https\:\/\/encrypted-tbn0\.gstatic\.com\/images\?.*?)\",\d+,\d+\]',
                   str(matched_google_image_data))).split(", ")

    thumbnails = [
        bytes(bytes(thumbnail, "ascii").decode("unicode-escape"), "ascii").decode("unicode-escape") for thumbnail in matched_google_images_thumbnails
    ]

    #print (thumbnails)

    # removing previously matched thumbnails for easier full resolution image matches.
    removed_matched_google_images_thumbnails = re.sub(
        r'\[\"(https\:\/\/encrypted-tbn0\.gstatic\.com\/images\?.*?)\",\d+,\d+\]', "", str(matched_google_image_data))
    
    matched_google_full_resolution_images = re.findall(r"(?:'|,),\[\"(https:|http.*?)\",\d+,\d+\]", removed_matched_google_images_thumbnails)

    #print (matched_google_full_resolution_images)

    full_res_images = [
        bytes(bytes(img, "ascii").decode("unicode-escape"), "ascii").decode("unicode-escape") for img in matched_google_full_resolution_images
    ]
        
    #creating list of elements with following attributes for indexing
    for index, (metadata, thumbnail, original) in enumerate(zip(soup.select(".isv-r.PNCib.MSM1fd.BUooTd"), thumbnails, full_res_images), start=1):
        google_images.append({
            "title": metadata.select_one(".VFACy.kGQAp.sMi44c.lNHeqe.WGvvNb")["title"],
            "link": metadata.select_one(".VFACy.kGQAp.sMi44c.lNHeqe.WGvvNb")["href"],
            "source": metadata.select_one(".fxgdke").text,
            "thumbnail": thumbnail,
            "original": original
        })

    #print (google_images)
    
    return google_images #return the entire list of all of the element attributes in case it needs to be used later? 

def images_to_use(n, images):
    use = []
    if len(images)>=n:
        for i in range(n):
            use.append(images[i]["original"]) #hence why we have to specify the "original" source here
    else:
        for image in images:
            use.append(image["original"])
    return use

def load_images(n, prompt):
    
    current_search = get_original_images(prompt)
    selected_images = images_to_use(n, current_search)
    return selected_images