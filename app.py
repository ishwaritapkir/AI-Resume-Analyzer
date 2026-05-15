##code for detect skills
import streamlit as st
import PyPDF2

st.title("AI Resume Analyzer")

uploaded_file = st.file_uploader("Upload Resume", type=["pdf"])

if uploaded_file is not None:

    pdf_reader = PyPDF2.PdfReader(uploaded_file)

    text = ""

    for page in pdf_reader.pages:
        text += page.extract_text()

    resume_text = text.lower()

    skills = ["python", "sql", "machine learning", "java"]

    found_skills = []

    for skill in skills:
        if skill in resume_text:
            found_skills.append(skill)

    st.header("Detected Skills")

    st.write(found_skills)