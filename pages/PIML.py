import streamlit as st
from texts.textPIML import get_images, process_text

st.title("🌌 Physics Informed Machine Learning")
st.subheader("Finding new elements, materials, and preventing disasters by combining Physics with ML")

st.markdown("---")

st.write("In the quaint village of Seabreeze, a curious challenge emerged among a group of friends. They wagered on who could predict where the sea would carry a tiny paper boat within a minute. For weeks, the group meticulously observed the ocean's rhythms, launching countless boats and recording their fates, hoping to uncover a pattern in the chaos. All except for Lily, who approached the task with a different lens. Armed with a deep understanding of the ocean's physics—its currents, the wind's influence, and the subtle pull of the moon—Lily needed only a day's observation. While her friends relied on brute force and endless data, Lily's insight into the underlying principles allowed her to predict the boat's journey with uncanny accuracy. Her success was a testament to the power of knowledge, serving as a vivid metaphor for Physics-Informed Machine Learning: sometimes, understanding the fundamental laws that govern a system can unveil the most profound truths, far beyond the reach of observation alone.")
st.video("images/PIML/physics.mp4")
st.markdown("##")


subheaders, texts = process_text()
images = get_images()
for i in range(len(subheaders)):
    st.subheader(subheaders[i])
    st.write(texts[i])
    if images[i] != "Nothing":
        st.image(images[i], caption=subheaders[i], use_column_width=True)

  


