import streamlit as st
from texts.textNEAT import get_images, process_text
st.set_page_config(
    page_title="Im Interested In NEAT",
    page_icon="🔍",
    
)

st.title("🐣 The NEAT Algorithm")
st.subheader("How Natural Selection and Evolution can help us make better AI")

st.markdown("---")

st.write("Imagine you're in charge of evolving a population of creatures to perform a specific task, like navigating a maze. That's where NEAT, or NeuroEvolution of Augmenting Topologies, comes into play.")
st.markdown("##")
st.video("webimages/Flappy.mp4")

subheaders, texts = process_text()
images = get_images()
for i in range(len(subheaders)):
    st.subheader(subheaders[i])
    st.write(texts[i])
    if images[i] != "Nothing":
        st.image(images[i], caption=subheaders[i], use_column_width=True)

    if subheaders[i] == 'Wrapping Up':
        st.markdown("##")
        st.markdown("---")
        st.title("A Section Which Might Interest AI Developers")
        st.markdown("##")
        st.markdown("---")


