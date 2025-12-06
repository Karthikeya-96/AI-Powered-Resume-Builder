# 🤖 AI-Powered Resume & Portfolio Builder

A streamlined web application that uses artificial intelligence to generate professional resumes in minutes. Simply fill in your information, and let the AI craft a compelling professional summary tailored to your target role.

## ✨ Features

- **AI-Powered Summary Generation**: Uses Google's Gemini 2.5 Flash model to create personalized professional summaries based on your background and target role
- **Dynamic Form Handling**: Easily add multiple work experiences and education entries with an intuitive interface
- **Professional PDF Export**: Generate beautifully formatted PDF resumes ready for job applications
- **Real-Time Form Validation**: Ensures all essential information is provided before generating your resume
- **Responsive Design**: Built with Streamlit for a clean, mobile-friendly user experience
- **Secure API Configuration**: Uses Streamlit's secrets management for safe API key handling

## 🚀 Quick Start

### Prerequisites

- **Python 3.8** or higher
- **pip** (Python package manager)
- A **Google AI API Key** (get it from [Google AI Studio](https://aistudio.google.com/app/apikeys))

### Local Installation & Setup

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/ai-resume-builder.git
   cd ai-resume-builder
   ```

2. **Create a Virtual Environment** (recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Your Google API Key**
   
   Create `.streamlit/secrets.toml` in your project root:
   ```toml
   GOOGLE_API_KEY = "YOUR_API_KEY_HERE"
   ```
   
   ⚠️ **IMPORTANT**: This file is in `.gitignore` and should NEVER be committed to GitHub.

5. **Run the Application**
   ```bash
   streamlit run AI-Resume-and-Portfolio-builder.py
   ```
   
   Open your browser to `http://localhost:8501`

## 📖 How to Use

1. **Fill in Your Information**
   - Personal details (name, email, phone, LinkedIn)
   - Target job/internship position
   - Work experience (add multiple entries if needed)
   - Education details
   - Professional skills

2. **Generate Your Resume**
   - Click **"✨ Generate My Resume"**
   - AI creates a tailored professional summary

3. **Download as PDF**
   - Click **"📥 Download as PDF"** button
   - Your resume is ready to submit!

## 📁 Project Structure

```
ai-resume-builder/
├── AI-Resume-and-Portfolio-builder.py  # Main application
├── requirements.txt                     # Python dependencies
├── README.md                            # This file
├── .gitignore                           # Git ignore rules
└── .streamlit/                          # Streamlit config (local only)
    └── secrets.toml                     # API key (DO NOT COMMIT)
```

## 📦 Dependencies

```txt
streamlit>=1.40.0
google-generativeai>=0.8.3
reportlab>=4.2.0
```

## 🔐 Security & GitHub Best Practices

### Never Commit secrets.toml

Your `.gitignore` file already excludes sensitive files:

```gitignore
# Streamlit secrets (contains API keys)
.streamlit/secrets.toml

# Environment files
.env
.env.local
.env.*.local
```

**Why this matters:**
- Your API key becomes public if committed to GitHub
- Anyone can use your API quota (and your billing account)
- Google may suspend your API key
- You'd need to regenerate a new key

### Safe API Key Management

**For Local Development:**
- Keep `secrets.toml` on your local machine only
- Add it to `.gitignore` (already done)
- Never add it to git

**For Streamlit Cloud Deployment:**
1. Push your code to GitHub
2. Connect your GitHub repo to Streamlit Cloud
3. Add API key in **App Settings → Secrets** tab
4. Streamlit Cloud will securely store and inject the secret

## ☁️ Deployment on Streamlit Cloud

1. **Push to GitHub** (without secrets.toml)
   ```bash
   git add .
   git commit -m "Initial commit"
   git push origin main
   ```

2. **Deploy to Streamlit Cloud**
   - Go to [share.streamlit.io](https://share.streamlit.io)
   - Connect your GitHub account
   - Select this repository
   - Choose the main branch and `AI-Resume-and-Portfolio-builder.py` as the entry point

3. **Add Secrets**
   - In the app settings, go to **Secrets**
   - Add your Google API Key:
     ```
     GOOGLE_API_KEY = "YOUR_API_KEY_HERE"
     ```
   - Save and the app will redeploy automatically

## 🔧 Technical Details

### Architecture
- **Frontend**: Streamlit web framework
- **AI Model**: Google Generative AI (Gemini 2.5 Flash)
- **PDF Generation**: ReportLab library
- **State Management**: Streamlit session state

### Key Components

**PDF Generation** (`create_resume_pdf`):
- Creates professional, formatted PDF documents
- Custom styling with navy blue headers
- Bullet-point formatting for achievements
- Clean, readable layout

**Dynamic Forms**:
- Add unlimited work experiences
- Add unlimited education entries
- Real-time validation
- Streamlit session state management

**AI Integration**:
- Crafts detailed prompts with user context
- Generates concise 3-4 sentence summaries
- Tailored to target job position
- Professional tone and structure

## ⚙️ Configuration

### Streamlit Configuration (Optional)

Edit `.streamlit/config.toml` for additional customization:

```toml
[theme]
primaryColor = "#1f77b4"
backgroundColor = "#ffffff"
secondaryBackgroundColor = "#f0f2f6"
textColor = "#262730"

[server]
maxUploadSize = 200
```

## 🎯 Use Cases

- **Job Seekers**: Generate tailored resumes for specific positions
- **Career Changers**: Highlight transferable skills effectively
- **Students**: Create polished resumes for internships
- **Freelancers**: Multiple resume versions for different clients
- **Professionals**: Keep resumes updated with AI enhancements

## 🐛 Troubleshooting

| Issue | Solution |
|-------|----------|
| "Google AI API key not found" | Ensure `.streamlit/secrets.toml` exists with correct API key |
| "ModuleNotFoundError" | Run `pip install -r requirements.txt` |
| App won't start locally | Check Python version (3.8+), verify virtual environment activated |
| PDF download fails | Try different browser, check firewall settings |
| AI generation fails | Verify API key validity, check rate limits |

## 📋 Development Tips

### Running in Development Mode
```bash
streamlit run AI-Resume-and-Portfolio-builder.py --logger.level=debug
```

### Clearing Cache
```bash
streamlit cache clear
```

### Testing Locally
1. Fill test data in the form
2. Verify AI generation works
3. Test PDF download
4. Check all sections display correctly

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/improvement`)
3. Commit changes (`git commit -m 'Add improvement'`)
4. Push to branch (`git push origin feature/improvement`)
5. Open a Pull Request

## 📝 License

This project is open source and available under the MIT License.

## 📚 Resources

- [Streamlit Documentation](https://docs.streamlit.io/)
- [Google Generative AI API](https://ai.google.dev/)
- [ReportLab Docs](https://www.reportlab.com/docs/reportlab-userguide.pdf)
- [Streamlit Cloud Deployment](https://docs.streamlit.io/streamlit-community-cloud/get-started)

## ⚠️ Important Notes

1. **Always Review AI Output**: Verify the generated summary for accuracy and relevance
2. **API Rate Limits**: Google Generative AI has usage quotas - monitor your usage
3. **Contact Information**: Double-check all contact details before downloading
4. **Regular Updates**: Keep dependencies updated for security patches

---

## Quick Command Reference

```bash
# Setup
git clone <repo-url>
cd ai-resume-builder
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Create secrets file
mkdir -p .streamlit
echo 'GOOGLE_API_KEY = "your-key"' > .streamlit/secrets.toml

# Run locally
streamlit run AI-Resume-and-Portfolio-builder.py

# Deploy to Streamlit Cloud
git add .
git commit -m "Ready for deployment"
git push origin main
```

---

**🎉 Ready to build amazing resumes!**

Have questions? Check the troubleshooting section or open an issue on GitHub.