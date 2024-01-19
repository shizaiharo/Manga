import os, sys
import PIL.Image
from Translate_def import translate_text
from manga_ocr import MangaOcr

MainPath = os.path.dirname(os.path.abspath(__file__)).replace("\\", "/")

def Manga(image_path):
    for image in image_path:
        try:
            sys.stdout = open(os.devnull, 'w') #turn off the output from MangaOCR
            mocr = MangaOcr()
            img = PIL.Image.open(MainPath + "/temp/" + image) #input combine image path here
            text = mocr(img)
            # f = open(MainPath + "/temp/" + image, 'w')
            # f.write(translate_text(text, "ja"))
            # f.close()
            sys.stdout = sys.__stdout__
            print(translate_text(text, "zh-TW"))
            return translate_text(text, "zh-TW")
        except: return False
    # print(text) #output text
