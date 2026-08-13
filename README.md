```markdown
# Course Recommendation Agent

A personalized learning path recommendation agent built for the Rooman AI Challenge.

## 🎯 Goal Statement
"My Course Recommendation Agent takes a student profile (background, skills, career goal) and a structured course catalogue as input, and produces an ordered, personalized learning path with explicit rationale for every recommendation."

## 📁 Repository Structure
- `agent.py`: Core agent logic powered by Gemini API.
- `catalogue.json`: Course catalogue with prerequisite mapping.
- `profiles.json`: Test input student profiles.

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
