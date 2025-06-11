import streamlit as st
from src.ML_model_functionality import MildewAlerter, run_analysis


def mildew_alerter_page():
    model = None

    st.header("Mildew alerter - AI powered classifier")
    st.divider()

    st.info(
        "Functionality on this page satisfies our second business requirement"
        " - machine model quickly and accurately distinguishes healthy and"
        " mildewed leaves."
        )
    st.divider()

    with st.expander("If needed, sample dataset for testing is available here"):
        with open("./outputs/sample_test/sample_cherry_leaves.zip", "rb") as f:
            dl_data = f.read()

        st.download_button(
            label="Download cherry leaves sample dataset",
            data=dl_data,
            file_name="sample_cherry_leaves.zip",
            mime="application/zip"
        )

    st.divider()
    st.subheader("Upload images and check for powdery mildew", divider=True)
    uploader_images = st.file_uploader(
        "Upload cherry leaf images here",
        type=["png", "jpg", "jpeg"],
        accept_multiple_files=True,
        label_visibility="collapsed"
    )

    # if any uploaded files
    if uploader_images:
        run_model_button = st.button("Run analysis!")
        # on "run analysis" button press
        if run_model_button:
            if model is None:
                model = MildewAlerter("v1")
            analysis_results = run_analysis(model, uploader_images)

            for img, text in analysis_results:
                col_img, col_text = st.columns([1, 2])
                with col_img:
                    st.divider()
                    st.image(img, width=150)
                with col_text:
                    st.divider()
                    st.write(text)
