from dotenv import load_dotenv
import os

load_dotenv()

GITHUB_TOKEN = os.getenv("MY_GITHUB_TOKEN")

required_secrets = {
    "GITHUB_TOKEN": GITHUB_TOKEN
}

for key, value in required_secrets.items():
    if not value:
        raise ValueError(f"{key} is missing. Ensure it is set in GitHub Secrets.")