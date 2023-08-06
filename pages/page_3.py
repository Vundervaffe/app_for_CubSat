import streamlit as st
from PIL import Image

arduino = Image.open("pictures\Arduino_Uno.png")
st.image(arduino)