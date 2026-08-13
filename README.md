
# Course Recommendation Agent

A personalized learning path recommendation agent built for the Rooman AI Challenge.

## 🎯 Goal Statement
"My Course Recommendation Agent takes a student profile (background, skills, career goal) and a structured course catalogue as input, and produces an ordered, personalized learning path with explicit rationale for every recommendation."

## 📁 Repository Structure
- `agent.py`: Core agent logic powered by Gemini API.
- `catalogue.json`: Course catalogue with prerequisite mapping.
- `profiles.json`: Test input student profiles.

## 📥 Sample Input & Output

### **Sample Input (`profiles.json` entry)**
```json
{
  "student_id": "STU001",
  "name": "Alex",
  "current_skills": ["Python basics"],
  "career_goal": "Data Scientist"
}

### **Sample Output (Agent JSON Response)**
{
  "student_id": "STU001",
  "recommended_path": [
    {
      "step": 1,
      "course_id": "CS101",
      "course_title": "Advanced Python & Data Structures",
      "rationale": "Strengthens core programming foundations necessary for handling data science workflows."
    },
    {
      "step": 2,
      "course_id": "DS201",
      "course_title": "Introduction to Machine Learning",
      "rationale": "Directly targets the career goal of becoming a data scientist after mastering prerequisite programming."
    }
  ],
  "summary_reasoning": "Alex starts with Python skill reinforcement and transitions cleanly into foundational machine learning."
}

## 🚀 Setup & Execution
1. Clone this repository:
   ```bash
   git clone https://github.com/kousalya-r48/course-recommendation-agent.git
   cd course-recommendation-agent

## Install required dependencies:
pip install google-genai

## Set your Gemini API key in environment:
- `Windows(CMD)`: set GEMINI_API_KEY=your_gemini_api_key
- `Linux/Mac`: export GEMINI_API_KEY="your_gemini_api_key"

## Run the Agent:
python agent.py

## ⚖️ Tradeoff & Architectural Reasoning
- `Model Selection`: Selected gemini-2.5-flash for high-speed inference, cost-efficiency, and strong structured output capabilities.

- `Design Tradeoffs`: Injected catalogue data directly into the system prompt context rather than setting up a RAG pipeline or Vector DB. For a small catalog, this eliminates DB query latency and keeps execution zero-friction and deterministic.

- `Future Improvements`: Implement strict Directed Acyclic Graph (DAG) logic in Python to deterministically validate prerequisites prior to calling the LLM.
