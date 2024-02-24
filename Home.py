import streamlit as st
st.set_page_config(
    page_title="Im Interested In This",
    page_icon="🔍",
    theme="dark",
)

st.title("👋 Hey There")
st.sidebar.success("Select a page to learn something.")
st.markdown("---")
st.subheader("This Should Be Interesting")
st.write("Every day there will be a new interesting page in this website, teaching complex things in simple ways. Hope you enjoy :)")
st.markdown("---")
st.subheader("Welcome")
st.write("I'm known to be easily mystified, and I find everything interesting. But I still think we give little credit to how beautiful our universe and its math and logic really are, and how they play a role in our everyday lives, nature, and in our future. I want to learn these things that interest me, and I want to give you the chance to see the beauty in them, give you more things to talk about, and make you smarter in the process.")
st.write("If that sounds like something you might be into, I'm glad you are here. If that doesn't sound like you, I bet you must be a great guest at a dinner table")
st.image("construction.webp",caption="This Whole Area Is Under Construction",use_column_width=True)

