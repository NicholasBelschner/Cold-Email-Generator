# Quick Start Guide

## 🚀 Get Running in 5 Minutes

### Prerequisites
- Python 3.8+ installed
- OpenAI API key (get one at [openai.com](https://openai.com))

### Step 1: Setup Environment
```bash
# Copy environment template
cp backend/env.example backend/.env

# Edit backend/.env and add your OpenAI API key
OPENAI_API_KEY=sk-your-api-key-here
```

### Step 2: Start the Application

**On Mac/Linux:**
```bash
./start.sh
```

**On Windows:**
```bash
start.bat
```

**Manual (if scripts don't work):**
```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload
```

### Step 3: Test the Application

1. **Open frontend**: Navigate to `frontend/index.html` in your browser
2. **Test API**: Run `python test_api.py` to verify backend is working
3. **Generate emails**: Fill out the form and click "Generate Cold Email"

## 📁 Project Structure

```
cold-email-generator/
├── backend/                 # FastAPI server
│   ├── main.py             # Main application
│   ├── prompt_builder.py   # GPT prompt logic
│   ├── requirements.txt    # Python dependencies
│   └── env.example        # Environment template
├── frontend/               # Static website
│   ├── index.html         # Main page
│   ├── styles.css         # Styling
│   └── script.js          # Frontend logic
├── start.sh               # Mac/Linux startup script
├── start.bat              # Windows startup script
├── test_api.py            # API testing script
└── README.md              # Full documentation
```

## 🔧 Configuration

### Environment Variables
- `OPENAI_API_KEY`: Your OpenAI API key (required)

### API Endpoints
- `GET /health`: Health check
- `POST /generate-email`: Generate cold email

### Frontend Configuration
Edit `frontend/script.js` to change the API URL:
```javascript
// For local development
API_BASE_URL = 'http://localhost:8000'

// For production (after deployment)
API_BASE_URL = 'https://your-backend-url.onrender.com'
```

## 🚀 Deployment

### Quick Deploy to Render
1. Push code to GitHub
2. Go to [render.com](https://render.com)
3. Create new Web Service
4. Connect your GitHub repo
5. Set root directory to `backend`
6. Add environment variable: `OPENAI_API_KEY`
7. Deploy!

### Frontend Deployment
- **Netlify**: Drag `frontend` folder to [netlify.com](https://netlify.com)
- **Vercel**: Import repo and set root to `frontend`
- **GitHub Pages**: Enable Pages in repo settings

## 💰 Monetization Setup

1. **Create Gumroad Product**
   - Go to [gumroad.com](https://gumroad.com)
   - Create product: "Pro Cold Email Bundle"
   - Set price: $5
   - Get your product URL

2. **Update Frontend**
   - Edit `frontend/index.html`
   - Replace `https://your-gumroad-link.com` with your actual Gumroad URL

## 🐛 Troubleshooting

### Common Issues

**"Could not connect to API"**
- Make sure backend is running: `uvicorn main:app --reload`
- Check if port 8000 is available

**"OpenAI API error"**
- Verify your API key in `backend/.env`
- Check OpenAI account for usage limits

**"CORS error"**
- Backend CORS is configured for development
- For production, update `ALLOWED_ORIGINS` in `main.py`

### Testing
```bash
# Test API functionality
python test_api.py

# Check if server is running
curl http://localhost:8000/health
```

## 📈 Next Steps

1. **Customize the prompts** in `backend/prompt_builder.py`
2. **Add more email goals** in the frontend form
3. **Implement user accounts** for email history
4. **Add analytics** to track usage
5. **Create email templates** for different industries

## 💡 Tips

- **API Costs**: Monitor OpenAI usage in your dashboard
- **Performance**: Consider caching responses for repeated requests
- **Security**: Use environment variables, never commit API keys
- **Scaling**: Render free tier has 750 hours/month limit

## 🆘 Need Help?

- Check the full [README.md](README.md) for detailed documentation
- Review [DEPLOYMENT.md](DEPLOYMENT.md) for production setup
- Test with `python test_api.py` to verify functionality 