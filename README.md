# 🤖 AI-Powered Resume & Portfolio Builder

A streamlined web application that uses artificial intelligence to generate professional resumes in minutes. Simply fill in your information, and let the AI craft a compelling professional summary tailored to your target role.

## ✨ Features

- **AI-Powered Summary Generation**: Uses Google's Gemini 2.5 Flash model to create personalized professional summaries based on your background and target role
- **Dynamic Form Handling**: Easily add multiple work experiences and education entries with an intuitive interface
- **Professional PDF Export**: Generate beautifully formatted PDF resumes ready for job applications
- **Real-Time Form Validation**: Ensures all essential information is provided before generating your resume
- **Responsive Design**: Built with Streamlit for a clean, mobile-friendly user experience
- **Secure API Configuration**: Uses Streamlit's secrets management for safe API key handling

## 🚀 Getting Started

### Prerequisites

Before you begin, ensure you have the following installed:
- **Python 3.8** or higher
- **pip** (Python package manager)
- A **Google AI API Key** (obtain from [Google AI Studio](https://aistudio.google.com/app/apikeys))

### Installation

1. **Clone the Repository** (or download the project files)
   ```bash
   git clone <repository-url>
   cd ai-resume-builder
   ```

2. **Create a Virtual Environment** (optional but recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Required Dependencies**
   ```bash
   pip install -r requirements.txt
   ```
   
   Or install manually:
   ```bash
   pip install streamlit google-generativeai reportlab
   ```

4. **Set Up Your Google API Key**

   **For Local Development:**
   - Create a `.streamlit` directory in your project folder (if it doesn't exist)
   - Create a `secrets.toml` file inside the `.streamlit` directory
   - Add your Google API Key:
     ```toml
     GOOGLE_API_KEY = "YOUR_API_KEY_HERE"
     ```

   **For Streamlit Cloud Deployment:**
   - Go to your app's settings on Streamlit Cloud
   - Navigate to the "Secrets" section
   - Add your API key in the format above

## 📖 Usage

1. **Run the Application**
   ```bash
   streamlit run AI-Resume-and-Portfolio-builder.py
   ```
   The app will open in your default browser at `http://localhost:8501`

2. **Fill in Your Information**
   - **Personal Information**: Full name, email, phone, and LinkedIn profile URL
   - **Target Role**: Specify the job or internship position you're applying for
   - **Work Experience**: Add details about your previous roles (job title, company, location, dates, and key achievements)
   - **Education**: Include your degrees, institutions, and graduation dates
   - **Skills**: List your technical and professional skills (comma-separated)

3. **Generate Your Resume**
   - Click the **"✨ Generate My Resume"** button
   - The AI will create a professional summary tailored to your target role
   - Review the generated resume on the screen

4. **Download Your Resume**
   - Click the **"📥 Download as PDF"** button to save your resume as a PDF file
   - The file will be named with your full name (e.g., `Jane_Doe_Resume.pdf`)

## 🔧 Technical Details

### Architecture

- **Frontend**: Streamlit (Python web framework)
- **AI Model**: Google Generative AI (Gemini 2.5 Flash)
- **PDF Generation**: ReportLab library
- **Session Management**: Streamlit session state for dynamic form handling

### Key Components

#### 1. **API Configuration**
   - Securely loads the Google API key from Streamlit secrets
   - Initializes the Gemini model for content generation
   - Provides helpful error messages if the API key is missing

#### 2. **PDF Generation Function** (`create_resume_pdf`)
   - Creates professional PDF documents with custom styling
   - Includes sections for name, contact info, professional summary, experience, education, and skills
   - Uses navy blue headers for visual appeal
   - Formats bullet points for better readability

#### 3. **Dynamic Form Handling**
   - Allows users to add unlimited work experiences and education entries
   - Uses Streamlit's session state to maintain form data across reruns
   - Initializes with one blank entry for better user experience

#### 4. **AI Prompt Engineering**
   - Crafts a detailed prompt that provides context about the candidate
   - Includes target role, experience, education, and skills
   - Requests a concise, professional summary (3-4 sentences)
   - Instructs the AI to avoid introductory phrases for cleaner output

### File Structure

```
ai-resume-builder/
├── AI-Resume-and-Portfolio-builder.py  # Main application file
├── requirements.txt                     # Python dependencies
├── .streamlit/
│   └── secrets.toml                     # API key configuration (local only)
└── README.md                            # This file
```

## 📋 Requirements

```
streamlit==1.40.0
google-generativeai==0.8.3
reportlab==4.2.0
```

## 🛡️ Security Best Practices

- **Never commit your API key** to version control
- Keep `.streamlit/secrets.toml` in your `.gitignore`
- For production deployments, use Streamlit Cloud's secrets management
- Always review AI-generated content for accuracy and relevance
- Do not share your API key or expose it in public repositories

## 🎯 Use Cases

- **Job Seekers**: Quickly generate resumes tailored to specific job postings
- **Career Changers**: Craft professional summaries that highlight transferable skills
- **Freelancers**: Create multiple versions of resumes for different client types
- **Students**: Build polished resumes for internship applications
- **Professionals**: Update existing resumes with AI-enhanced professional summaries

## ⚠️ Important Notes

1. **AI Content Review**: Always review the AI-generated professional summary for accuracy and relevance. The AI may make assumptions or include information that needs adjustment.

2. **API Rate Limits**: Google Generative AI has rate limits. Check your quota to avoid service interruptions.

3. **Customization**: Feel free to modify the resume styling, prompts, and sections to match your preferences.

4. **Contact Information**: Ensure all contact details are accurate before downloading your resume.

## 🚀 Deployment

### Deploy to Streamlit Cloud

1. Push your code to GitHub
2. Connect your GitHub account to Streamlit Cloud
3. Create a new app and select your repository
4. Add your `GOOGLE_API_KEY` in the Secrets section
5. Deploy!

### Deploy to Other Platforms

For deployment to AWS, Heroku, or other platforms, ensure:
- Environment variables are properly configured
- Dependencies are installed from `requirements.txt`
- The application runs on the correct port (default: 8501 for Streamlit)

## 🐛 Troubleshooting

### Issue: "Google AI API key not found"
- **Solution**: Ensure your `.streamlit/secrets.toml` file is created with the correct API key format

### Issue: "ModuleNotFoundError"
- **Solution**: Install all dependencies with `pip install -r requirements.txt`

### Issue: PDF Download Button Not Working
- **Solution**: Check your browser's download settings or try a different browser

### Issue: AI Summary Generation Fails
- **Solution**: Verify your Google API key is valid and has appropriate permissions

## 📞 Support & Feedback

For issues, feature requests, or suggestions:
1. Check existing GitHub issues
2. Provide detailed error messages and steps to reproduce
3. Include your Python version and Streamlit version (`streamlit --version`)

## 📄 License

This project is provided as-is for educational and professional use. Modify and distribute as needed for your organization.

## 🤝 Contributing

Contributions are welcome! Feel free to fork the repository, make improvements, and submit pull requests.

## 📚 Learning Resources

- [Streamlit Documentation](https://docs.streamlit.io/)
- [Google Generative AI API](https://ai.google.dev/)
- [ReportLab Documentation](https://www.reportlab.com/)
- [Python Best Practices](https://pep8.org/)

---

**Happy Resume Building! 🎉**

Create professional resumes that stand out and land you your dream job!