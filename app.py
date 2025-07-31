from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import json
from pathlib import Path
from urllib.parse import urlparse

import convert_cookie_for_youtube
import upload_file_to_github

app = FastAPI()

# --- CORS Configuration ---
origins = ["*"]  # Allow all origins for development (restrict in production)
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- File-based Storage Setup ---
STORAGE_FILE = Path("cookies.json")

def load_cookies():
    if STORAGE_FILE.exists():
        try:
            with open(STORAGE_FILE, "r") as f:
                return json.load(f)
        except json.JSONDecodeError:
            return {}
    return {}

def save_cookies_to_file(data):
    with open(STORAGE_FILE, "w") as f:
        json.dump(data, f)

save_data = load_cookies()

# --- POST Endpoint: Save Cookies ---
@app.post("/save-cookies")
async def save_cookies(request: Request):
    try:
        data = await request.json()
        print(f"Received POST data: {data}")

        # Validate structure
        if "raw_cookies_string" in data and "source_url" in data:


            # Extract domain like 'youtube' or 'instagram' from the source_url
            parsed_domain = urlparse(data["source_url"]).hostname or ""
            domain_key = parsed_domain.split('.')[-2] if parsed_domain else "unknown"

            # Clean and normalize key if needed
            domain_key = domain_key.strip().lower()

            # Save data dynamically using the domain_key
            save_data[domain_key] = {
                "raw_cookies": data["raw_cookies_string"],
                "source_url": data["source_url"]
            }

            save_cookies_to_file(save_data)
            convert_cookie_for_youtube.main(save_data)
            print(f"Stored data: {save_data}")
            upload_file_to_github.main()
            return JSONResponse(content={"message": "Cookies received and stored"}, status_code=200)
        else:
            return JSONResponse(content={"message": "Invalid data structure"}, status_code=400)

    except Exception as e:
        print(f"Error in POST: {e}")
        return JSONResponse(content={"message": f"Error: {e}"}, status_code=500)

# --- GET Endpoint: Retrieve Cookies ---
@app.get("/cookies")
async def get_cookies():
    print(f"Returning stored cookies: {save_data}")
    return JSONResponse(content=save_data, status_code=200)

# --- Root Endpoint: Status Check ---
@app.get("/")
async def read_root():
    return {"message": "Cookie Receiver API is running!"}
