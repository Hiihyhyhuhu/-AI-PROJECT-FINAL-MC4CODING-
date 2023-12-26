import streamlit as st

st.set_page_config(page_title="GET TO KNOW US", page_icon="🤝", layout='wide')
st.markdown(
   """
   <style>
   img {cursor: pointer; transition: all .2s ease-in-out}
   img:hover {transform: scale(1.04)}
   </style>
   """,
   unsafe_allow_html=True)

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
local_css("style/style.css")

col1, col2, col3 = st.columns([0.05, 0.9, 0.05])
col2.image("style/heading1_1.JPG")
col1.write('~ '*80)
col3.write('~ '*80)
st.title(":grey[**FINDING ONE'S LOST - ONCE LOST**]")
st.write("Your family as well as your friends are ***the most precious treasure*** you have ever had " + "-"*280 + " Let us carry out the mission to find out them")
st.image('style/heading1_2.JPG')
col1, col2, col3 = st.columns([0.5,0.25,0.25])
with col1:
    st.subheader(":grey[WHO WE ARE...]")
    st.write("We are just alike: normal people doing such ordinary things that worth nothing. We are willing to back up the community in order to **ease the sorrow of getting somebody lost**. Steping out of the safe zone, we hold the desire to knit the tie between the pure souls to get back to their family, friends.")
    st.subheader(":grey[WHAT WE DO...]")
    st.write("We organise some researches on AI models to address the conundrum. Finding out the most feasible approach to figure out who is the one that needs finding. Then, we develop a mean of metarializing our dream. We bielieve that... **evenwhen you lost someone, don't lost yourself by losing heart**.")
    st.write("Not only do we **make effort to search for the one who is lost**, but it also **confirms the identification**, hence the improvement of security services. Since prioritising the social safety, we make sure to enhance the quality of this searching engine.")
with col2:
    colA, colB, colC = st.columns([0.6,0.6,0.6])
    with colA:
        st.write('')
    with colB:
        st.subheader('Tien: Founder')
    with colC:
        st.write('')
    st.image('style/anhTien.JPG', width=300)
with col3:
    st.image('style/anhHy.JPG', width=300)
    colA, colB, colC = st.columns([0.6,0.6,0.3])
    with colA:
        st.write('')
    with colB:
        st.subheader('Hy: Co-Founder')
    with colC:
        st.write('')
st.image('style/heading1_2.JPG')
st.write('')
col1, col2 = st.columns([0.5,0.6])
with col1:
    st.image('style/heading1_3.JPG')
with col2:
    st.title(':grey[CONTACT US] -----------')
    with st.expander('**FEEDBACK**', expanded=False):
        contact_form = """
            <form action="https://formsubmit.co/hychanhtran@gmail.com" method="POST">
                <input type="hidden" name="_captcha" value="false">
                <input type="text" name="name" placeholder="Your name" required>
                <input type="email" name="email" placeholder="Your email" required>
                <textarea name="message" placeholder="Your message here" required></textarea>
                <button type="submit">Send</button>
            </form>
            """
        st.markdown(contact_form, unsafe_allow_html=True)
        st.write('')

with st.sidebar:
    if st.button('Where to go'):
        st.toast("Let us know you at GET TO KNOW YOU", icon='💓')