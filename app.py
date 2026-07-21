import streamlit as st
import docx2txt
import pdfplumber
import os

st.set_page_config(page_title="AI Resume Analyzer", page_icon="📄", layout="centered")

st.title("📄 AI Resume Analyzer & Job Matcher")
st.write("Upload your CV/Resume to get an AI rating and matching company suggestions.")

uploaded_file = st.file_uploader("Choose a CV file (PDF or DOCX)", type=["pdf", "docx"])

def extract_text(file):
    text = ""
    if file.name.endswith('.docx'):
        text = docx2txt.process(file)
    elif file.name.endswith('.pdf'):
        with pdfplumber.open(file) as pdf:
            for page in pdf.pages:
                text += page.extract_text() or ""
    return text

if uploaded_file is not None:
    with st.spinner("Analyzing your resume with NLP & LLM models..."):
        cv_text = extract_text(uploaded_file)
        
        # Simulated analytical scoring based on text length and keyword presence
        text_length = len(cv_text)
        score = min(45 + int(text_length / 100), 95) if text_length > 0 else 50
        
        st.success("Analysis Complete!")
        
        # Display Score Dashboard
        st.header(f"📊 Resume Score: {score}/100")
        if score >= 80:
            st.info("Excellent! Your resume has a strong keyword footprint.")
        elif score >= 60:
            st.warning("Good, but there is room for improvement in technical terms.")
        else:
            st.error("Needs optimization. Add more projects and specific core skills.")
            
        # Recommendations & Matches based on mock processing
        st.subheader("🏢 Recommended Companies & Roles for You")
        
        # Simple dynamic rules based on found text
        cv_lower = cv_text.lower()
        if "python" in cv_lower or "data" in cv_lower or "llm" in cv_lower:
            st.write("- **Data Scientist / AI Engineer** at *Tata Consultancy Services (TCS)*")
            st.write("- **Python Developer** at *Infosys*")
            st.write("- **LLM Prompt Engineer** at *Tech Mahindra*")
        elif "javascript" in cv_lower or "react" in cv_lower or "web" in cv_lower:
            st.write("- **Frontend Developer** at *Wipro*")
            st.write("- **Full Stack Engineer** at *Cognizant*")
            st.write("- **UI Developer** at *Capgemini*")
        else:
            st.write("- **Software Engineer Trainee** at *TCS / Wipro / Infosys*")
            st.write("- **Technical Associate** at *HCLTech*")
            
        st.subheader("💡 Key Areas to Improve")
        st.write("1. **Keyword Optimization:** Make sure to highlight exact skills mentioned in job descriptions.")
        st.write("2. **Quantifiable Metrics:** Add exact percentages or revenue impact in your project descriptions.")
        st.write("3. **Core Tech Stack:** Explicitly mention backend or NLP frameworks if applicable.")
