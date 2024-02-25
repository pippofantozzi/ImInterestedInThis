import streamlit as st
from texts.textTuring import get_images, process_text,simulate_turing_patterns
import matplotlib.pyplot as plt


st.title("🐯 Unraveling Nature's Patterns: The Turing Theory")
st.subheader("How The Spots In Cheetas Relate To AI Image Generation")

st.markdown("---")

st.write("Nature's canvas is splashed with an array of patterns, from the intricate stripes on a surgeonfish to the distinctive spots on a cheetah. These patterns have fascinated scientists and laypeople alike for centuries, prompting the question: How does nature create such diverse and complex designs from seemingly simple rules? Alan Turing, a pioneer in computing, proposed a mathematical theory that could explain this natural phenomenon.")
st.markdown("##")
one,two = st.columns(2)
with one:
    Du = st.sidebar.slider('Diffusion rate of Activator (Du)', 0.10, 0.20, 0.16)
    Dv = st.sidebar.slider('Diffusion rate of Inhibitor (Dv)', 0.05, 0.10, 0.08)
with two:
    feed_rate = st.sidebar.slider('Feed Rate', 0.02, 0.06, 0.035)
    kill_rate = st.sidebar.slider('Kill Rate', 0.05, 0.07, 0.06)


u, v = simulate_turing_patterns(Du=Du, Dv=Dv, feed_rate=feed_rate, kill_rate=kill_rate)
fig, ax = plt.subplots()
ax.imshow(u, cmap='plasma')
ax.axis('off')
st.pyplot(fig)

subheaders, texts = process_text()
images = get_images()
for i in range(len(subheaders)):
    st.subheader(subheaders[i])
    st.write(texts[i])
    if images[i] != "Nothing":
        st.image(images[i], caption=subheaders[i], use_column_width=True)

    


