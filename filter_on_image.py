import streamlit as st
import cv2
import cv2.data
from PIL import Image,ImageFilter
from random import randint


st.title("image filter playground")

modelPath = cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
model=cv2.CascadeClassifier(modelPath)
file = cv2.imread("./file")
faces = model.detectMultiScale(file, 1.3, 5) 


file = st.file_uploader("Select Image",type=["png","jpg","jpeg"])

if file:
    option = st.selectbox("Select Filter",["Original","GrayScale","Blur","Face Detection"])

    img=Image.open(file)
    if option =="GrayScale":
        img= img.convert("L")
    if option =="Blur":
        img = img.filter(ImageFilter.BLUR)
    if option == "Face Detection":
        for face in faces:
            x,y,w,h = face

            red = randint(0,255)
            blue = randint(0,255)
            green = randint(0,255)
            file = cv2.rectangle(image,(x,y),(x+w,y+h),(red,blue,green),3)

    st.image(img)

    file.seek(0) #download prompt 
    img.save(file,format ="PNG")

    st.download_button(label="Download Image",data=file,file_name="stranger.jpg")
    
