import os
from pathlib import Path
from dotenv import load_dotenv

from utilities.logger import Logger

logger = Logger.get_logger(__name__)

BASE_DIR = Path(__file__).resolve().parent.parent
ENV_FILE = BASE_DIR / ".env"

logger.info(f"Loading .env from: {ENV_FILE}")

load_dotenv(dotenv_path=ENV_FILE, override=True)

BASE_URL = os.getenv("BASE_URL")
EMAIL_ADDRESS = os.getenv("APP_EMAIL_ADDRESS")
PASSWORD = os.getenv("APP_PASSWORD")

BROWSER = os.getenv("BROWSER", "chromium")
HEADLESS = os.getenv("HEADLESS", "False").lower() == "true"
TIMEOUT = int(os.getenv("TIMEOUT", "30000"))
SLOW_MO = int(os.getenv("SLOW_MO", "0"))

logger.info(f"BASE_URL: {BASE_URL}")
logger.info(f"EMAIL_ADDRESS: {EMAIL_ADDRESS}")
logger.info(f"PASSWORD: {'********' if PASSWORD else 'Not Configured'}")