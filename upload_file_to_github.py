import requests
import base64

import ImportantVariables
import crediantials


def upload_to_github(token, owner, repo, local_file_path, github_file_path, branch="main"):

    url = f"https://api.github.com/repos/{owner}/{repo}/contents/{github_file_path}"
    headers = {"Authorization": f"token {token}", "Accept": "application/vnd.github.v3+json"}

    # Read file content and encode it in Base64
    with open(local_file_path, "rb") as file:
        content = base64.b64encode(file.read()).decode("utf-8")

    # Check if the file already exists to get its SHA
    response = requests.get(url, headers=headers)
    sha = response.json().get("sha", None) if response.status_code == 200 else None

    # Prepare data payload
    data = {
        "message": f"Upload {github_file_path} via API",
        "content": content,
        "branch": branch
    }
    if sha:
        data["sha"] = sha  # Required for updating an existing file

    # Upload the file
    response = requests.put(url, json=data, headers=headers)

    return response.json()  # Return API response


def main():
    # Example usage
    GITHUB_TOKEN = crediantials.GITHUB_TOKEN
    GITHUB_OWNER = ImportantVariables.GITHUB_OWNER
    GITHUB_REPO = ImportantVariables.GITHUB_REPO
    TOKENS_LOCAL_FILE_PATH = ImportantVariables.COOKIES_LOCAL_FILE_PATH
    GITHUB_FILE_PATH = "main_cookies.txt"

    # generate_new_refresh_token.main()

    result = upload_to_github(GITHUB_TOKEN, GITHUB_OWNER, GITHUB_REPO, TOKENS_LOCAL_FILE_PATH, GITHUB_FILE_PATH)
    print(result)

if __name__ == "__main__":
    main()
