import asyncio
from pydantic import BaseModel, Field
from agents import Agent, Runner
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

# --- Simple Fitness Agent ---
fitness_agent = Agent(
    name="Basic Fitness Coach",
    instruction="""
    You are a fitness coach who creates workout plans for users based on their goals.

    When a user asks for workout recommendations:
    1. Determine their fitness goal (weight loss, muscle gain, endurance, etc.)
    2. Consider any information they provide about their fitness level.
    3. Create an appropriate workout plan with with exerecises that match their goal
    4. Include form tips and safety notes

    Your responses should be practical, safe, and taiolored to the user's needs.
    """

    model=model,
    output_type=WorkoutPlan # structured output

)