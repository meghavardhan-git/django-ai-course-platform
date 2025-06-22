import google.generativeai as genai
import json
import re

# API KEY (use your actual API key here)
api_key = "AIzaSyDDL2-CRfil41T4n8rr9YCpXKieWOd6hVI"
genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-1.5-flash")

# Normal chat
def ask_gemini(prompt):
    response = model.generate_content(prompt)
    return response.text

# AI Course Suggestion
def ask_gemini_suggestions(user_input):
    prompt = f"""
    Act as a course recommendation assistant.
    The user says: "{user_input}".
    Available categories: Python, DSA, Web Development, AI.
    Suggest 3 courses in strict JSON like:
    [
      {{"title": "Python Beginner", "category": "Python", "difficulty": "Beginner", "description": "Introductory Python."}},
      ...
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
