import streamlit as st

# Set the page configuration
st.set_page_config(page_title="Community Resource Hub - NGO Portal", layout="wide")

# Header
st.title("Welcome to the Community Resource Hub")
st.subheader("Your Central Hub for Support and Resources")
st.markdown("🌍 Join our community and access vital resources and support services! 🚀")

# Navigation
st.markdown("## Explore Our Resources")
st.write("Select a category below to find more information:")
options = ["Education", "Hunger", "Health", "Quality of Life"]
selected_option = st.selectbox("Choose a resource category:", options)

# Display content based on selection
if selected_option == "Education":
    st.write("### Education Resources")
    st.write("Access educational institutions, scholarships, and training programs.")
    # Link to education page
    st.markdown("[Learn More](1_education.py)")

elif selected_option == "Hunger":
    st.write("### Hunger Relief Resources")
    st.write("Find food banks and nutrition programs.")
    # Link to hunger page
    st.markdown("[Learn More](2_hunger.py)")

elif selected_option == "Health":
    st.write("### Health Services")
    st.write("Discover healthcare facilities and mental health resources.")
    # Link to health page
    st.markdown("[Learn More](3_health.py)")

elif selected_option == "Quality of Life":
    st.write("### Quality of Life Resources")
    st.write("Explore housing support, employment services, and community activities.")
    # Link to quality of life page
    st.markdown("[Learn More](4_qualityoflife.py)")

# Footer
st.markdown("---")
st.markdown("© 2025 Community Resource Hub | Follow us on [Twitter](#) | [Facebook](#) | [Instagram](#)")
