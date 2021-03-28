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


# download function
def get_image_download_link_cartoon(img):
	"""Generates a link allowing the PIL image to be downloaded
	in:  PIL image
	out: href string
	"""
	buffered = BytesIO()
	img.save(buffered, format="JPEG")
	img_str = base64.b64encode(buffered.getvalue()).decode()
	href = f'<a href="data:file/jpg;base64,{img_str}" download="cartoon.jpg">Download result</a>'
	return href

def get_image_download_link_bg(img):
	"""Generates a link allowing the PIL image to be downloaded
	in:  PIL image
	out: href string
	"""
	buffered = BytesIO()
	img.save(buffered, format="JPEG")
	img_str = base64.b64encode(buffered.getvalue()).decode()
	href = f'<a href="data:file/jpg;base64,{img_str}" download="foreground.jpg">Download result</a>'
	return href

# background
st.markdown(
    """
    <style>
    .reportview-container {
        background-color: #df73ff
    }
    .sidebar .sidebar-content {
         background-color: #FFDF73
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

###side bar
st.sidebar.title('Upload')
st.sidebar.header("Upload a photo to transform :-) ")

### Excluding Imports ###
#st.title("Upload a photo to transform :-) ")

col1, col2 = st.beta_columns(2)

uploaded_file = st.sidebar.file_uploader("Choose an image...", type=["jpg","jpeg","png"])
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.sidebar.markdown("<h1 style='text-align: center; color: white;'>Original Image</h1>", unsafe_allow_html=True)
    st.sidebar.image(image,width=300, caption='Uploaded Image.', use_column_width=True)
    st.write("")
    # st.markdown("<h1 style='text-align: center; color:#710193;'>processing...</h1>", unsafe_allow_html=True)

    # background removal
    modelType = "xception_model"
    MODEL = DeepLabModel(modelType)
    col1.markdown("<h1 style='text-align: center; color: white;'>Background Removal</h1>", unsafe_allow_html=True)
    with st.spinner('Removing background ...'):
        bg_image = run_visualization(image, MODEL)
    st.success('Done!')
    col1.image(bg_image, caption='background removed image.', use_column_width=True)
    # download image
    col1.markdown(get_image_download_link_bg(bg_image), unsafe_allow_html=True)

    # cartoon creation
    model_path = 'test_code/saved_models'
    col2.markdown("<h1 style='text-align: center; color: white;'>Image Cartooning</h1>", unsafe_allow_html=True)
    col2.write("")
    col2.write("")
    col2.write("")
    with st.spinner('Cartooning Image ...'):
        final_img= cartoon(model_path,bg_image)
        
    col2.image(final_img, caption='cartoonified image.', use_column_width=True)
    # download image
    col2.markdown(get_image_download_link_cartoon(Image.fromarray(final_img)), unsafe_allow_html=True)
    st.balloons()

    





