import streamlit as st
import time
import model 
import io
from PIL import Image

st.title(":blue[Resnet] Image Classifier ")

st.html("<h>Description:")
st.html("<p>upload a image and we will find something that's in the image using this pretrainied model</p>")
img=st.file_uploader("Upload your image here")
if img:
    img = Image.open(io.BytesIO(img.read()))
    st.image(img)
    
    name,accuracy=model.process(img)
    
    progress_bar = st.progress(0)
    for i in range(100):
        time.sleep(0.05)
        progress_bar.progress(i + 1)

    name=name.decode('utf-8')
    st.write(f"Image : ***{name.title()}***")
    st.write(f"Accuracy : *{accuracy}*")

    if accuracy<60:
        st.warning("The model might not be trained on the data that you have uploaded as the accuracy is less it might gives irrelevant results")
    