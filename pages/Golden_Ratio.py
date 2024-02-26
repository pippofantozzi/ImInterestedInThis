import streamlit as st
from texts.textGolden import get_images, process_text


st.title("🪷 The Golden Ratio")
st.subheader("Unveiling the Myth and Reality in Nature")

st.markdown("---")

st.write("The Golden Ratio, often symbolized as Phi (Φ) or phi, is a mathematical constant that has fascinated mathematicians, artists, and scientists for centuries. Its value, approximately 1.618, is found in various natural, architectural, and artistic forms, leading many to speculate about its universal significance. However, the distinction between the myth and reality of the Golden Ratio is nuanced, blending mathematical truths with human pattern recognition tendencies.")
st.markdown("##")
st.image("images/Golden/chameleon.jpg",caption="The Golden Ratio",use_column_width=True)

subheaders, texts = process_text()
images = get_images()
for i in range(len(subheaders)):
    st.subheader(subheaders[i])
    st.write(texts[i])
    if images[i] != "Nothing":
        st.image(images[i], caption=subheaders[i], use_column_width=True)

    if subheaders[i] == "Understanding the Golden Ratio":
        choice = st.selectbox("Choose which rectangle you think is most aesthetically pleasing, and well tell you which has the Golden Ratio:",
                     ["A","B","C","D","E","F","G","H","I","J"])
        check = st.button("Click to check:")
        if check:
            if choice == "D":
                st.write("You picked the Golden Rectangle, which 79% of our users agree is the most aesthetic rectangle of the bunch")
            else:
                st.write(f"You picked {choice}, while the Golden Rectangle was D. Maybe your mind works in a unique way. (Take that as a compliment)")
        


