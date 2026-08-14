
# Course Recommendation Agent

A personalized learning path recommendation agent built for the Rooman AI Challenge.

## 🎯 Goal Statement
"My Course Recommendation Agent takes a student profile (background, skills, career goal) and a structured course catalogue as input, and produces an ordered, personalized learning path with explicit rationale for every recommendation."

## 📁 Repository Structure
- `agent.py`: Core agent logic powered by Gemini API.
- `catalogue.json`: Course catalogue with prerequisite mapping.
- `profiles.json`: Test input student profiles.
- `test_agent.py`: Unit test suite.

## 📥 Sample Input & Output

### **Sample Input (`profiles.json`)**
```json
[
  {
    "student_id": "STU_001",
    "name": "Alice",
    "background": "2nd Year CSE Student",
    "current_skills": ["Basic Python", "High School Math"],
    "career_goal": "Become an AI & Machine Learning Engineer"
  },
  {
    "student_id": "STU_002",
    "name": "Rahul",
    "background": "Non-CS Business Graduate",
    "current_skills": ["Excel", "Communication"],
    "career_goal": "Transition to Data Analyst"
  },
  {
    "student_id": "STU003",
    "name": "David",
    "current_skills": ["Basic Networking", "Linux"],
    "career_goal": "Cybersecurity Analyst"
  },
  {
    "student_id": "STU004",
    "name": "Sophia",
    "current_skills": ["Python", "SQL"],
    "career_goal": "Machine Learning Engineer"
  }
]
```
### **Sample Output (Agent JSON Response for STU_001)**
```json
{
  "student_id": "STU_001",
  "recommended_path": [
    {
      "step": 1,
      "course_id": "CS101",
      "course_title": "Advanced Python & Data Structures",
      "rationale": "Builds upon basic Python skills and provides essential programming concepts required for AI models."
    },
    {
      "step": 2,
      "course_id": "MATH201",
      "course_title": "Linear Algebra & Probability for AI",
      "rationale": "Transitions high school math foundations into core mathematical concepts needed for machine learning algorithms."
    },
    {
      "step": 3,
      "course_id": "AI301",
      "course_title": "Applied Machine Learning & Deep Learning",
      "rationale": "Directly achieves the target goal of becoming an AI/ML Engineer after prerequisites are fulfilled."
    }
  ],
  "summary_reasoning": "Alice leverages her CSE background and Python basics to progress systematically through advanced programming, foundational AI math, and practical machine learning."
}
```

## 🚀 Setup & Execution
1. Clone this repository:
   ```bash
   git clone https://github.com/kousalya-r48/course-recommendation-agent.git
   cd course-recommendation-agent
   ```

2. Install required dependencies:
   ```bash
   pip install google-genai pytest
   ```
   
3. Set your Gemini API key in environment:

- Windows (CMD):
```cmd
set GEMINI_API_KEY=your_gemini_api_key
```
- Linux/Mac:
 ```bash
export GEMINI_API_KEY="your_gemini_api_key"
  ```

4. Run the Agent:
  ```bash
    python agent.py
```

## Running Tests

To run the automated unit tests, make sure `pytest` is installed and execute:
```bash
pytest
```
## ⚖️ Tradeoff & Architectural Reasoning
- `Model Selection`: Selected gemini-3.6-flash for high-speed inference, cost-efficiency, and strong structured output capabilities.

- `Design Tradeoffs`: Injected catalogue data directly into the system prompt context rather than setting up a RAG pipeline or Vector DB. For a small catalog, this eliminates DB query latency and keeps execution zero-friction and deterministic.

- `Future Improvements`: Implement strict Directed Acyclic Graph (DAG) logic in Python to deterministically validate prerequisites prior to calling the LLM.
