import streamlit as st
import os
from PIL import Image
import random


WORKING_DIR = os.getcwd()
DATASET_DIR = WORKING_DIR + "/inputs/dataset/cherry-leaves/validation"
HEALTHY_DIR = DATASET_DIR + "/healthy"
MILDEW_DIR = DATASET_DIR + "/powdery_mildew"


def set_images_for_montage(montage_type):
    """
    gets 10 random images from healthy/powdery_mildew dataset
    or 5v5 combination depending on passed string
    and stores them as a list in session_state["loaded_images"]
    """
    if montage_type == "Comparison":
        healthy_images = random.sample(
            [
                HEALTHY_DIR + "/" + img_path
                for img_path in os.listdir(HEALTHY_DIR)
            ], 5)

        mildew_images = random.sample(
            [
                MILDEW_DIR + "/" + img_path
                for img_path in os.listdir(MILDEW_DIR)
            ], 5)

        all_images = []
        for alter, nate in zip(healthy_images, mildew_images):
            all_images.append(alter)
            all_images.append(nate)

    else:
        chosen_dir = HEALTHY_DIR if montage_type == "Healthy" else MILDEW_DIR

        all_images = random.sample(
            [
                chosen_dir + "/" + img_path
                for img_path in os.listdir(chosen_dir)
            ], 10)

    st.session_state["loaded_images"] = [Image.open(img) for img in all_images]


def display_montage(loaded_images):
    """
    displays list of 10 passed images in 5 rows and 2 columns
    """
    for row in range(5):
        cols = st.columns(2)

        for col in range(2):
            index = row * 2 + col
            with cols[col]:
                st.image(
                    loaded_images[index],
                    use_container_width=True
                    )
