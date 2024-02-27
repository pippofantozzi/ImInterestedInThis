import streamlit as st
from texts.textStable import get_images, process_text


st.title("🎨 Stable Diffusion")
st.subheader("How we turn a static TV like image into whatever we want")

st.markdown("---")

st.write("Imagine this: Franc, an artist hailing from the quirky town of Janice, where artists seem to have a knack for slipping and turning their canvases into messy blobs of paint. Recognizing an untouched opportunity, Franc dedicates years intentionally blurring his paintings, only to skillfully recreate them from the abstract blur. Mastering this unique craft, he hits the streets to offer his services, and business flourishes. However, skeptics in the crowd question if it's all a scam.")
st.write("In an attempt to test him, they randomly throw buckets of paint onto a canvas, claiming there was a masterpiece before the accidental blur. Unfazed and brimming with confidence, Franc takes on the challenge. Within minutes, he presents them with a stunning painting of oak trees on a mountain top, with a vivid Sunset on the background. That, is Stable Diffusion in a nutshell.")
st.markdown("##")


subheaders, texts = process_text()
images = get_images()
for i in range(len(subheaders)):
    st.subheader(subheaders[i])
    st.write(texts[i])
    if images[i] != "Nothing":
        st.image(images[i], caption=subheaders[i], use_column_width=True)

  


