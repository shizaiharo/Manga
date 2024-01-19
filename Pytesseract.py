import os, pytesseract
from pytesseract import Output
from Translate_def import translate_text
from PIL import Image
from mangaOCR import Manga

MainPath = os.path.dirname(os.path.abspath(__file__)).replace("\\", "/")

def tes(images_path):
    for image in images_path:
        if(image.split(".")[1] == "png"):
            img = Image.open(MainPath + "/temp/" + image) #image
            text = pytesseract.image_to_string(img)
            try: 
                osd = pytesseract.image_to_osd(img, output_type=Output.DICT)
                script_orientation = osd['rotate']
                script_language = osd['script']
                print(script_language)
                if(script_language == "Latin" or script_language == "English"):
                    print(translate_text(text, "en"))
                elif(script_language == "Japanese"):
                    print(Manga(images_path))

            except: 
                if(Manga(images_path) is False): print("detection fail")


# tes("japanese.jpg")