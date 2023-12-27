import google.generativeai as palm
from deepface import DeepFace
import streamlit as st
import urllib.request
import numpy as np
import pandas as pd
import replicate
import random
import time
import os

st.set_page_config(page_title="FINDING SOMEONE", page_icon="🔓", layout='wide')
st.markdown(
   """
   <style>
   img {cursor: pointer; transition: all .2s ease-in-out}
   img:hover {transform: scale(1.05)}
   </style>
   """,
   unsafe_allow_html=True)

def show(col, i=int):
    col.header(f':grey[Matching {i}]')
    col.image(similar_img[i], width=280)
    col.subheader((round(score[i]*100),2) + '%')

col1, col2, col3 = st.columns([0.05, 0.9, 0.05])
col2.image("style/heading3_1.jpg")
col1.write('~ '*80)
col3.write('~ '*80)

tab1, tab2, tab3 = st.tabs(["📝 GET TO KNOW","📬 FIND OUT", "⛑️ TIPS AND FACTS"])
with tab1:
    col2.title(":grey[**- REGCONITION: FINDING ONE'S LOST ~ ONCE LOST -**]")
    st.info("This is where you can find your relatives, friends and the identification of someone who needs help.")
    st.header(":grey[**GET TO KNOW WHO IS LOST**]")  
    
    col1, col2 = st.columns([0.3,0.76], gap='small')
    with col2.form('description'):
        st.subheader('**PERSONAL INFORMATION**')
        colA, colB, colC = st.columns([0.25,0.4, 0.3], gap='small')
        gender = colA.radio("***Biological gender:***", ["Boy","Girl"], horizontal=True, index=None)
        if gender == 'Boy': pronounce = 'His'
        elif gender == 'Girl': pronounce = 'Her'
        else: pronounce = 'The'
        age = colB.number_input(f"***{pronounce} age:***", 0, 150)
        race = colC.selectbox(f'***{pronounce} race:***', ['American','Asian','Indian','Middle Eastern','Latino Hispanic'], index=None, placeholder='Choose a race')

        colI, colII = st.columns([0.4,0.6])
        colI.subheader('**ABOUT FACE** '+'-'*15)
        colII.subheader('**ABOUT HAIR** '+'-'*33)
        colA, colB, colC, colD = st.columns([0.2,0.2,0.3,0.3])
        faceshape = colA.selectbox(f"***{pronounce} face shape:***", ['oval','square','round','diamond','heart'], index=None, placeholder='Choose a shape')
        skin = colB.selectbox(f"***{pronounce} skin:***", ['bright','tan'], index=None, placeholder='Choose a shape')
        hairlength = colC.selectbox(f'***{pronounce} hair length:***',['long','short','shoulderlength'], index=None, placeholder='Choose the length')
        haircolor = colD.selectbox(f"***{pronounce} hair color:***",['black','blond', 'brown', 'white'], placeholder='Choose a color')

        colI, colII = st.columns([0.4,0.5])
        colI.subheader('**ABOUT EYE** '+'-'*20)
        colII.subheader('**ABOUT NOSE** '+'-'*28)
        colA, colB, colC, colD = st.columns([0.3,0.3,0.4,0.3])
        eyesize = colA.radio(f"***{pronounce} eye:***", ['small','big'], horizontal=True, index=None)
        eyebrow = colB.radio(f"***{pronounce} eyebrow:***", ['thick','thin'], horizontal=True, index=None)
        noseshape = colC.multiselect(f"***{pronounce} nose shape:***",['straight','pug','crooked','pointed'])
        nosesize = colD.radio(f"***{pronounce} nose size:***",['big','small'], horizontal=True, index=None)
        draw = st.form_submit_button('DRAW', type='primary', use_container_width = True)
        
    with col1:
        with st.form('find'):
            colA, colB = st.columns([0.55,0.4])
            header = colA.subheader('OUR SKETCH:')
            find = colB.form_submit_button('FIND NOW', type='primary', help='Click here to see what we imagine about the lost one.', use_container_width= True)
            imgshow = st.image("style/default_img.jpg")
    if draw:
        des = f'realistic color portrait photo of {age} year olds {race} {gender} who has {skin} skin, {eyesize} eye, {eyebrow} eyebrow, {noseshape} nose, {hairlength} hair'
        replicate = replicate.Client(api_token='r8_XoAyduGHWDjA6jgFvABGsXNBvN757qA27x6Lt')
        output = replicate.run("stability-ai/stable-diffusion:27b93a2413e7f36cd83da926f3656280b2931564ff050bf9575f1fdf9bcd7478", input={"prompt": des})
        urllib.request.urlretrieve(output[0], "style/sample_img.png")
        imgshow.empty()
        imgshow = colA.image('style/sample_img.png', width=280)

    header = tab2.columns([0.32,0.8])[1].title('THERE IS NO RESULT YET')
    if find:
        header.empty()
        with st.spinner('Wait for us...'):
            my_bar = st.progress(0, text='Operation in progress. Please wait.')
            for percent_complete in range(100):
                time.sleep(0.01)
                my_bar.progress(percent_complete + 1, text='Operation in progress. Please wait.')
            time.sleep(1)
        result = DeepFace.find(img_path = "style/sample_img.png", db_path = 'images', enforce_detection = False)
        df = result[0]
        df.head()
        result = result.reshape((-1,10))
        result = np.flip(result)
        similar_img, score = result[:10,0], result[:10,9]
        tab2.header("**LOOK AT THE :grey[**MATCHING RESULT**]**")
        my_bar.empty()
        col1, col2, col3, col4, col5 = tab2.columns(5)
        show(col1, 0)
        show(col1, 5)
        show(col2, 1)
        show(col2, 6)
        show(col3, 2)
        show(col3, 7)
        show(col4, 3)
        show(col4, 8)
        show(col5, 4)
        show(col5, 9)
        os.remove("images/representations_vgg_face.pkl")

with tab2:
    st.info("This is where you see the result of people similar to our sketch.")
    st.write('')
with tab3:
    col1, col2 = st.columns([0.35,0.65])
    col2.title('**TIPS AND FACT**')
    palm.configure(api_key="AIzaSyBrCL27cjlIiPQO4ng4JRFTwED3VHHoGk8")
    prompt = st.text_input('***Write your questions here:***', placeholder='Here is your question.')
    if len(prompt) > 0:
        response = palm.generate_text(prompt=prompt, temperature=random.uniform(0, 1))
        text = st.warning(response.result)