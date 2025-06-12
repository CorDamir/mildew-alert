import streamlit as st


def hypothesis_page():
    st.header("Hypothesis")
    st.info(
        "Machine learning model could be implemented to replace"
        " labor-intensive and time-consuming process of powdery"
        " mildew detection on cherry plantations. This would"
        " significantly speed up detection potentially saving"
        " time as well as plantation yield due to early detection."
        )

    st.header("Validation")
    st.success(
        "1. Visual study\n"
        "* average, variability and difference image inspection reveals"
        " subtle but significant differences between categories\n"
        "* manual inspection is extremely effective, differences are"
        " mostly obvious\n"
        "2. Model evaluation\n"
        "* trained model shows 100% accuracy on training and validation sets"
        " of data as well as 99.88% accuracy on unseen test set"
    )

    st.header("Conclusion")
    st.success(
        "* with nearly 100% preliminary performance ML model is at least as"
        " accurate as current methods of detection\n"
        "* model can accurately distinguish between mildewed and healthy"
        " leaves at a much higher speed than current methods\n"
        "* ML model is a superior way of detection on plantations and should"
        " be implemented"
    )
