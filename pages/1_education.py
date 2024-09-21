import streamlit as st

st.set_page_config(page_title='education', page_icon=':wave:', layout= "wide")

st.title("education")



with st.container():
    cols = st.columns(2)
    with cols[0]:
         st.markdown(
            "<p style='font-size: 22px;'>Accessibility to education in Hong Kong is a pressing issue, particularly for students from low-income families and marginalized communities. Many face barriers such as high tuition fees, the cost of private tutoring, and limited access to quality schools. Overcrowded classrooms in public institutions further hinder personalized learning and support. Additionally, students with special needs often struggle to find appropriate resources and inclusive environments. The competitive academic landscape leaves many children at a disadvantage, perpetuating cycles of inequality. Experts emphasize the need for policies that promote equitable access to education, ensuring that all children can pursue their academic goals without financial or social barriers.</p>",
            unsafe_allow_html=True
        )
    with cols[1]:
            st.image('education.jpg', use_column_width=True)
st.divider()
with st.container():
    cols = st.columns(3)
    with cols[0]:
        st.header("Bring Me a Book Hong Kong")
        st.write(
            "Bring Me a Book Hong Kong is a non-profit organization that promotes early childhood literacy and access to quality books. They work with schools, libraries, and community organizations to establish reading programs and provide books to underprivileged children."
        )
        st.button("contact ngo 1")
    with cols[1]:
        st.header("Project WeCan")
        st.write(
            "Project WeCan is a non-profit education initiative that partners with Hong Kong secondary schools to provide resources, mentorship, and opportunities to students from disadvantaged backgrounds. Their goal is to empower these students and help them reach their full potential."
        )
        st.button("contact ngo 2")
    with cols[2]:
        st.header("Education for Good")
        st.write(
            "Education for Good is a Hong Kong-based non-profit that focuses on improving access to quality education for underprivileged children and youth. They provide scholarships, learning resources, and support programs to help students succeed in school and beyond."
        )
        st.button("contact ngo 3")

st.divider()

with st.container():
    st.write("© 2023 Community Resource Hub HK. All rights reserved.")