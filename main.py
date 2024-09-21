import streamlit as st

# Set the page configuration
st.set_page_config(page_title="Community Resource Hub - NGO Portal", layout="wide")

# Header
st.title("Welcome to the Community Resource Hub")
st.subheader("Your Central Hub for Support and Resources")
st.markdown("🌍 Join our community and access vital resources and support services! 🚀")

# Create a container
with st.container():
    cols = st.columns(2)
    with cols[0]:
        st.write("...")
    
    with cols[1]:
        st.write("...")