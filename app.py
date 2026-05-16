import streamlit as st
import PyPDF2
import matplotlib.pyplot as plt

# PAGE CONFIG
st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="centered"
)

# SIDEBAR
st.sidebar.title("📄 AI Resume Analyzer")

# MAIN TITLE
st.title("📄 AI Resume Analyzer")

st.divider()

# FILE UPLOAD
uploaded_file = st.file_uploader("Upload Resume", type=["pdf"])

# MAIN PROGRAM
if uploaded_file is not None:

    # READ PDF
    pdf_reader = PyPDF2.PdfReader(uploaded_file)

    text = ""

    for page in pdf_reader.pages:
        extracted_text = page.extract_text()

        if extracted_text:
            text += extracted_text

    # CONVERT TO LOWERCASE
    resume_text = text.lower()

    # REQUIRED SKILLS
    skills = ["python", "sql", "machine learning", "java"]

    found_skills = []
    missing_skills = []

    # DETECT SKILLS
    for skill in skills:

        if skill in resume_text:
            found_skills.append(skill)

        else:
            missing_skills.append(skill)

    # DISPLAY FOUND SKILLS
    st.header("✅ Detected Skills")

    if len(found_skills) == 0:
        st.warning("No matching skills found.")

    else:
        st.write(found_skills)

    st.divider()

    # ATS SCORE
    ats_score = (len(found_skills) / len(skills)) * 100

    st.header("📊 ATS Score")

    st.write(f"{ats_score:.0f}%")

    st.progress(int(ats_score) / 100)

    st.divider()

    # METRICS
    st.header("📌 Resume Metrics")

    col1, col2, col3 = st.columns(3)

    col1.metric("ATS Score", f"{ats_score:.0f}%")

    col2.metric("Skills Found", len(found_skills))

    col3.metric("Missing Skills", len(missing_skills))

    st.divider()

    # RESUME STATUS
    st.header("🚀 Resume Status")

    if ats_score >= 75:
        st.success("Strong Resume 🚀")
        st.balloons()

    elif ats_score >= 50:
        st.info("Average Resume")

    else:
        st.error("Needs Improvement")

    st.divider()

    # MISSING SKILLS
    st.header("❌ Missing Skills")

    if len(missing_skills) == 0:
        st.success("All important skills found!")

    else:
        for skill in missing_skills:
            st.error(skill)

    st.divider()

    # RESUME SUGGESTIONS
    st.header("💡 Resume Suggestions")

    if len(found_skills) < 3:
        st.warning("Add more technical skills.")

    if "projects" not in resume_text:
        st.warning("Add projects section.")

    if "internship" not in resume_text:
        st.warning("Add internship experience.")

    if "certification" not in resume_text:
        st.warning("Add certifications.")

    st.divider()

    # OVERALL FEEDBACK
    st.header("📝 Overall Feedback")

    if ats_score >= 75:
        st.success("Excellent resume! Your resume matches most ATS requirements.")

    elif ats_score >= 50:
        st.info("Good resume, but adding more skills and experience can improve it.")

    else:
        st.error("Resume needs improvement for better ATS performance.")

    st.divider()

    # PIE CHART
    st.header("📈 Skills Analysis Chart")

    labels = ["Found Skills", "Missing Skills"]

    sizes = [len(found_skills), len(missing_skills)]

    fig, ax = plt.subplots()

    ax.pie(
        sizes,
        labels=labels,
        autopct='%1.1f%%'
    )

    ax.axis('equal')

    st.pyplot(fig)

else:
    st.info("Please upload a PDF resume to start analysis.")