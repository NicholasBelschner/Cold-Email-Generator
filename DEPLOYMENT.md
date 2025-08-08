# Deployment Guide

## Local Development Setup

### 1. Backend Setup

```bash
# Navigate to backend directory
cd backend

# Create virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Create environment file
cp env.example .env
# Edit .env and add your OpenAI API key

# Run the server
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

### 2. Frontend Setup

```bash
# Navigate to frontend directory
cd frontend

# Open index.html in your browser
# Or serve with a local server:
python -m http.server 3000
```

## Production Deployment

### Option 1: Render (Recommended)

#### Backend Deployment

1. **Create Render Account**
   - Go to [render.com](https://render.com)
   - Sign up with GitHub

2. **Deploy Backend**
   - Click "New Web Service"
   - Connect your GitHub repository
   - Configure:
     - **Name**: `cold-email-generator-api`
     - **Environment**: Python 3
     - **Build Command**: `pip install -r requirements.txt`
     - **Start Command**: `uvicorn main:app --host 0.0.0.0 --port 10000`
     - **Root Directory**: `backend`

3. **Environment Variables**
   - Add in Render dashboard:
     - `OPENAI_API_KEY`: Your OpenAI API key

#### Frontend Deployment

1. **Deploy to Netlify**
   - Go to [netlify.com](https://netlify.com)
   - Drag and drop the `frontend` folder
   - Or connect GitHub repository

2. **Update API URL**
   - Edit `frontend/script.js`
   - Change `API_BASE_URL` to your Render backend URL

### Option 2: Vercel + Render

#### Frontend on Vercel
1. Go to [vercel.com](https://vercel.com)
2. Import your GitHub repository
3. Set root directory to `frontend`
4. Deploy

#### Backend on Render
- Same as Option 1

### Option 3: GitHub Pages + Render

#### Frontend on GitHub Pages
1. Push code to GitHub
2. Go to repository Settings > Pages
3. Set source to `frontend` directory
4. Deploy

## Environment Variables

### Required
- `OPENAI_API_KEY`: Your OpenAI API key

### Optional
- `PORT`: Server port (default: 8000)
- `HOST`: Server host (default: 0.0.0.0)
- `ALLOWED_ORIGINS`: CORS origins for production

## API Endpoints

- `GET /`: Health check
- `GET /health`: Health check for monitoring
- `POST /generate-email`: Generate cold email

## Monitoring

### Health Checks
- Backend: `https://your-backend-url.onrender.com/health`
- Should return: `{"status": "healthy", "service": "cold-email-generator"}`

### Logs
- Render: View logs in dashboard
- Monitor for errors and API usage

## Troubleshooting

### Common Issues

1. **CORS Errors**
   - Ensure CORS middleware is configured
   - Check `ALLOWED_ORIGINS` in production

2. **OpenAI API Errors**
   - Verify API key is correct
   - Check API usage limits

3. **Frontend Can't Connect to Backend**
   - Verify API URL in `script.js`
   - Check if backend is running
   - Test with curl: `curl -X POST https://your-backend-url.onrender.com/generate-email`

### Performance Optimization

1. **Backend**
   - Use async/await for API calls
   - Implement request caching
   - Monitor OpenAI API usage

2. **Frontend**
   - Minify CSS/JS for production
   - Use CDN for fonts
   - Implement loading states

## Security Considerations

1. **API Keys**
   - Never commit `.env` files
   - Use environment variables in production
   - Rotate keys regularly

2. **CORS**
   - Restrict origins in production
   - Use specific domains, not wildcards

3. **Rate Limiting**
   - Consider implementing rate limiting
   - Monitor for abuse

## Cost Optimization

1. **OpenAI API**
   - Monitor usage in OpenAI dashboard
   - Set up billing alerts
   - Consider caching responses

2. **Hosting**
   - Render free tier: 750 hours/month
   - Vercel free tier: 100GB bandwidth
   - Netlify free tier: 100GB bandwidth

## Scaling Considerations

1. **Traffic Spikes**
   - Monitor Render usage
   - Consider paid plans for higher limits

2. **API Limits**
   - Implement request queuing
   - Add retry logic for failed requests

3. **Database** (Future)
   - Consider adding user accounts
   - Store email history
   - Analytics tracking 