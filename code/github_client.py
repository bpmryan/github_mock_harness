import requests 

def get_public_repo_count(username: str) -> int:
    url = f"https://api.github.com/users/{username}"

    # get request to the target url
    response = requests.get(url)
    print(response.json())

    # check for failure 
    if response.status_code != 200:
        raise ValueError("GitHub identity lookup failed")
    
    # parse the reponse body as JSON and extract the repo count
    payload = response.json()
    return payload["public_repos"] # grab integer count of public repo
