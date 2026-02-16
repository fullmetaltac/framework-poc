from os import environ
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

# CONSTANTS

BASE_UI_URL = environ.get("BASE_UI_URL")
BASE_API_URL = environ.get("BASE_API_URL")

# CONFIG
CI: bool = environ.get("CI", "false") == "true"
TIMEOUT_API: int = int(environ.get("TIMEOUT_API", 10))


# FOLDERS
ROOT_DIR: Path = Path(__file__).resolve().parent.parent
TEMP_DIR: Path = ROOT_DIR / "zz_temp"
LOGS_DIR: Path = TEMP_DIR / "logs"
SCREENSHOTS_DIR: Path = TEMP_DIR / "screenshots"
