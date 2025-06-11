import streamlit as st


def project_summary_page():
    st.title("Project: Mildew Alert!")
    st.divider()
    st.write("## Project summary")
    st.subheader("Context information", divider=True)

    st.info(
        "**WHAT IS :violet[POWDERY MILDEW]?**\n"
        "* :violet[Fungal disease] that affects many types of plants,"
        " including cherry trees\n"
        "* Appears as :violet[white or gray powdery spots] on leaves, stems,"
        " and fruit\n"
        "* Thrives in :violet[warm, dry climates with high humidity]\n"
        "* Infected leaves may become :violet[distorted, yellow, or fall"
        " prematurely]\n"
        "* Can lead to :violet[reduced photosynthesis, stunted growth,"
        " and lower yield]\n"
        "* :violet[Early detection] is key to :violet[preventing spread"
        " and minimizing damage]\n\n"
        "**BUSINESS MOTIVATION**\n"
        "* Multiple cherry plantations are experiencing widespread"
        " leaf infections\n"
        "* Manual inspection is time-consuming and labor-intensive\n"
        "* Delays in detection lead to increased crop loss and reduced yield\n"
        "* Client seeks a fast, reliable method to identify infected leaves"
        " at scale\n"
        "* An AI-powered solution can support early intervention and"
        " reduce costs"
        )

    st.subheader("Dataset information", divider=True)
    st.info(
        "* The dataset is sourced from [Kaggle]"
        "(https://www.kaggle.com/codeinstitute/cherry-leaves)\n"
        "* The dataset contains 4208 images; 2104 of healthy cherry"
        " leaves and 2104 of cherry leaves"
        " with powdery mildew, taken from the client's crop fields\n"
        "* All images are 200 by 200 pixels in dimension, RGB .jpg format\n"
        "* The dataset doesn't require cleaning"
    )

    st.subheader("Business requirements", divider=True)
    st.info(
        "* 1 - The client is interested in conducting a study to visually"
        " differentiate a healthy cherry leaf from one with powdery mildew\n"
        "* 2 - The client is interested in predicting if a cherry leaf is"
        " healthy or contains powdery mildew"
    )

    st.subheader("Additional information", divider=True)
    st.info(
        "For extensive information please refer to [README file]"
        "(https://github.com/CorDamir/mildew-alert/blob/main/README.md)"
    )
