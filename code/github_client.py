import requests 

def get_public_repo_count(username: str) -> int:
    url = f"https://api.github.com/users/{username}"