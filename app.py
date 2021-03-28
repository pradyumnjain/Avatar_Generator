import streamlit as st
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy as np
import pandas as pd
from PIL import Image
import sys
import os
from io import BytesIO
from cartoonize import cartoon
import network 
import guided_filter 
import base64
from seg import DeepLabModel
from seg import run_visualization
import cv2

# download function
def get_image_download_link(img):
	"""Generates a link allowing the PIL image to be downloaded
	in:  PIL image
	out: href string
	"""
	buffered = BytesIO()
	img.save(buffered, format="png")
	img_str = base64.b64encode(buffered.getvalue()).decode()
	href = f'<a href="data:file/png;base64,{img_str}">Download</a>'
	return href

# background
st.markdown(
    """
    <style>
    .reportview-container {
        background-color: #df73ff
    }
   .sidebar .sidebar-content {
        background-color: #00FFFF
    }
    </style>
    """,
    unsafe_allow_html=True
)

# title class
st.markdown("""
<style>
.big-title {
    font-size:100px !important;
    color:#710193;
}
</style>
""", unsafe_allow_html=True)

# heading class
st.markdown("""
<style>
.big-font {
    font-size:50px !important;
    color:#ffffff;
}
</style>
""", unsafe_allow_html=True)

# content class
st.markdown("""
<style>
.small-font {
    font-size:25px !important;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<p class="big-title">Pixel</p>', unsafe_allow_html=True)
st.markdown('<p class="big-font">One click to transform yourself in a cartoon.</p>', unsafe_allow_html=True)

### Excluding Imports ###
st.title("Upload a photo to transform :-) ")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg","jpeg","png"])
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.markdown("<h1 style='text-align: center; color: white;'>Original Image</h1>", unsafe_allow_html=True)
    st.image(image, caption='Uploaded Image.', use_column_width=True)
    st.write("")
    # st.markdown("<h1 style='text-align: center; color:#710193;'>processing...</h1>", unsafe_allow_html=True)

    # background removal
    modelType = "xception_model"
    MODEL = DeepLabModel(modelType)
    st.markdown("<h1 style='text-align: center; color: white;'>Background Removal</h1>", unsafe_allow_html=True)
    with st.spinner('Removing background ...'):
        bg_image = run_visualization(image, MODEL)
    st.success('Done!')
    st.image(bg_image, caption='background removed image.', use_column_width=True)
    st.markdown(get_image_download_link(bg_image), unsafe_allow_html=True)

    # st.balloons()
    # cartoon creation
    model_path = 'test_code/saved_models'
    final_img= cartoon(model_path,bg_image)
    final_img = cv2.cvtColor(final_img, cv2.COLOR_BGR2RGB)
    st.image(final_img, caption='cartoonified image.', use_column_width=True)

    





