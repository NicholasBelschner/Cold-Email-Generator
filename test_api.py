#!/usr/bin/env python3
"""
Simple test script for the Cold Email Generator API
"""

import requests
import json
import sys

def test_api():
    """Test the API endpoints"""
    
    base_url = "http://localhost:8000"
    
    print("🧪 Testing Cold Email Generator API...")
    print(f"📍 Testing against: {base_url}")
    print()
    
    # Test 1: Health check
    print("1️⃣ Testing health check...")
    try:
        response = requests.get(f"{base_url}/health")
        if response.status_code == 200:
            print("✅ Health check passed")
            print(f"   Response: {response.json()}")
        else:
            print(f"❌ Health check failed: {response.status_code}")
            return False
    except requests.exceptions.ConnectionError:
        print("❌ Could not connect to API. Is the server running?")
        print("   Run: cd backend && uvicorn main:app --reload")
        return False
    except Exception as e:
        print(f"❌ Health check error: {e}")
        return False
    
    print()
    
    # Test 2: Generate email
    print("2️⃣ Testing email generation...")
    
    test_data = {
        "company_name": "TechFlow Solutions",
        "target_industry": "SaaS",
        "goal": "Sales",
        "product_description": "We provide AI-powered workflow automation software that helps teams save 10+ hours per week.",
        "tone": "Professional"
    }
    
    try:
        response = requests.post(
            f"{base_url}/generate-email",
            headers={"Content-Type": "application/json"},
            json=test_data
        )
        
        if response.status_code == 200:
            result = response.json()
            print("✅ Email generation passed")
            print(f"   Generated email length: {len(result.get('email', ''))} characters")
            print()
            print("📧 Generated email preview:")
            print("-" * 50)
            email_content = result.get('email', '')
            # Show first 200 characters
            preview = email_content[:200] + "..." if len(email_content) > 200 else email_content
            print(preview)
            print("-" * 50)
        else:
            print(f"❌ Email generation failed: {response.status_code}")
            print(f"   Response: {response.text}")
            return False
            
    except Exception as e:
        print(f"❌ Email generation error: {e}")
        return False
    
    print()
    print("🎉 All tests passed! Your API is working correctly.")
    print()
    print("💡 Next steps:")
    print("   1. Open frontend/index.html in your browser")
    print("   2. Fill out the form and test the full application")
    print("   3. Deploy to production when ready")
    
    return True

if __name__ == "__main__":
    success = test_api()
    sys.exit(0 if success else 1) 