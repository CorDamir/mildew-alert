import streamlit as st
import pandas as pd


def technical_informatio_page():
    st.header("Technical information")

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

    with st.expander("Dataset distribution"):
        st.write(
            "Dataset was split to 70% for training, 10% for validation and"
            " 20% for testing, randomized"
        )
        st.image(images_dir + "/dataset_dist.png", use_container_width=True)

    with st.expander("Model summary"):
        st.write(
            "Model design and layer specifications"
        )
        st.image(images_dir + "/model_summary.png", use_container_width=True)
        st.write(
            "* Starting point was based on logic from TensorFlow tutorial on "
            " simple convolutional networks - convolution layer followed by"
            " pooling layer, and then flatten layer before a dense layer.\n"
            "* Model retained this basic structure and evolved by additions"
            " of convolution + pooling layers." "Having two dense layers with"
            " dropout of 30-40% showed good results immediately. I've learned"
            " that the best approach was to get key features by using less"
            " filters and then increase detail of learning in next layers.\n"
            "* This is reflected in a growing number of filters in convolution"
            " layers (32 - 64 - 128) and then dense layers having 256 nodes."
        )

    with st.expander("Model fitting / training"):
        st.write(
            "Model was trained with planned maximum of 25 epochs and an early"
            " stop condition of four epochs with no improvement to loss"
            " function. It was optimized after only five epochs, triggering"
            " early stop after ninth. Best configuration was then selected."
        )

        st.subheader("Performance tracking")

        st.image(images_dir + "/accuracy_plot.png", use_container_width=True)
        st.image(images_dir + "/loss_function_plot.png",
                 use_container_width=True)

        st.write(
            "Machine learning process quickly identified key features and"
            " reached optimal performance for it's design on 5th epoch."
            " Afterwards more iterations led to drop in performance"
            " so having an early stop function was critical"
        )

    with st.expander("Model performance"):
        st.write(
            "Performance on test set exceeds requirements"
        )
        st.table(pd.read_csv(images_dir + "/../model/evaluation.csv"))
