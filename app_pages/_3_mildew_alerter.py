import streamlit as st
from streamlit import session_state as sesh
from src.ML_model_functionality import MildewAlerter, run_analysis
import pandas as pd
import io
from datetime import datetime


def mildew_alerter_page():
    st.header("Mildew alerter - AI powered classifier")
    st.divider()

    st.info(
        "Functionality on this page satisfies our second business requirement"
        " - machine model quickly and accurately distinguishes healthy and"
        " mildewed leaves."
        )
    st.divider()

    with st.expander(
        "If needed, sample dataset for testing is available here"
                    ):
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

    uploaded_imgs = st.file_uploader(
        "Upload cherry leaf images here",
        type=["png", "jpg", "jpeg"],
        accept_multiple_files=True,
        label_visibility="collapsed"
    )

    # initial session conditions
    generate_report_button = False
    if "model" not in sesh:
        sesh.model = MildewAlerter("v1")
    if "analysis_done" not in sesh:
        sesh.analysis_done = False
    if "table_ready" not in sesh:
        sesh.table_ready = False
    if "analysis_results" not in sesh:
        sesh.analysis_results = []
    if "dl_button_used" not in sesh:
        sesh.dl_button_used = False

    # if any files in uploader
    if uploaded_imgs:
        col_btn_1, col_btn_2, col_btn_3 = st.columns([1, 1, 1])

        with col_btn_1:
            # if run analysis button pressed enable dl button
            # and flag analysis done
            if st.button("Run analysis!"):
                sesh.analysis_results = run_analysis(sesh.model, uploaded_imgs)
                sesh.analysis_done = True
                sesh.table_ready = False
                sesh.dl_button_used = False

        with col_btn_2:
            # if analysis done display generate report button
            if sesh.analysis_done:
                generate_report_button = st.button("Generate report table")

        # if generate table button pressed flag: table is ready
        if generate_report_button:
            sesh.table_data = generate_table_data(sesh.analysis_results)
            sesh.table_ready = True
            st.table(sesh.table_data)

        # analysis done and generate table not pressed
        elif sesh.analysis_done:
            for img, text in sesh.analysis_results:
                col_img, col_text = st.columns([1, 2])
                with col_img:
                    st.divider()
                    st.image(img, width=150)
                with col_text:
                    st.divider()
                    st.write(text)

        with col_btn_3:
            if sesh.analysis_done and sesh.table_ready:
                get_download_button(sesh.table_data, sesh.dl_button_used)
                sesh.dl_button_used = True


def generate_table_data(results):
    table_data = []

    for img, text in results:
        pred = "Healthy" if "healthy" in text else "Powdery mildew"
        table_data.append({"Image name": img.name, "Prediction": pred})

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
