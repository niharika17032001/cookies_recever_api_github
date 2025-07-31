import os

# root folder path
file_path = os.path.abspath(__file__)
current_Folder_Path = os.path.dirname(file_path)
root_folder = os.path.dirname(current_Folder_Path)

# current folder path
cookies_file_path = current_Folder_Path + "/main_cookies.txt"

# github
GITHUB_OWNER = "niharika17032001"
GITHUB_WORKFLOW_FILE = "main.yml"
GITHUB_BRANCH = "main"
GITHUB_REPO = "youtube_vedio_download_github"
COOKIES_LOCAL_FILE_PATH = "main_cookies.txt"

