import streamlit as st
import google.generativeai as genai
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_JUSTIFY, TA_LEFT, TA_CENTER
from reportlab.lib.colors import navy, black
import io

# --- Page Configuration ---
st.set_page_config(
    page_title="AI Resume & Portfolio Builder",
    page_icon="📄",
    layout="wide",
)

# --- API Key Configuration ---
# This app is designed to work with Streamlit's secrets management.
st.sidebar.header("🔑 API Configuration")

# Check if the API key is available in secrets
if "GOOGLE_API_KEY" in st.secrets:
    api_key = st.secrets["GOOGLE_API_KEY"]
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-2.5-flash')
else:
    # If the key is not found, display an error and stop the app
    st.sidebar.error("Google AI API key not found.")
    st.warning("Please add your Google AI API key to your Streamlit secrets to continue.")
    st.info("For local development, create a file named `.streamlit/secrets.toml` with the content: \n\n`GOOGLE_API_KEY = 'YOUR_API_KEY_HERE'`")
    st.stop() # Stop the app from running further.


# --- PDF Generation Function ---
def create_resume_pdf(resume_data):
    """Generates a PDF resume from the provided data."""
    buffer = io.BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter,
                            rightMargin=50, leftMargin=50,
                            topMargin=50, bottomMargin=50)
    styles = getSampleStyleSheet()
    
    # Custom Styles
    styles.add(ParagraphStyle(name='NameStyle', fontName='Helvetica-Bold', fontSize=22, alignment=TA_CENTER, textColor=navy))
    styles.add(ParagraphStyle(name='ContactStyle', fontName='Helvetica', fontSize=10, alignment=TA_CENTER, spaceAfter=10))
    styles.add(ParagraphStyle(name='HeaderStyle', fontName='Helvetica-Bold', fontSize=14, textColor=navy, spaceBefore=12, spaceAfter=6, borderBottomWidth=1, borderBottomColor=navy, paddingBottom=2))
    styles.add(ParagraphStyle(name='BodyStyle', fontName='Helvetica', fontSize=10, alignment=TA_JUSTIFY, leading=14))
    styles.add(ParagraphStyle(name='JobTitleStyle', fontName='Helvetica-Bold', fontSize=11, spaceAfter=2))
    styles.add(ParagraphStyle(name='CompanyStyle', fontName='Helvetica-Oblique', fontSize=10, spaceAfter=6))
    
    story = []

    # 1. Name and Contact Info
    story.append(Paragraph(resume_data['full_name'], styles['NameStyle']))
    contact_info = f"{resume_data['email']} | {resume_data['phone']} | {resume_data['linkedin']}"
    story.append(Paragraph(contact_info, styles['ContactStyle']))
    story.append(Spacer(1, 24))

    # 2. Professional Summary
    story.append(Paragraph("Professional Summary", styles['HeaderStyle']))
    story.append(Paragraph(resume_data['summary'], styles['BodyStyle']))
    story.append(Spacer(1, 12))

    # 3. Work Experience
    if resume_data['experience']:
        story.append(Paragraph("Work Experience", styles['HeaderStyle']))
        for exp in resume_data['experience']:
            story.append(Paragraph(exp['title'], styles['JobTitleStyle']))
            company_info = f"{exp['company']} | {exp['location']} | {exp['dates']}"
            story.append(Paragraph(company_info, styles['CompanyStyle']))
            # Split responsibilities into bullet points
            responsibilities = exp['responsibilities'].split('\n')
            for resp in responsibilities:
                if resp.strip(): # Ensure not to add empty lines
                    story.append(Paragraph(f"• {resp.strip()}", styles['BodyStyle']))
            story.append(Spacer(1, 12))

    # 4. Education
    if resume_data['education']:
        story.append(Paragraph("Education", styles['HeaderStyle']))
        for edu in resume_data['education']:
            story.append(Paragraph(edu['degree'], styles['JobTitleStyle']))
            institution_info = f"{edu['institution']} | {edu['grad_date']}"
            story.append(Paragraph(institution_info, styles['CompanyStyle']))
            story.append(Spacer(1, 12))

    # 5. Skills
    if resume_data['skills']:
        story.append(Paragraph("Skills", styles['HeaderStyle']))
        story.append(Paragraph(resume_data['skills'], styles['BodyStyle']))

    doc.build(story)
    buffer.seek(0)
    return buffer

# --- Streamlit App UI ---
st.title("🤖 AI-Powered Resume Builder")
st.markdown("Create a professional resume in minutes. Fill in your details, and let our AI enhance your profile!")

# Define callbacks for adding items
def add_experience():
    st.session_state.experience.append({'title': '', 'company': '', 'location': '', 'dates': '', 'responsibilities': ''})

def add_education():
    st.session_state.education.append({'institution': '', 'degree': '', 'grad_date': ''})

# --- RECOMMENDED CHANGE HERE ---
# Initialize session state lists. Start with one blank entry for a better user experience.
if 'experience' not in st.session_state:
    st.session_state.experience = [{'title': '', 'company': '', 'location': '', 'dates': '', 'responsibilities': ''}]
if 'education' not in st.session_state:
    st.session_state.education = [{'institution': '', 'degree': '', 'grad_date': ''}]

