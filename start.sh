#!/bin/bash

# Cold Email Generator Startup Script

echo "🚀 Starting Cold Email Generator..."

# Check if we're in the right directory
if [ ! -f "backend/main.py" ]; then
    echo "❌ Error: Please run this script from the project root directory"
    exit 1
fi

# Check if virtual environment exists
if [ ! -d "backend/venv" ]; then
    echo "📦 Creating virtual environment..."
    cd backend
    python3 -m venv venv
    cd ..
fi

# Activate virtual environment
echo "🔧 Activating virtual environment..."
source backend/venv/bin/activate

# Install dependencies
echo "📥 Installing dependencies..."
cd backend
pip install -r requirements.txt
cd ..

# Check if .env file exists
if [ ! -f "backend/.env" ]; then
    echo "⚠️  Warning: No .env file found in backend directory"
    echo "📝 Please create backend/.env with your OpenAI API key:"
    echo "   OPENAI_API_KEY=your_api_key_here"
    echo ""
    echo "💡 You can copy from env.example:"
    echo "   cp backend/env.example backend/.env"
    echo ""
fi

# Start the server
echo "🌐 Starting FastAPI server..."
echo "📍 Backend will be available at: http://localhost:8000"
echo "🌍 Frontend: Open frontend/index.html in your browser"
echo "📚 API docs: http://localhost:8000/docs"
echo ""
echo "Press Ctrl+C to stop the server"
echo ""

cd backend
uvicorn main:app --reload --host 0.0.0.0 --port 8000 