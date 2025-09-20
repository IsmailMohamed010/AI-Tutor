import os
from dotenv import load_dotenv

load_dotenv()

# Load API credentials safely
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
if not GITHUB_TOKEN:
    raise ValueError("❌ Missing GITHUB_TOKEN in .env file!")

ENDPOINT = "https://models.github.ai/inference"
MODEL_NAME = "openai/o4-mini"
