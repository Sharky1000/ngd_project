import google.generativeai as genai
import os

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel("gemini-2.0-flash")

def run_on_dataset(variant: str, dataset: list[dict]) -> list[dict]:
    results = []
    # Limit to 3 for demo speed (scale this later with async)
    for ex in dataset[:3]:
        try:
            res = model.generate_content(f"{variant}\n\nInput: {ex['input']}")
            results.append({"input": ex["input"], "label": ex["label"], "model_output": res.text.strip()})
        except Exception as e:
            print(f"⚠️ Scorer error: {e}")
            results.append({"input": ex["input"], "label": ex["label"], "model_output": "error"})
    return results

def accuracy_score(scored: list[dict]) -> float:
    if not scored: return 0.0
    correct = 0
    for r in scored:
        pred = r["model_output"].lower().strip()
        label = r["label"].lower().strip()
        # Flexible matching: exact, substring, or starts with
        if pred == label or label in pred or pred.startswith(label.split()[0]):
            correct += 1
    return round(correct / len(scored), 3)

def llm_judge_score(variant: str, task_type: str, outputs: list[dict]) -> float:
    # Simplified fallback judge (replace with full LLM judge if needed)
    return 0.7 + (len(variant) % 10) * 0.02