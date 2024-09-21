import streamlit as st

st.set_page_config(page_title='hunger', page_icon=':wave:', layout= "wide")

st.title("hunger")

with st.container():
    cols = st.columns(2)
    with cols[0]:
         st.markdown(
            "<p style='font-size: 22px;'>Hunger in Hong Kong is a pressing issue, exacerbated by high living costs and income inequality. Many families struggle to afford basic necessities, leading to food insecurity and malnutrition, particularly among children and the elderly. Despite the city’s wealth, a significant portion of the population relies on food banks and community kitchens for support. The COVID-19 pandemic further intensified these challenges, highlighting the need for effective social safety nets. Community initiatives aimed at reducing food waste and improving access to affordable, nutritious food are essential. Experts call for comprehensive policies to address the underlying causes of hunger and promote food justice for all residents.</p>",
            unsafe_allow_html=True
        )

    with cols[1]:
        st.image('hunger.jpg', use_column_width=True)

st.divider()

with st.container():
    cols = st.columns(3)
    with cols[0]:
        st.header("Food Angel")
        st.write(
            "Food Angel is a non-profit food rescue and food assistance program in Hong Kong that aims to help those in need. It was founded in 2011 with the mission of \"Waste Not, Hunger Not\" - rescuing edible surplus food from the food industry and redistributing it to the underprivileged communities."
        )
        st.button("contact ngo 1")
    with cols[1]:
        st.header("Feeding HK")
        st.write(
            "Feeding Hong Kong is a non-profit organization that partners with food companies, charities, and volunteers to redistribute surplus food from where it is plentiful to where there is need in Hong Kong. Their mission is to reduce food waste and support vulnerable communities by providing meals to those who struggle to afford food."
        )
        st.button("contact ngo 2")
    with cols[2]:
        st.header("Food for Good")
        st.write(
            "Food for Good is a Hong Kong-based non-profit organization that works to alleviate food insecurity and reduce food waste. They collect surplus food from retailers, restaurants, and manufacturers, and distribute it to underprivileged communities through a network of food banks and social welfare organizations."
        )
        st.button("contact ngo 3")
st.divider()
with st.container():
    st.write("© 2023 Community Resource Hub HK. All rights reserved.")