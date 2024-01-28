import os, shutil, requests
# from Pytesseract import tes
from PIL import Image, ImageFile
from ImageQuadtree import Quadtree
from ImageCombine_def import combine
from werkzeug.utils import secure_filename
from flask import Flask, url_for, request, redirect, render_template

app = Flask(__name__)
ImageFile.LOAD_TRUNCATED_IMAGES = True
# upload_path = "upload"
MainPath = os.path.dirname(os.path.abspath(__file__)).replace("\\", "/")
print(MainPath)
temp_path = MainPath +"/temp"
app.secret_key = "s1e2a3n4"
app.config['UPLOAD_FOLDER'] = MainPath + '/static/upload'  # Folder to store uploaded images
# def gn(x):
#     match = re.search(r'_(\d+)\(', x)
#     if match:
#         return int(match.group(1))
#     else:
#         return float('inf')
        
@app.route('/')
def index():
    try:
        request.headers['ngrok-skip-browser-warning'] = '696969'
        return render_template('index.html')
    except Exception as e:
        return str(e), 500

@app.route('/upload', methods=['POST'])
def upload():
    folder = request.files.getlist('image_folder')  # Get the uploaded files
    
    # # Create a directory to store the uploaded images
    # if not os.path.exists(app.config['UPLOAD_FOLDER']):
    #     os.makedirs(app.config['UPLOAD_FOLDER'])
    # if not os.path.exists(temp_path):
    #     os.makedirs(temp_path)
    
    
    # Save the uploaded images to the server
    for file in folder:
        filename = secure_filename(file.filename)
        # image = Image.open(filename)
        # return render_template('myconsole.html', info=filename)
        # image = image.convert("RGB")
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

    return redirect(url_for('processed_images'))


# @app.route('/processed_images')
# def processed_images():
#     # Get the list of processed images in the 'uploads' folder
#     original_images_path = os.listdir(app.config['UPLOAD_FOLDER'])
#     txt = 0
#     for image_name in original_images_path:
#         txt += 1
#         image_quadtree = Quadtree()
#         image_path = os.path.join(app.config['UPLOAD_FOLDER'], image_name)
#         image = Image.open(image_path)
    
#         image_quadtree.check_img(MainPath + "/temp/"+image_name.split('.')[0]+"_0",image)
#         words_images_path = image_quadtree.get_images()
#         #words_images_path = sorted(words_images_path, key=lambda x: gn(x))
#         # tes(combine(words_images_path))
#         combine(words_images_path)
#         for words_image_path in words_images_path:
#             word_image = Image.open(MainPath + "/temp/"+words_image_path)
#             filename = words_image_path
#             word_image.save(app.config['UPLOAD_FOLDER'] + "/" + filename)

        
#         #     # os.remove("temp/"+words_image_path) 
#         # txt += image_quadtree.content
            
#     # return render_template('myconsole.html', info=txt)
#     return render_template('processed_images.html', OGimages=original_images_path)
@app.route('/processed_images')
def processed_images():
    # Get the list of processed images in the 'uploads' folder
    original_images_path = os.listdir(app.config['UPLOAD_FOLDER'])
    txt = 0
    for image_name in original_images_path:
        txt += 1
        image_quadtree = Quadtree()
        image_path = os.path.join(app.config['UPLOAD_FOLDER'], image_name)
        image = Image.open(image_path)
    
        image_quadtree.check_img(MainPath + "/temp/"+image_name.split('.')[0]+"_0",image)
        words_images_path = image_quadtree.get_images()
        combine(words_images_path)
        for words_image_path in words_images_path:
            word_image = Image.open(MainPath + "/temp/"+words_image_path)
            filename = words_image_path
            word_image.save(MainPath + "/temp/" + filename)  # Save only to the temp folder

    return render_template('processed_images.html', OGimages=original_images_path)

@app.route('/clear_and_back', methods=['POST'])
def clear_and_back():
    # Remove uploaded images from static/upload folder
    upload_folder_path = app.config['UPLOAD_FOLDER']
    for filename in os.listdir(upload_folder_path):
        file_path = os.path.join(upload_folder_path, filename)
        if os.path.isfile(file_path):
            os.remove(file_path)

    # Remove processed images from temp folder
    temp_folder_path = MainPath + "/temp"
    for filename in os.listdir(temp_folder_path):
        file_path = os.path.join(temp_folder_path, filename)
        if os.path.isfile(file_path):
            os.remove(file_path)

    # Redirect back to the image processing page
    return render_template('index.html')

if __name__ == '__main__': 
    if MainPath[0].isalpha() and MainPath[1] == ":": os.system("cls") # Windows localhost
    if os.path.exists(app.config['UPLOAD_FOLDER']):
        shutil.rmtree(app.config['UPLOAD_FOLDER'])
    os.makedirs(app.config['UPLOAD_FOLDER'])
    if os.path.exists(temp_path):
        shutil.rmtree(temp_path)
    os.makedirs(temp_path) 

    app.run(host="0.0.0.0", port=6969)