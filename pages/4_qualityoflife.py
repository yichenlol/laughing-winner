import streamlit as st

st.set_page_config(page_title='Quality of Life', page_icon=':wave:', layout="wide")

st.title("Quality of Life in Hong Kong")

with st.container():
    cols = st.columns(2)
    with cols[0]:
         st.markdown(
            "<p style='font-size: 22px;'>""Quality of life in Hong Kong faces challenges such as high living costs, limited affordable housing, and environmental issues. Many residents struggle to maintain a decent standard of living due to rising rents and stagnant wages. Additionally, pollution and a lack of green spaces can impact mental and physical well-being. To address these challenges, there is a growing need for community initiatives focused on sustainability, affordable housing, and mental health support. Experts advocate for comprehensive policies to improve urban living conditions and ensure that all citizens can enjoy a better quality of life..""</p>",
            unsafe_allow_html=True
        )
    with cols[1]:
        st.image('homeless.jpg', use_column_width=True) 

st.divider()

with st.container():
    cols = st.columns(3)
    with cols[0]:
        st.header("The Hong Kong Housing Society")
        st.write(
            "The Hong Kong Housing Society is dedicated to providing affordable housing solutions and improving living conditions for residents. They work on community development projects and provide support services to help families find stable housing."
        )
        st.button("Contact NGO 1")
    with cols[1]:
        st.header("Impact HK")
        st.write(
            "Impact HK is a non-profit organization that aims to support the homeless community in Hong Kong. They provide essential services such as food, shelter, and healthcare, and work to raise awareness about homelessness and its underlying issues."
        )
        st.button("Contact NGO 2")
    with cols[2]:
        st.header("Mind Hong Kong")
        st.write(
            "Mind Hong Kong is dedicated to promoting mental health awareness and providing resources for those in need. They offer support services and programs aimed at improving mental well-being in the community."
        )
        st.button("Contact NGO 3")

st.divider()

with st.container():
    st.write("© 2023 Community Resource Hub HK. All rights reserved.")