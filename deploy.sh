#!/bin/bash

echo "🚀 Cold Email Generator - Quick Deploy Script"
echo "=============================================="
echo ""

# Check if git is initialized
if [ ! -d ".git" ]; then
    echo "📦 Initializing git repository..."
    git init
    git add .
    git commit -m "Initial commit - Cold Email Generator"
    echo "✅ Git repository initialized"
    echo ""
fi

echo "🌐 Ready to deploy! Here's what you need to do:"
echo ""
echo "1️⃣ BACKEND DEPLOYMENT (Render):"
echo "   - Go to https://render.com"
echo "   - Sign up and create new Web Service"
echo "   - Connect your GitHub repo"
echo "   - Configure:"
echo "     • Name: cold-email-generator-api"
echo "     • Root Directory: backend"
echo "     • Build Command: pip install -r requirements.txt"
echo "     • Start Command: uvicorn main:app --host 0.0.0.0 --port 10000"
echo "   - Add Environment Variable: OPENAI_API_KEY = your API key"
echo "   - Deploy and get your backend URL"
echo ""

echo "2️⃣ FRONTEND DEPLOYMENT (Netlify):"
echo "   - Go to https://netlify.com"
echo "   - Drag and drop the 'frontend' folder"
echo "   - Get your frontend URL"
echo ""

echo "3️⃣ UPDATE API URL:"
echo "   - Edit frontend/script.js"
echo "   - Change line 2 to your Render backend URL"
echo ""

echo "4️⃣ SET UP GUMROAD:"
echo "   - Go to https://gumroad.com"
echo "   - Create product: 'Pro Cold Email Bundle'"
echo "   - Price: $5"
echo "   - Update the link in frontend/index.html"
echo ""

echo "5️⃣ LAUNCH & PROMOTE:"
echo "   - Test your live site"
echo "   - Share on social media"
echo "   - Post on Product Hunt, Reddit, etc."
echo ""

echo "💰 REVENUE PROJECTIONS:"
echo "   • Conservative: $300-450/month"
echo "   • Optimistic: $1,500-2,250/month"
echo ""

echo "⚡ Quick commands:"
echo "   • Test API: python test_api.py"
echo "   • Open frontend: open frontend/index.html"
echo "   • View logs: tail -f backend/logs/app.log"
echo ""

echo "🎯 Next steps:"
echo "   1. Deploy backend to Render"
echo "   2. Deploy frontend to Netlify"
echo "   3. Set up Gumroad product"
echo "   4. Launch and start making money!"
echo ""

echo "Good luck! 🚀💰" 