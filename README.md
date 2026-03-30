# VOUCH - Fact Checker AI Mainframe

A real-time AI-powered fact-checking application built with Streamlit and Google Generative AI.

## Features
- 🤖 Real-time fact verification using Google Gemini AI
- 🔍 Live web search integration
- 💬 Chat-based interface
- 🎨 Advanced cyberpunk UI design

## Prerequisites
- Python 3.8+
- Google API Key (from Google Cloud Console)

## Installation

### 1. Clone the repository
```bash
git clone <your-github-repo-url>
cd VOUCH
```

### 2. Create a virtual environment (optional but recommended)
```bash
python -m venv venv
venv\Scripts\activate  # On Windows
```

### 3. Install dependencies
```bash
pip install -r requirement.txt
```

### 4. Set up your API key
1. Get a Google API Key from [Google AI Studio](https://aistudio.google.com/app/apikey)
2. Copy `.streamlit/secrets.toml.example` to `.streamlit/secrets.toml`
3. Add your API key to `.streamlit/secrets.toml`:
```toml
API_KEY = "your_actual_api_key_here"
```

**IMPORTANT**: `.streamlit/secrets.toml` is in `.gitignore` - never commit it!

## Running the Application

### Using Streamlit (Recommended)
```bash
streamlit run vouch.py
```

### Using the batch file (Windows)
```bash
Launch_Vouch.bat
```

## Project Structure
```
VOUCH/
├── vouch.py                    # Main application
├── requirement.txt             # Python dependencies
├── Launch_Vouch.bat           # Windows batch launcher
├── .streamlit/
│   ├── secrets.toml           # ⚠️ DO NOT COMMIT (has .gitignore)
│   └── secrets.toml.example   # Template for setup
├── .gitignore                 # Git ignore rules
└── vouch_chat_history.json    # User chat history (auto-generated)
```

## Security Notes
⚠️ **Never commit these files to GitHub:**
- `.streamlit/secrets.toml` - Contains your API key
- `vouch_chat_history.json` - Contains user data

These are protected by `.gitignore`.

## Troubleshooting

### "API_KEY not found" error
- Ensure `.streamlit/secrets.toml` exists
- Verify the API key is correctly formatted
- Check that the file is in the `.streamlit/` directory

### Port already in use
Change the default port:
```bash
streamlit run vouch.py --server.port 8502
```

### Missing dependencies
Reinstall requirements:
```bash
pip install -r requirement.txt
```

## License
[Add your license here]

## Support
[Add contact/support information here]
