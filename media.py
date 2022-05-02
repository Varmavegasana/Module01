import streamlit as st

#working Media(video/Audio/Image)

from PIL import Image
img = Image.open("downloadimage.jpg")
st.image(img,use_column_width=True)

#From URL
# st.image("https://www.istockphoto.com/collaboration/boards/j58EUsKy00WtX0BvfhqA9w")
