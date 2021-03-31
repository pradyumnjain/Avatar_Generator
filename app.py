import streamlit as st
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy as np
import pandas as pd
from PIL import Image
import sys
import os
from io import BytesIO
import tensorflow as tf 
from cartoonize import cartoon
import network 
import guided_filter 
import base64
from seg import DeepLabModel
from seg import run_visualization
import SessionState


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
st.title('Upload')
st.header("Upload a photo to transform :-) ")

### Excluding Imports ###
#st.title("Upload a photo to transform :-) ")

def bg_removal(image, model):
    with st.spinner('Removing background ...'):
        bg_image = run_visualization(image, MODEL)
    st.success('Done!')
    st.image(bg_image, caption='background removed image.', use_column_width=True)
    # download image
    st.markdown(get_image_download_link_bg(bg_image), unsafe_allow_html=True)
    return bg_image

def cartoonify(image , model_path):
    st.markdown("<h1 style='text-align: center; color: white;'>Image Cartooning</h1>", unsafe_allow_html=True)
    with st.spinner('Cartooning Image ...'):
        final_img= cartoon(model_path,image)
    st.image(final_img, caption='cartoonified image.', use_column_width=True)
    # download image
    st.markdown(get_image_download_link_cartoon(Image.fromarray(final_img)), unsafe_allow_html=True)
    st.balloons()  



uploaded_file = st.file_uploader("Choose an image...", type=["jpg","jpeg","png"])
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.markdown("<h1 style='text-align: center; color: white;'>Original Image</h1>", unsafe_allow_html=True)
    st.image(image,width=300, caption='Uploaded Image.', use_column_width=True)
    st.write("")
    
    ss = SessionState.get(i=image)
    st.markdown("click bg_removal multiple time until satisfied with the output")
    if(st.button("Bg_removal", key="1")):
        st.markdown("<h1 style='text-align: center; color: white;'>Background Removal</h1>", unsafe_allow_html=True)
        modelType = "xception_model"
        MODEL = DeepLabModel(modelType)
        ss.i=bg_removal(ss.i, MODEL)


    st.markdown("click cartoonify to get cartoonized output")
    if(st.button("cartoonify",key="2")):
        model_path = 'test_code/saved_models'
        cartoonify(ss.i , model_path)




 
    
    









    # # background removal
    # modelType = "xception_model"
    # MODEL = DeepLabModel(modelType)
    # st.markdown("<h1 style='text-align: center; color: white;'>Background Removal</h1>", unsafe_allow_html=True)
    # with st.spinner('Removing background ...'):
    #     bg_image = run_visualization(image, MODEL)
    # st.success('Done!')
    # st.image(bg_image, caption='background removed image.', use_column_width=True)
    # # download image
    # st.markdown(get_image_download_link_bg(bg_image), unsafe_allow_html=True)
    # k =1
    # def rec(bg_image, Model,k):
    #     st.markdown("would you like to perform background removal again?")
    #     if(st.button("Yes", key="y"+str(k))):
    #         with st.spinner('Removing background ...'):
    #             new_img = run_visualization(bg_image, Model)
    #         st.success('Done!') 
    #         st.image(new_img, caption='background removed image.', use_column_width=True)   
    #         rec(new_img, Model, k+1)
    #     elif(st.button("No", key= "n"+str(k))):
    #         model_path = 'test_code/saved_models'
    #         st.markdown("<h1 style='text-align: center; color: white;'>Image Cartooning</h1>", unsafe_allow_html=True)

    #         with st.spinner('Cartooning Image ...'):
    #             final_img= cartoon(model_path,bg_image)
        
    #         st.image(final_img, caption='cartoonified image.', use_column_width=True)
    #         # download image
    #         st.markdown(get_image_download_link_cartoon(Image.fromarray(final_img)), unsafe_allow_html=True)
    #         st.balloons()    

    # rec(bg_image, MODEL, k)
   
    

    





