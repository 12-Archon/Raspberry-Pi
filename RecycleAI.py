from tensorflow import keras
from tensorflow.keras.models import load_model
from PIL import Image, ImageOps
import numpy as np
import os

dir_path='/home/pi/Desktop/SRS-IOT/'

def getRecycleClassification(name):

    np.set_printoptions(suppress=True)

    model = load_model('/home/pi/Desktop/SRS-IOT/RecycleAI/keras_model.h5', compile=False)

    class_names = open('/home/pi/Desktop/SRS-IOT/RecycleAI/labels.txt', 'r').readlines()

    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

    image = Image.open(dir_path + name).convert('RGB')
    

    size = (224, 224)
    image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)

    image_array = np.asarray(image)

    normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1

    data[0] = normalized_image_array

    prediction = model.predict(data)
    index = np.argmax(prediction)
    class_name = class_names[index]
    confidence_score = prediction[0][index]
    RecycleResult = class_name.split()[1]

    if RecycleResult == '플라스틱':
        RecycleResult='Plastic'
    elif RecycleResult == '캔' :
        RecycleResult='Can'
    elif RecycleResult == '유리병':
        RecycleResult = 'Glass Bottle'
    else:
        RecycleResult = 'None'

    return RecycleResult
