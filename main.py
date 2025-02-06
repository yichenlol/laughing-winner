import streamlit as st

# Set the page configuration
st.set_page_config(page_title="Community Resource Hub - NGO Portal", layout="wide")

# Header
st.title("Community Resource Hub")
st.markdown("### Access resources and contact NGO's")
st.markdown("Get connected with essential services!")

# Main sections
st.markdown("## Explore Our Services")
st.write("Choose a category to find the resources you need.")

# Resource categories
cols = st.columns(4)

with cols[0]:
    st.image("https://via.placeholder.com/150", caption="Education")
    st.markdown("[**Education**](1_education.py): Learn about schools, scholarships, and training programs.")

with cols[1]:
    st.image("https://via.placeholder.com/150", caption="Hunger Relief")
    st.markdown("[**Hunger Relief**](2_hunger.py): Find food banks and nutrition programs.")

with cols[2]:
    st.image("https://via.placeholder.com/150", caption="Health Services")
    st.markdown("[**Health Services**](3_health.py): Discover healthcare facilities and mental health resources.")

with cols[3]:
    st.image("https://via.placeholder.com/150", caption="Quality of Life")
    st.markdown("[**Quality of Life**](4_qualityoflife.py): Access housing support and community activities.")

# Footer
st.markdown("---")
st.markdown("© 2025 Community Resource Hub")
