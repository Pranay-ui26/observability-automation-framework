import os
from pathlib import Path
from dotenv import load_dotenv

# Absolute path to the project root .env
BASE_DIR = Path(__file__).resolve().parent.parent
ENV_FILE = BASE_DIR / ".env"

print(f"Loading .env from: {ENV_FILE}")

load_dotenv(dotenv_path=ENV_FILE, override=True)

BASE_URL = os.getenv("BASE_URL")
EMAIL_ADDRESS = os.getenv("APP_EMAIL_ADDRESS")
PASSWORD = os.getenv("APP_PASSWORD")

BROWSER = os.getenv("BROWSER", "chromium")
HEADLESS = os.getenv("HEADLESS", "False").lower() == "true"
TIMEOUT = int(os.getenv("TIMEOUT", "30000"))
SLOW_MO = int(os.getenv("SLOW_MO", "0"))

print("BASE_URL :", BASE_URL)
print("USERNAME :", EMAIL_ADDRESS)
print("PASSWORD :", "********" if PASSWORD else None)