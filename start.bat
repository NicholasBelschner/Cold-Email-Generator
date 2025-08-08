@echo off
REM Cold Email Generator Startup Script for Windows

echo 🚀 Starting Cold Email Generator...

REM Check if we're in the right directory
if not exist "backend\main.py" (
    echo ❌ Error: Please run this script from the project root directory
    pause
    exit /b 1
)

REM Check if virtual environment exists
if not exist "backend\venv" (
    echo 📦 Creating virtual environment...
    cd backend
    python -m venv venv
    cd ..
)

REM Activate virtual environment
echo 🔧 Activating virtual environment...
call backend\venv\Scripts\activate.bat

REM Install dependencies
echo 📥 Installing dependencies...
cd backend
pip install -r requirements.txt
cd ..

REM Check if .env file exists
if not exist "backend\.env" (
    echo ⚠️  Warning: No .env file found in backend directory
    echo 📝 Please create backend\.env with your OpenAI API key:
    echo    OPENAI_API_KEY=your_api_key_here
    echo.
    echo 💡 You can copy from env.example:
    echo    copy backend\env.example backend\.env
    echo.
)

REM Start the server
echo 🌐 Starting FastAPI server...
echo 📍 Backend will be available at: http://localhost:8000
echo 🌍 Frontend: Open frontend\index.html in your browser
echo 📚 API docs: http://localhost:8000/docs
echo.
echo Press Ctrl+C to stop the server
echo.

cd backend
uvicorn main:app --reload --host 0.0.0.0 --port 8000 