import requests

BASE_URL = "https://amit0987-cookies-recever-api.hf.space"

sample_data = {
    "data": {
        "session": "test_session_123_from_script",
        "user": "test_user_abc_from_script",
        "expires": "2026-01-01"
    },
    "raw_cookies_string": "session=test_session_123_from_script; user=test_user_abc_from_script; expires=2026-01-01",
    "source_url": "https://script-test.com"
}

def post_cookies():
    try:
        response = requests.post(f"{BASE_URL}/save-cookies", json=sample_data, timeout=10)
        response.raise_for_status()
        print("[POST] ✅", response.json())
    except Exception as e:
        print("[POST] ❌", e)

def get_cookies():
    try:
        response = requests.get(f"{BASE_URL}/cookies", timeout=10)
        response.raise_for_status()
        print("[GET] ✅", response.json())
        return response.json()
    except Exception as e:
        print("[GET] ❌", e)

if __name__ == "__main__":
    # post_cookies()
    get_cookies()
