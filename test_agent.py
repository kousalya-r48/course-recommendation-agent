import json
import pytest
from agent import run_agent  # or whatever your core function/class is named

# Sample test data
@pytest.fixture
def sample_data():
    profile = {
        "student_id": "STU001",
        "name": "Test Student",
        "current_skills": ["Python"],
        "career_goal": "Data Scientist"
    }
    catalogue = [
        {
            "course_id": "CS101",
            "title": "Advanced Python",
            "prerequisites": ["Python"]
        },
        {
            "course_id": "DS201",
            "title": "Machine Learning Fundamentals",
            "prerequisites": ["CS101"]
        }
    ]
    return profile, catalogue

def test_catalogue_structure(sample_data):
    """Test if catalogue data is structured properly."""
    _, catalogue = sample_data
    assert isinstance(catalogue, list)
    assert len(catalogue) > 0
    assert "course_id" in catalogue[0]

def test_profile_structure(sample_data):
    """Test if profile data contains required fields."""
    profile, _ = sample_data
    assert "student_id" in profile
    assert "career_goal" in profile
