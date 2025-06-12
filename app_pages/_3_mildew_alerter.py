import streamlit as st
from streamlit import session_state as sesh
from src.ML_model_functionality import MildewAlerter
import io
from datetime import datetime


def mildew_alerter_page():
    st.header("Mildew alerter - AI powered classifier")

    st.info(
        "Functionality on this page satisfies our second business requirement"
        " - machine model quickly and accurately distinguishes healthy and"
        " mildewed leaves."
        )

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
    st.error(
        "Adding, removing or changing uploaded files is considered a change of"
        " analysis set and will remove your report. Make sure to download"
        " before switching images"
        )

    st.subheader("Upload images and check for powdery mildew", divider=True)
    uploaded_imgs = st.file_uploader(
        "Upload cherry leaf images here",
        type=["png", "jpg", "jpeg"],
        accept_multiple_files=True,
        label_visibility="collapsed"
    )

    # initial session conditions
    if "model" not in sesh:
        sesh.model = None
    if "analysis_done" not in sesh:
        sesh.analysis_done = False
    if "table_ready" not in sesh:
        sesh.table_ready = False
    if "dl_button_used" not in sesh:
        sesh.dl_button_used = True
    if "uploaded_files" not in sesh:
        sesh.uploaded_files = None

    # on uploaded set change
    if not sesh.uploaded_files == uploaded_imgs:
        sesh.analysis_done = False
        sesh.table_ready = False

    col_btn_1, col_btn_2, col_btn_3 = st.columns([1, 1, 1])
    with col_btn_1:
        st.button(
            "Run analysis!",
            on_click=lambda: run_analysis(uploaded_imgs),
            disabled=not uploaded_imgs or sesh.analysis_done
            )

    with col_btn_2:
        st.button(
            "Generate report table",
            on_click=generate_report,
            disabled=not sesh.analysis_done or sesh.table_ready
                  )

    with col_btn_3:
        if sesh.analysis_done and sesh.table_ready:
            get_download_button(sesh.table_data, sesh.dl_button_used)
            sesh.dl_button_used = True

    if sesh.table_ready:
        st.divider()
        st.table(sesh.table_data)

    elif sesh.analysis_done:
        for img, text in sesh.model.results:
            col_img, col_text = st.columns([1, 2])
            with col_img:
                st.divider()
                st.image(img, width=150)
            with col_text:
                st.divider()
                st.write(text)


def run_analysis(uploaded_imgs):
    if sesh.model is None: 
        sesh.model = MildewAlerter("v1")
    sesh.uploaded_files = uploaded_imgs
    sesh.model.run_analysis(sesh.uploaded_files)
    sesh.analysis_done = True
    sesh.table_ready = False
    sesh.dl_button_used = False


def generate_report():
    sesh.table_data = sesh.model.results_to_dataframe()
    sesh.table_ready = True


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
