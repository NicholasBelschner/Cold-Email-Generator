from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from prompt_builder import build_prompt
from openai import OpenAI
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Create FastAPI app
app = FastAPI(
    title="Cold Email Generator API",
    description="Generate tailored cold emails using GPT-4o",
    version="1.0.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify your frontend domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Request model
class EmailRequest(BaseModel):
    company_name: str
    target_industry: str
    goal: str
    product_description: str
    tone: str

# Response model
class EmailResponse(BaseModel):
    email: str
    success: bool = True

@app.get("/")
async def root():
    """Health check endpoint"""
    return {"message": "Cold Email Generator API is running!"}

@app.post("/generate-email", response_model=EmailResponse)
async def generate_email(req: EmailRequest):
    """
    Generate a cold email based on the provided parameters
    """
    try:
        # Validate OpenAI API key
        if not os.getenv("OPENAI_API_KEY"):
            raise HTTPException(status_code=500, detail="OpenAI API key not configured")
        
        # Build the prompt
        prompt = build_prompt(
            req.company_name,
            req.target_industry,
            req.goal,
            req.product_description,
            req.tone
        )
        
        # Call OpenAI API
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
            max_tokens=500
        )
        
        # Extract the generated email
        email_content = response.choices[0].message.content.strip()
        
        return EmailResponse(email=email_content)
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating email: {str(e)}")

@app.get("/health")
async def health_check():
    """Health check endpoint for deployment monitoring"""
    return {"status": "healthy", "service": "cold-email-generator"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000) 