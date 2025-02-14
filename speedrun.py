# %%
# imports
class Agent:
    def __init__(self, name, strategy):
        self.name = name
        self.strategy = strategy

    def act(self):
        # Implement the agent's action based on its strategy
        print(f"{self.name} is acting using {self.strategy} strategy.")

    def learn(self, feedback):
        # Implement learning from feedback
        print(f"{self.name} is learning from feedback: {feedback}")


# %%
# Read in codebase
import os
import requests


def read_github_repo_files(repo_url):
    """
    Reads all files from a GitHub repository and returns their content along with file identifiers.

    Args:
        repo_url (str): The URL of the GitHub repository (e.g., 'https://github.com/user/repo').

    Returns:
        dict: A dictionary where keys are file identifiers (file paths) and values are file contents.
    """
    # Extract the user and repo name from the URL
    parts = repo_url.strip().split("/")
    user, repo = parts[-2], parts[-1]

    # GitHub API URL to get the contents of the repo
    api_url = f"https://api.github.com/repos/{user}/{repo}/contents"

    response = requests.get(api_url)
    if response.status_code != 200:
        raise Exception(f"Failed to fetch repository contents: {response.status_code}")

    files_content = {}

    # Iterate through the files in the repository
    for item in response.json():
        if item["type"] == "file":
            file_path = item["path"]
            file_response = requests.get(item["download_url"])
            if file_response.status_code == 200:
                files_content[file_path] = file_response.text
            else:
                print(f"Failed to read file {file_path}: {file_response.status_code}")

    return files_content
