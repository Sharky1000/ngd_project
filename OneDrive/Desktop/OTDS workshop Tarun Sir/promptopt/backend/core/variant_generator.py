import google.generativeai as genai
import os
import json

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
# Flash is perfect for fast iterative prompt generation
model = genai.GenerativeModel("gemini-2.0-flash")

META_PROMPT = """You are an expert prompt engineer. Your goal is to improve a base prompt for the task: {task_name} ({task_type}).
Return exactly a JSON array of {n} unique, improved prompt strings. Do NOT include markdown formatting or explanations. Just the raw JSON array.

Base prompt:
"{base}"

Feedback from previous rounds (if any):
{feedback}"""

def generate_variants(base_prompt: str, task_type: str, task_name: str, n: int, feedback: str = "None") -> list[str]:
    prompt = META_PROMPT.format(task_name=task_name, task_type=task_type, n=n, base=base_prompt, feedback=feedback)
    try:
        res = model.generate_content(prompt)
        text = res.text.strip()
        # Strip markdown code blocks if Gemini adds them
        if text.startswith("```"):
            text = text.split("\n", 1)[1].rsplit("```", 1)[0]
        variants = json.loads(text)
        return variants[:n]
    except Exception as e:
        print(f"⚠️ Variant generation error: {e}")
        # Fallback so the loop doesn't break
        return [f"{base_prompt} [variant {i+1}]" for i in range(n)]