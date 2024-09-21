import streamlit as st

# Set the page configuration
st.set_page_config(page_title='Health', page_icon=':wave:', layout="wide")


# Title
st.title("Health in Hong Kong")

with st.container():
    cols = st.columns(2)
    with cols[0]:
        st.markdown(
            "<p style='font-size: 22px;'>Healthcare in Hong Kong faces challenges, including an increasing demand for services and long waiting times for public hospital treatments. While the city boasts a high standard of medical care, access is often limited for lower-income residents, leading to disparities in health outcomes. The aging population further strains the healthcare system, necessitating more resources and support for chronic diseases. Mental health services also require urgent attention, as stigma and lack of awareness hinder access. Experts advocate for a comprehensive approach to healthcare reform, emphasizing the need for improved funding, expanded services, and community outreach to ensure equitable access for all citizens.</p>",
            unsafe_allow_html=True
        )
    with cols[1]:
        st.image('doctor.jpg', use_column_width=True)

st.divider()

with st.container():
    cols = st.columns(3)
    with cols[0]:
        st.header("Hong Kong Red Cross")
        st.write(
            "The Hong Kong Red Cross is a non-profit organization that provides a wide range of health and social services to the community. "
            "They offer emergency medical and disaster relief, as well as programs focused on youth development, first aid training, and blood donation."
        )
        st.button("Contact NGO 4")
    with cols[1]:
        st.header("Hong Kong Adventist Hospital")
        st.write(
            "Hong Kong Adventist Hospital is a non-profit, private hospital that provides comprehensive medical services, including acute care, outpatient clinics, and community health programs. "
            "They are committed to promoting holistic health and wellness in the local community."
        )
        st.button("Contact NGO 5")
    with cols[2]:
        st.header("Médecins Sans Frontières")
        st.write(
            "Médecins Sans Frontières (Doctors Without Borders) is an international, independent medical humanitarian organization that provides emergency relief and healthcare services in Hong Kong and around the world. "
            "They focus on providing medical care to those in crisis situations and underserved communities."
        )
        st.button("Contact NGO 6")

st.divider()

with st.container():
    st.write("© 2023 Community Resource Hub. All rights reserved.")