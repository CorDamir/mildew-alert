import streamlit as st
from src.ML_model_functionality import MildewAlerter, run_analysis
import pandas as pd
import io
from datetime import datetime


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

    # initial conditions for buttons
    generate_table_button = False
    if "analysis_done" not in st.session_state:
        st.session_state.analysis_done = False
    if "table_ready" not in st.session_state:
        st.session_state.table_ready = False
    if "analysis_results" not in st.session_state:
        st.session_state.analysis_results = []
    if "dl_done" not in st.session_state:
        st.session_state.dl_done = False

    # if any files in uploader
    if uploader_images:
        col_btn_1, col_btn_2, col_btn_3 = st.columns([1, 1, 1])

        with col_btn_1:
            # if run analysis button pressed
            if st.button("Run analysis!"):
                if model is None:
                    model = MildewAlerter("v1")
                st.session_state.analysis_results = run_analysis(
                                                    model, uploader_images
                                                    )
                st.session_state.analysis_done = True
                st.session_state.table_ready = False
                st.session_state.dl_done = False

        with col_btn_2:
            if st.session_state.analysis_done:
                generate_table_button = st.button("Generate report table")

        # if generate table button pressed
        if generate_table_button:
            st.session_state.table_data = generate_table_data(
                                            st.session_state.analysis_results
                                            )
            st.session_state.table_ready = True
            st.table(st.session_state.table_data)

        # display analysis results
        elif st.session_state.analysis_done:
            for img, text in st.session_state.analysis_results:
                col_img, col_text = st.columns([1, 2])
                with col_img:
                    st.divider()
                    st.image(img, width=150)
                with col_text:
                    st.divider()
                    st.write(text)

        with col_btn_3:
            if st.session_state.analysis_done and st.session_state.table_ready:
                get_download_button(
                    st.session_state.table_data,
                    st.session_state.dl_done
                    )
                st.session_state.dl_done = True


def generate_table_data(results):
    table_data = []

    for img, text in results:
        img_name = img.name
        pred = "Healthy" if "healthy" in text else "Powdery mildew"
        table_data.append({"Image name": img_name, "Prediction": pred})

    return pd.DataFrame(table_data)


def get_download_button(df, used):
    temp_ram_storage = io.StringIO()
    df.to_csv(temp_ram_storage, index=False)
    csv_data = temp_ram_storage.getvalue().encode("utf-8")
    now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    file_name = f"mildew_report_{now}.csv"

    return st.download_button(
        label="Download table data (CSV)",
        data=csv_data,
        file_name=file_name,
        mime="text/csv",
        disabled=used
        )
