#drafting space

def transform(image):
    #check out tesseract documnetation for ways to image- pre-processing or the image_to_text: https://pypi.org/project/pytesseract/
    results = pytesseract.image_to_data(np.array(image), output_type=pytesseract.Output.DICT)

    max_index = 0 #by width and confidence
    for i in range(len(results["text"])):
        print (i, results["width"][i], results["conf"][i])
        #down here is a bad conditional... rewrite to prioritize both width and confidence... or reorder list by confidence and then find the biggest width from that!
        if results["width"][i] > results["width"][max_index] or results["conf"][i] > results["conf"][max_index]:
            max_index = i

    #print ("index", max_index)

    #find difference between the found max and the size of the current image.
    new_width, new_height = results["width"][max_index], results["height"][max_index]
    current_width, current_height = image.size
    change_in_width, change_in_height = current_width/new_width, current_height/new_height #returns percentage of max_index width/height that current is...

    #print (results["left"][max_index], results["top"][max_index], new_width, new_height)  
    im1 = image.crop((results["left"][max_index], results["top"][max_index], results["left"][max_index]+new_width, results["top"][max_index]+new_height))

    st.image(im1)

    im1_width, im1_height = im1.size
    #print (im1_width, im1_height, im1.size)

    im2 = cv2.resize(np.array(im1), (int(im1_width)*int(change_in_width), int(im1_height)*int(change_in_height)))

    st.image(im2)
    
    return im2