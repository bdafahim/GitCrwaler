import requests
import time
import json
from datetime import datetime

# Constants
GITHUB_API_URL = "https://api.github.com"
OWNER = "apache"
REPO = "ambari"
with open("access_token.txt", "r") as file:
    ACCESS_TOKEN = file.read().strip()

# Headers for authentication
headers = {
    "Authorization": f"token {ACCESS_TOKEN}",
    "Accept": "application/vnd.github.v3+json"
}

# Rate limit handler
def handle_rate_limit(response):
    if response.status_code == 403 and 'X-RateLimit-Remaining' in response.headers and response.headers['X-RateLimit-Remaining'] == '0':
        reset_time = int(response.headers['X-RateLimit-Reset'])
        sleep_time = max(0, reset_time - int(time.time()) + 1)
        print(f"Rate limit reached. Sleeping for {sleep_time} seconds.")
        time.sleep(sleep_time)
        return True
    return False

# Retry logic with exponential backoff
def fetch_with_retries(url, headers, max_retries=5):
    retries = 0
    while retries < max_retries:
        try:
            response = requests.get(url, headers=headers)
            if handle_rate_limit(response):
                continue
            if response.status_code == 200:
                return response.json()
            print(f"Error fetching data: {response.status_code} - {response.text}")
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f"Request failed: {e}. Retrying in {2 ** retries} seconds...")
            time.sleep(2 ** retries)
            retries += 1
    raise Exception(f"Failed to fetch data from {url} after {max_retries} retries.")

# Get all commits
def get_commits():
    commits = []
    page = 1
    while True:
        url = f"{GITHUB_API_URL}/repos/{OWNER}/{REPO}/commits?page={page}"
        page_commits = fetch_with_retries(url, headers)
        if not page_commits:
            break
        commits.extend(page_commits)
        page += 1
    return commits

# Get all issues
def get_issues():
    issues = []
    page = 1
    while True:
        url = f"{GITHUB_API_URL}/repos/{OWNER}/{REPO}/issues?page={page}&state=all"
        page_issues = fetch_with_retries(url, headers)
        if not page_issues:
            break
        issues.extend(page_issues)
        page += 1
    return issues

# Save data to JSON
def save_to_json(data, filename):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4, default=str)

def main():
    print("Fetching commits...")
    commits = get_commits()
    save_to_json(commits, 'commits.json')
    print(f"Saved {len(commits)} commits to commits.json")

    print("Fetching issues...")
    issues = get_issues()
    save_to_json(issues, 'issues.json')
    print(f"Saved {len(issues)} issues to issues.json")

if __name__ == "__main__":
    main()
