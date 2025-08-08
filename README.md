# Cold Email Generator for Freelancers & Startups

A fast, simple tool that generates tailored cold emails using GPT-4o. Perfect for freelancers and startups looking to improve their outreach.

## Features

- 🎯 Goal-based email generation (Sales, Hiring, Fundraising, Partnership)
- 🎨 Multiple tone options (Professional, Casual, Bold)
- 💰 Freemium model with Gumroad integration
- 🚀 Zero upfront cost deployment
- ⚡ Fast API with FastAPI backend

## Tech Stack

- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Python FastAPI
- **AI**: OpenAI GPT-4o
- **Hosting**: Render (free tier)
- **Payments**: Gumroad

## Quick Start

### Local Development

1. **Setup Backend**
   ```bash
   cd backend
   pip install -r requirements.txt
   # Add your OpenAI API key to .env
   uvicorn main:app --reload
   ```

2. **Setup Frontend**
   - Open `frontend/index.html` in your browser
   - Or serve with a local server

### Environment Variables

Create `backend/.env`:
```
OPENAI_API_KEY=your_openai_api_key_here
```

## Deployment

### Backend (Render)
- Create new Web Service
- Connect GitHub repo
- Build command: `pip install -r requirements.txt`
- Start command: `uvicorn main:app --host 0.0.0.0 --port 10000`

### Frontend
- Deploy static files to Netlify, Vercel, or GitHub Pages
- Update API URL in `script.js` to point to your deployed backend

## Monetization

- Free: 1 email generation
- Pro ($5): 5 email variations + LinkedIn DM version
- Integrated with Gumroad for instant payments

## Project Structure

```
cold-email-generator/
├── backend/
│   ├── main.py
│   ├── prompt_builder.py
│   └── requirements.txt
├── frontend/
│   ├── index.html
│   ├── styles.css
│   └── script.js
└── README.md
```

## Future Features

- Save emails to PDF
- Email tracking
- User login system
- Mailchimp/SendGrid integration
- AI-generated subject lines 