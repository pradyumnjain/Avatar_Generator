import streamlit as st
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy as np
import pandas as pd

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
st.markdown('<p class="small-font">Upload a photo to transform : </p>',unsafe_allow_html=True )



