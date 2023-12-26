import streamlit as st
import base64

st.set_page_config(page_title="HOMEPAGE", page_icon="👋", layout='wide')
images = []
for file in ["style/pic2.jpg", "style/pic3.jpg", "style/pic4.jpg"]:
   with open(file, "rb") as image:
      encoded = base64.b64encode(image.read()).decode()
      images.append(f"data:image/jpg;base64,{encoded}")
st.header(":grey[**FINDING ONE'S LOST - ONCE LOST**]", help='Click on the sections below to get started.')
col1, col2 = st.columns([0.45,0.55])
with col1:
   st.markdown(f"[![Foo]({images[0]})](http://hiihyhyhuhu/-ai-project-final-mc4coding-/GET_TO_KNOW_US)")
   st.markdown(f"[![Foo]({images[1]})](http://hiihyhyhuhu/-ai-project-final-mc4coding-/GET_TO_KNOW_YOU)")
with col2:
   st.markdown(f"[![Foo]({images[2]})](http://hiihyhyhuhu/-ai-project-final-mc4coding-/FINDING_SOMEONE)")
with st.sidebar:
   if st.button('Where to go'):
      msg = st.toast("Find us at GET TO KNOW US", icon='🔍')