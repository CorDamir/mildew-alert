import streamlit as st
import os
from PIL import Image
import random


WORKING_DIR = os.getcwd()
DATASET_DIR = WORKING_DIR + "/inputs/dataset/cherry-leaves/validation"
HEALTHY_DIR = DATASET_DIR + "/healthy"
MILDEW_DIR = DATASET_DIR + "/powdery_mildew"


def display_montage(montage_type):
    """
    gets 10 random images from healthy/powdery_mildew dataset
    or 5v5 combination depending on passed string
    and stores them as a list in session_state["loaded_images"]
    """
    if montage_type == "Healthy":
        all_images = [
            HEALTHY_DIR + "/" + img_path
            for img_path in os.listdir(HEALTHY_DIR)
        ]

        st.session_state["loaded_images"] = [
            Image.open(img)
            for img in random.sample(all_images, 10)
            ]

    elif montage_type == "Mildewed":
        st.write(MILDEW_DIR)

    else:
        st.write("combine")