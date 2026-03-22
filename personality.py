from questions import ask_gemini
def analyze_personality(all_answers):
    prompt = f"""
    Based on these answers: {all_answers}
    
    Give personality result in EXACTLY this format:
    
    ARCHETYPE: [3 words max]
    SAVAGE: [one short funny sentence - max 8 words]
    DEEP: [one short deep sentence - max 8 words]
    POETIC: [one beautiful sentence - max 8 words]
    
    Keep everything SHORT and PUNCHY!
    """
    return ask_gemini(prompt)
    
    

    
