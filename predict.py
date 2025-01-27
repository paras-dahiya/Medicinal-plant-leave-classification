import numpy as np
import tensorflow as tf
from tensorflow import keras
from keras.models import load_model
from keras_preprocessing import image

class maskdetection:
    def __init__(self, filename):
        self.filename = filename

    def predictionmask(self):
        try:
            #load model
            model = load_model('mymodel.h5')

            imagename = self.filename
            test_image = image.load_img(imagename, target_size = (256,256))
            test_image = image.img_to_array(test_image)
            test_image = np.expand_dims(test_image,axis = 0)
            result = model.predict(test_image)

            if result[0][0] == 1:
                prediction = 'arjun'
                return [{"image": prediction}]
            elif result[0][1] == 1:
                prediction = 'curry'
                return [{"image": prediction}]
            elif result[0][2] == 1:
                prediction = 'marsh pennywort'
                return [{"image": prediction}]
            elif result[0][3] == 1:
                prediction = 'mint'
                return [{"image": prediction}]
            elif result[0][4] == 1:
                prediction = 'neem'
                return [{"image": prediction}]
            else:
                prediction = 'rubble'
                return [{"image": prediction}]

        except Exception as ex:
            raise ex

