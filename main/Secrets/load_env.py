import os
from dotenv import load_dotenv

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
SPOONACULAR_API_KEY = os.getenv("SPOONACULAR_API_KEY")
VOICE_ID = os.getenv("VOICE_ID")
ELEVEN_LABS_API = os.getenv("ELEVEN_LABS_API")