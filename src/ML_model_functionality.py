from keras.models import load_model
import os
import numpy as np
from keras.preprocessing import image
import pandas as pd


class MildewAlerter():
    """
    self.results[] contains image paths and text
    interpretation of analysis if analysis was done

    self.run_analysis() accepts list-like collection of
    image paths, stores analysis in self.results[]

    self.results_to_dataframe() returns pandas dataframe
    with image names and respective analysis results
    """
    def __init__(self, version):
        save_dir = os.getcwd() + "/outputs/model"
        self.best_model = load_model(
            f"{save_dir}/powdery_mildew_alerter_{version}.keras")
        self.results = []

    def prediction_for_image(self, img_path):
        img = MildewAlerter.load_resize_image_as_array(img_path, 75, 75)
        img = np.expand_dims(img, axis=0)
        return np.round(self.best_model.predict(img) * 100, 2)[0][0]

    def prediction_to_text(self, img_path):
        result = self.prediction_for_image(img_path)

        text_for_display = "Leaf in this image "

        if result > 50:
            text_for_display += "contains powdery mildew"
        else:
            text_for_display += "is healthy"
            result = 100-result

        result_formatted = f"{result:.2f}".rstrip('0').rstrip('.')
        return text_for_display + f". Model is {result_formatted}% confident."

    def run_analysis(self, images):
        self.results = []
        for img in images:
            self.results.append((img, self.prediction_to_text(img)))

    def results_to_dataframe(self):
        table_data = []

        for img, text in self.results:
            pred = "Healthy" if "healthy" in text else "Powdery mildew"
            table_data.append({"Image name": img.name, "Prediction": pred})

        return pd.DataFrame(table_data)

    @staticmethod
    def load_resize_image_as_array(img_path, width, height):
        img = image.load_img(img_path, target_size=(width, height))
        return image.img_to_array(img) / 255
