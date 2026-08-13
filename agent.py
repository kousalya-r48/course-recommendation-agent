import os
import json
from google import genai

# Initialize Gemini Client (uses GEMINI_API_KEY from environment variables)
client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

SYSTEM_PROMPT = """
You are an expert Academic & Career Recommendation Agent.
Your job is to analyze a student's profile and recommend a step-by-step personalized learning path from the provided Course Catalogue.

RULES:
1. Recommend ONLY courses present in the provided Course Catalogue.
2. Ensure course prerequisites are satisfied based on the student's current skills.
3. Order the learning path logically from foundation to advanced.
4. For every recommended course, provide a clear rationale explaining WHY it fits their specific background and goals.
5. Return the result in clean JSON format matching this schema:
{
  "student_id": "...",
  "recommended_path": [
    {
      "step": 1,
      "course_id": "...",
      "course_title": "...",
      "rationale": "..."
    }
  ],
  "summary_reasoning": "..."
}
"""

def load_data():
    with open("catalogue.json", "r") as f:
        catalogue = json.load(f)
    with open("profiles.json", "r") as f:
        profiles = json.load(f)
    return catalogue, profiles

def run_agent(student_profile, catalogue):
    user_message = f"""
    Student Profile:
    {json.dumps(student_profile, indent=2)}

    Available Course Catalogue:
    {json.dumps(catalogue, indent=2)}
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=[SYSTEM_PROMPT, user_message],
    )

    return response.text

if __name__ == "__main__":
    catalogue, profiles = load_data()
    print("🤖 Course Recommendation Agent starting...\n")

    for profile in profiles:
        print(f"--- Generating Recommendation for {profile['name']} ({profile['student_id']}) ---")
        result = run_agent(profile, catalogue)
        print(result)
        print("\n" + "="*50 + "\n")
