import asyncio
from pydantic import BaseModel, Field
from agents import Agent, Runner, FunctionTool, function_tool
from dotenv import load_dotenv
import os

# Load environment variable
# set model of choice
model = os.getenv('LLM_MODEL_NAME', 'gpt-4o-mini')


# --- Strucutured Output Model ---
class WorkoutPlan(BaseModel) :
    """Workout recommendataion with exercises and details"""
    focus_area: str = Field(description="Primary focus of the workout (e.g., 'upper body', 'cardio')")
    difficulty: str = Field(description="Difficulty level (Beginner, Intermediate, Advanced)")
    exercises: list[str] = Field(description="List of recommended exercises")
    notes: str = Field(description="Additional notes or form tips")

# --- Tools ---
@function_tool
def get_exercise_info(muscle_group: str) -> str:
    """Get a list of exercises for a specifice muscle group"""
    exercise_data = {
        "chest": [
            "Push-ups: 3 sets of 10-15 reps",
            "Bench Press: 3 sets of 8-12 reps"
        ]
    }

    muscle_group = muscle_group.lower()
    if muscle_group in exercise_data:
        exercises = exercise_data[muscle_group]
        return json.dumps({
            "muscle_group": muscle_group,
            "exercises": exercises,
            "recommendation": f"For {muscle_group} training, complete all exercises with 60-90 seconds rest between sets."
        })
    else: return f"Exercise information for {muscle_group} is not available."
