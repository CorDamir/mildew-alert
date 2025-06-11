import streamlit as st
from src.image_montage_functionality import (
    set_images_for_montage, display_montage
)


def data_study_page():
    # Set radio key on page load to avoid errors
    if "montage_radio" not in st.session_state:
        st.session_state["montage_radio"] = None

    # Set image loading into session state to avoid
    # rendering them before radio buttons
    if "loaded_images" not in st.session_state:
        st.session_state["loaded_images"] = []

    # Set appropriate header-like style for expander elements
    st.markdown(
        """
        <style>
            .st-emotion-cache-qoz3f2 p{
                font-size: 1.65rem;
                font-weight: bold;
                color: #6285ed;
            }
        </style>
        """,
        unsafe_allow_html=True
        )

    images_dir = "./outputs/images"

    st.header("Data study")
    st.divider()

    st.info(
        "Data study was done to satisfy business requirement 1"
        " - to visually distinguish healthy and mildewed leaves. "
        "Study logic and conclusions are organized in sections below. "
        "For better view of images please use fullscreen option"
    )
    st.divider()

    with st.expander("Healthy leaves"):
        st.write(
            "Inspecting average and variability image"
            " from healthy leaves dataset"
        )
        st.image(images_dir + "/avg_varia_healthy.png")

        st.subheader("Interpretation")
        st.write(
            "* healthy leaves have a consistent green color\n"
            "* healthy leaves have virtually no variance at the"
            " large central area\n"
            "* healthy leaves have small variance on the edges"
        )

        st.subheader("Conclusions")
        st.write(
            "* healthy leaves don't have significant differences"
            " except near the edges which is explained"
            " by difference in shapes"
        )

    with st.expander("Mildewed leaves"):
        st.write(
            "Inspecting average and variability image"
            " from mildewed leaves dataset"
            )
        st.image(images_dir + "/avg_varia_powdery_mildew.png")

        st.subheader("Interpretation")
        st.write(
            "* mildewed leaves have a noticeably brighter shade of"
            " green compared to healthy leaves\n"
            "* mildewed leaves have a significantly larger variance"
            " at the large central area compared to healthy leaves\n"
            "* mildewed leaves are similar in variance at the very edges"
            " to healthy leaves"
        )

        st.subheader("Conclusions")
        st.write(
            "* near the edges healthy and mildewed leaves are"
            " virtually indistinguishable\n"
            "* mildewed leaves have a brighter surface due to"
            " whitish powder from infection\n"
            "* mildewed leaves have a higher variance on the"
            " surface due inconsistent positioning of mentioned"
            " white powder"
        )

    with st.expander("Averages difference"):
        st.write(
            "Inspect difference image between averages of healthy"
            " and mildewed leaves"
        )
        st.image(images_dir + "/difference_image.png")

        st.subheader("Interpretation")
        st.write(
            "* average healthy leaves differ from average infected"
            " leaf only slightly at the very edges of the leaf\n"
            "* average healthy leaves moderately differ from average"
            " infected leaves on parts around halfway between"
            " centerline and edge"
        )

        st.subheader("Conclusion")
        st.write(
            "* difference near the edges of leaves is explained by leaf shape"
            " and therefore insignificant for required distinction\n"
            "* differences in shade and patterns on leaf surface result from"
            " whitish powder specific to mildew infection and can be used for"
            " distinction"
        )

    with st.expander("Manual inspection"):
        st.info(
            "With manual inspection of leaves we can clearly distinguish"
            " which are infected. Combined with knowledge that average"
            " images moderately differ we can be optimistic that machine"
            " learning model will also be succesfull."
        )

        st.subheader("Image montages", divider=True)

        st.radio(
            "Select montage type",
            label_visibility="collapsed",
            options=["Healthy", "Mildewed", "Comparison"],
            key="montage_radio",
            on_change=set_images_for_montage(st.session_state["montage_radio"])
        )

        # loaded images are in session_state from st.radio's "on_change" call
        loaded_images = st.session_state["loaded_images"]

        if loaded_images:
            display_montage(loaded_images)
