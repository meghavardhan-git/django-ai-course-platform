import google.generativeai as genai
import os
import json
import re

# Read API key from environment variable
api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-1.5-flash")

def ask_gemini(prompt):
    response = model.generate_content(prompt)
    return response.text

def ask_gemini_suggestions(user_input):
    prompt = f"""
    Act as a course recommendation assistant.
    The user is interested in: "{user_input}". 
    Available categories: Python, DSA, Web Development, AI.

    Suggest 3 courses ONLY in strict JSON format like:
    [
      {{"title": "Python Beginner", "category": "Python", "difficulty": "Beginner", "description": "Introductory Python."}}
    ]
    """

    response = model.generate_content(prompt)

    try:
        match = re.search(r'\[.*\]', response.text, re.DOTALL)
        if match:
            return json.loads(match.group())
    except Exception as e:
        print("Parsing error:", e)

    return []