# --- Data Collection Form ---
with st.form("resume_form"):
    st.header("1. Personal Information")
    col1, col2 = st.columns(2)
    with col1:
        full_name = st.text_input("Full Name", placeholder="e.g., Jane Doe")
        email = st.text_input("Email Address", placeholder="e.g., jane.doe@email.com")
    with col2:
        phone = st.text_input("Phone Number", placeholder="e.g., +1 123-456-7890")
        linkedin = st.text_input("LinkedIn Profile URL", placeholder="e.g., linkedin.com/in/janedoe")

    st.header("2. Target Role")
    job_spec = st.text_input("What job or internship are you applying for?", placeholder="e.g., Software Development Intern, Data Analyst")

    st.header("3. Work Experience")
    for i, exp in enumerate(st.session_state.experience):
        st.markdown(f"---")
        st.subheader(f"Experience #{i+1}")
        exp['title'] = st.text_input(f"Job Title", key=f"title_{i}", placeholder="e.g., Software Engineer")
        exp['company'] = st.text_input(f"Company", key=f"company_{i}", placeholder="e.g., Tech Solutions Inc.")
        col_exp1, col_exp2 = st.columns(2)
        with col_exp1:
            exp['location'] = st.text_input(f"Location", key=f"location_{i}", placeholder="e.g., San Francisco, CA")
        with col_exp2:
            exp['dates'] = st.text_input(f"Dates of Employment", key=f"dates_{i}", placeholder="e.g., May 2022 - Present")
        exp['responsibilities'] = st.text_area(f"Key Responsibilities & Achievements (one per line)", key=f"resp_{i}", placeholder="e.g., Developed a new feature that increased user engagement by 15%")
    
    st.header("4. Education")
    for i, edu in enumerate(st.session_state.education):
        st.markdown(f"---")
        st.subheader(f"Education #{i+1}")
        edu['institution'] = st.text_input(f"Institution", key=f"inst_{i}", placeholder="e.g., University of Technology")
        edu['degree'] = st.text_input(f"Degree/Certificate", key=f"degree_{i}", placeholder="e.g., Bachelor of Science in Computer Science")
        edu['grad_date'] = st.text_input(f"Graduation Date", key=f"grad_date_{i}", placeholder="e.g., May 2024")

    st.header("5. Skills")
    skills = st.text_area("List your key skills (comma-separated)", placeholder="e.g., Python, SQL, Machine Learning, Project Management, Public Speaking")

    # --- Form Submission ---
    submitted = st.form_submit_button("✨ Generate My Resume")

# --- Buttons for adding dynamic content ---
col_btn1, col_btn2 = st.columns(2)
with col_btn1:
    st.button("Add another experience", on_click=add_experience, use_container_width=True)
with col_btn2:
    st.button("Add another education", on_click=add_education, use_container_width=True)


# --- AI Generation and Resume Display ---
if submitted:
    if not full_name or not email or not job_spec:
        st.error("Please fill in at least your Name, Email, and Target Role.")
    else:
        with st.spinner("🤖 AI is crafting your professional summary... Please wait."):
            try:
                # Compile all user data into a single string for the prompt
                experience_str = "\n".join([f"- {exp['title']} at {exp['company']}: {exp['responsibilities']}" for exp in st.session_state.experience if exp['title']])
                education_str = "\n".join([f"- {edu['degree']} from {edu['institution']}" for edu in st.session_state.education if edu['degree']])

                prompt = f"""
                Based on the following information, write a compelling and professional summary for a resume.
                The summary should be concise (3-4 sentences), tailored for a '{job_spec}' position, and highlight the candidate's key strengths.

                **Candidate Information:**
                - **Target Role:** {job_spec}
                - **Experience:** {experience_str}
                - **Education:** {education_str}
                - **Skills:** {skills}

                Generate only the professional summary text, without any introductory phrases like "Here is the summary:".
                """

                response = model.generate_content(prompt)
                ai_summary = response.text.strip()
                
                # Store all data in session state for PDF generation
                st.session_state.resume_data = {
                    'full_name': full_name,
                    'email': email,
                    'phone': phone,
                    'linkedin': linkedin,
                    'summary': ai_summary,
                    'experience': st.session_state.experience,
                    'education': st.session_state.education,
                    'skills': skills
                }

            except Exception as e:
                st.error(f"An error occurred while communicating with the AI. Please check your API key and try again. Error: {e}")
                st.session_state.resume_data = None # Reset data on error


# --- Display Generated Resume and Download Button ---
if 'resume_data' in st.session_state and st.session_state.resume_data:
    st.balloons()
    st.header("🎉 Your Resume is Ready!")

    resume_data = st.session_state.resume_data
    
    # Display Resume on Screen
    st.markdown(f"## {resume_data['full_name']}")
    st.markdown(f"📧 {resume_data['email']} | 📞 {resume_data['phone']} | 🔗 [{resume_data['linkedin']}]({resume_data['linkedin']})")
    
    st.markdown("---")
    st.subheader("Professional Summary")
    st.markdown(resume_data['summary'])

    # Filter out empty entries before displaying
    valid_experience = [exp for exp in resume_data['experience'] if exp['title']]
    if valid_experience:
        st.subheader("Work Experience")
        for exp in valid_experience:
            st.markdown(f"**{exp['title']}** | {exp['company']}")
            st.markdown(f"*{exp['dates']}*")
            st.markdown(exp['responsibilities'])
    
    valid_education = [edu for edu in resume_data['education'] if edu['degree']]
    if valid_education:
        st.subheader("Education")
        for edu in valid_education:
            st.markdown(f"**{edu['degree']}** | {edu['institution']}")
            st.markdown(f"*{edu['grad_date']}*")

    if resume_data['skills']:
        st.subheader("Skills")
        st.markdown(resume_data['skills'])

    # PDF Download Button
    st.markdown("---")
    st.subheader("Download Your Resume")
    pdf_buffer = create_resume_pdf(resume_data)
    st.download_button(
        label="📥 Download as PDF",
        data=pdf_buffer,
        file_name=f"{resume_data['full_name'].replace(' ', '_')}_Resume.pdf",
        mime="application/pdf"
    )

st.sidebar.markdown("---")
st.sidebar.info("This is an AI-powered application. Always review the generated content for accuracy.")