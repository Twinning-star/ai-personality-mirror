from questions import ask_gemini

def analyze_personality(all_answers):
    prompt = f"""
    Based on these answers from a personality test:
    {all_answers}
    
    Reveal personality in exactly 4 parts.
    Each part must be ONLY 1 sentence. No more.
    Use simple easy English.
    
    ARCHETYPE: [one cool name]
    SAVAGE: [one funny brutal sentence]
    DEEP: [one deep insight sentence]
    POETIC: [one beautiful sentence]
    """

    return ask_gemini(prompt)
