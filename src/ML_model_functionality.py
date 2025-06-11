from keras.models import load_model
import os
import numpy as np
from keras.preprocessing import image


class MildewAlerter():
    def __init__(self, version):
        save_dir = os.getcwd() + "/outputs/model"

        self.best_model = load_model(
            f"{save_dir}/powdery_mildew_alerter_{version}.keras"
            )

    @staticmethod
    def load_resize_image_as_array(img_path, width, height):
        img = image.load_img(img_path, target_size=(width, height))
        return image.img_to_array(img) / 255

    def model_prediction_for_image(self, img_path):
        img = MildewAlerter.load_resize_image_as_array(img_path, 75, 75)
        img = np.expand_dims(img, axis=0)
        return np.round(self.best_model.predict(img) * 100, 2)[0][0]

    def model_prediction_to_text(self, img_path):
        result = self.model_prediction_for_image(img_path)

        text_for_display = "Leaf in this image "

        if result > 50:
            text_for_display += "contains powdery mildew"
        else:
            text_for_display += "is healthy"
            result = 100-result

        result_formatted = f"{result:.2f}".rstrip('0').rstrip('.')

        return text_for_display + f". Model is {result_formatted}% confident."


def run_analysis(model, images):
    result = []

    for img in images:
        result.append((
            img,
            model.model_prediction_to_text(img)
            ))

    return result
