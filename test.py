import streamlit as st
from PIL import Image

st.write("## Welcome to my website🍵")
st.write("## Follow me: ")

img = Image.open("SUBSCRIBETOOURCHANNEL.png")
st.image(
    img,
    caption="Youtube: ",
    width=100,
    channels="paper",

)
st.link_button(":red[Music channel]", "https://www.youtube.com/channel/UC_ogwyRl6D4MncWqxh200gQ")
st.link_button(":red[Main channel]", "https://www.youtube.com/@hakimasfat5068")

st.write("(Just learned how to code with streamlit LOL💀)")
