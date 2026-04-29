import google.generativeai as genai
import os

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel("gemini-2.0-flash")

def criteria_score(variant: str, criteria: list[str], test_input: str) -> float:
    if not criteria: return 0.5
    # Simple mock for speed; in prod, you'd loop each rule and ask Gemini
    # to verify if the output satisfies it.
    return 0.6 + (len(variant) % 8) * 0.03