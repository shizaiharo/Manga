import os, tensorflow
from keras.models import load_model
from PIL import Image, ImageOps
import numpy as np

MainPath = os.path.dirname(os.path.abspath(__file__)).replace("\\", "/")
np.set_printoptions(suppress=True)
model = tensorflow.keras.models.load_model(MainPath + "/keras_model.h5", compile=False)
class_names = open(MainPath + "/labels.txt", "r").readlines()
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
size = (224, 224)


def check_img_for_word(image_path):
  # print(image_path.replace("/", "\\"))
  image = Image.open(image_path).convert("RGB")
  image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)
  image_array = np.asarray(image)
  normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1
  data[0] = normalized_image_array
  prediction = model.predict(data)
  return round(prediction[0][0], 1)