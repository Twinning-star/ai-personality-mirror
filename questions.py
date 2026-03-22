import requests

GEMINI_API_KEY = "AIzaSyD5TXI9a4Dph1_AHOhBbEMVjhRUWFnKxeU"
GEMINI_URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={GEMINI_API_KEY}"

def ask_gemini(prompt):
    response = requests.post(
        GEMINI_URL,
        json={
            "contents": [
                {"parts": [{"text": prompt}]}
            ]
        }
    )
    result = response.json()

    if "candidates" not in result:
        print("Gemini Error:", result)
        return "Error getting response"

    return result["candidates"][0]["content"]["parts"][0]["text"]

def generate_question(previous_answers):
    context = "\n".join(previous_answers) if previous_answers else "No answers yet"

    prompt = f"""
    Previous answers: {context}
    
    Write a NEW personality test question. 
    
    STRICT RULES:
    - NEVER repeat a previous scenario
    - Each question must be about a DIFFERENT situation
    - SCENARIO must be EXACTLY 1 sentence
    - Options must be EXACTLY 3 words each
    - Use ONLY simple common words
    - Be creative, pick different places each time like: forest, school, space, ocean, dream, street, house, etc.
    
    Example of good format:
    SCENARIO: You see a strange door in your room.
    A) Open it now
    B) Walk away fast
    C) Call for help
    D) Break it down
    
    Now write ONE completely new and different question in that exact style.
    """

    return ask_gemini(prompt)
