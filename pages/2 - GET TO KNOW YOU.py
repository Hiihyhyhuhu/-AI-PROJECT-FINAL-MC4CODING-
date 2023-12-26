import streamlit as st
import datetime as dt
import time

st.set_page_config(page_title="GET TO KNOW YOU", page_icon="👋", layout='wide')
st.markdown(
   """
   <style>
   img {cursor: pointer; transition: all .2s ease-in-out}
   img:hover {transform: scale(1.04)}
   </style>
   """,
   unsafe_allow_html=True)
col1, col2, col3 = st.columns([0.05, 0.9, 0.05])
col2.image("style/heading2_1.JPG")
col1.write('~ '*80)
col3.write('~ '*80)
col2.title(":grey[**JOIN US - GET AN ACCOUNT - HELP OUR COMUNITY**]")
warn = st.warning("You haven't register for an account yet.")
st.header('**CREATING AN ACCOUNT**')
col1, col2 = st.columns([0.76,0.3], gap='medium')
with col1:
    colA, colB= st.columns([0.3,0.4], gap='medium')
    familyname = colA.text_input("***Your family name:***", placeholder='Enter your family name')
    firstname = colB.text_input("***Your first name:***", placeholder='Enter your first name')
    birthday = st.date_input("***Your birthday:***", min_value= dt.date(1900,1,1), format='DD/MM/YYYY')
    st.slider(f"***You are {2023 - birthday.year} year olds***", 1, 150, 2023 - birthday.year, disabled=True)
    hometown = st.selectbox('***Your hometown:***', options =
        ["An Giang province",
        "Ba Ria-Vung Tau province",
        "Bac Giang province",
        "Bac Kan province",
        "Bac Lieu province",
        "Bac Ninh province",
        "Ben Tre province",
        "Binh Dinh province",
        "Binh Duong province",
        "Binh Phuoc province",
        "Binh Thuan province",
        "Ca Mau province",
        "Can Tho city",
        "Cao Bang province",
        "Da Nang city",
        "Dak Lak province",
        "DaK Nong province",
        "Dien Bien province",
        "Dong Nai province",
        "Dong Thap province",
        "Gia Lai province",
        "Ha Giang province",
        "Ha Nam province",
        "Ha Noi city",
        "Ha Tinh province",
        "Hai Duong province",
        "Hai Phong city",
        "Hau Giang province",
        "Ho Chí Minh city",
        "Hoa Binh province",
        "Hung Yen province",
        "Khanh Hoa province",
        "Kien Giang province",
        "Kon Tum province",
        "Lai Chau province",
        "Lam Dong province",
        "Lang Son province",
        "Lao Cai province",
        "Long An province",
        "Nam Dinh province",
        "Nghe An province",
        "Ninh Binh province",
        "Ninh Thuan province",
        "Phu Tho province",
        "Phu Yen province",
        "Quang Binh province",
        "Quang Nam province",
        "Quang Ngai province",
        "Quang Ninh province",
        "Quang Tri province",
        "Soc Trang province",
        "Son La province",
        "Tay Ninh province",
        "Thai Binh province",
        "Thai Nguyen province",
        "Thanh Hoa province",
        "Thua Thien-Hue province",
        "Tien Giang province",
        "Tra Vinh province",
        "Tuyen Quang province",
        "Vinh Long province",
        "Vinh Phuc province",
        "Yen Bai province"],
        index = None,
        placeholder = 'Choose your hometown')
    colA, colB= st.columns([0.2,0.4], gap='medium')
    phone = colA.text_input("***Your phone number:***", placeholder='Enter your phone number')
    mail = colB.text_input("***Your mail:***", placeholder='Enter your mail address')
    st.write('')
    button = st.button('Create my account', type='primary', use_container_width = True)
with col2:
    st.header('**YOUR PROFILE**')
    imgshow = st.image("style/default_img.jpg")
    holder = st.empty()
    avatar = holder.file_uploader('Upload photo', type='jpg', key=1)
    if avatar is not None:
        st.image(avatar, width=300)
        imgshow.empty()
        holder.empty()
if button:
    with st.spinner('Wait for us...'):
            my_bar = st.progress(0, text='Operation in progress. Please wait.')
    for percent_complete in range(100):
        time.sleep(0.01)
        my_bar.progress(percent_complete + 1, text='Operation in progress. Please wait.')
    time.sleep(1)
    my_bar.empty()
    warn.empty()
    st.success('You have registered', icon='✅')
with st.sidebar:
   if st.button('Where to go'):
      msg = st.toast("Find someone at FINDING ONE'S LOST - ONCE LOST", icon = "👨‍👩‍👧‍👦")
      time.sleep(5)