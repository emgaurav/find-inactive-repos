import requests
from datetime import datetime, timedelta
import concurrent.futures

# Your GitHub Personal Access Token and organization name
ORG_NAME = "{ORG_NAME}"
GITHUB_TOKEN = "{YOUR_TOKEN}"

# Base URL for GitHub API
BASE_URL = "https://api.github.com"

# Headers to use with the GitHub API
headers = {
    'Authorization': f'token {GITHUB_TOKEN}',
    'Accept': 'application/vnd.github.v3+json',
}

# Function to fetch repos from the GitHub organization
def fetch_org_repos(org_name):
    repos = []
    page = 1
    while True:
        print(f"Fetching page {page} of repositories...")
        response = requests.get(f'{BASE_URL}/orgs/{org_name}/repos?type=all&per_page=100&page={page}', headers=headers)
        response_data = response.json()
        if response.status_code != 200 or not response_data:
            break
        repos.extend(response_data)
        print(f"Fetched {len(response_data)} repositories.")
        page += 1
    return repos

# Function to check if a repo has been committed to in the last 90 days
def is_repo_inactive(repo, days=90):
    latest_commit_url = repo['commits_url'].split('{')[0] + 'master'
    response = requests.get(latest_commit_url, headers=headers)
    if response.status_code != 200:
        return False  # Assume active if we can't fetch the commit
    commit_date = datetime.strptime(response.json()[0]['commit']['committer']['date'], '%Y-%m-%dT%H:%M:%SZ')
    return datetime.utcnow() - commit_date > timedelta(days=days)

# Function to process each repository in parallel
def process_repo(repo):
    print(f"Checking repository: {repo['name']}")
    if is_repo_inactive(repo):
        print(f"Repository {repo['name']} is inactive.")
        return repo['name']
    else:
        print(f"Repository {repo['name']} is active.")
        return None

# Main function to fetch and check repos
def main():
    repos = fetch_org_repos(ORG_NAME)
    total_repos = len(repos)
    print(f"Total repositories to check: {total_repos}")

    # Using ThreadPoolExecutor to process repositories in parallel
    with concurrent.futures.ThreadPoolExecutor() as executor:
        future_to_repo = {executor.submit(process_repo, repo): repo for repo in repos}
        inactive_repos = [future.result() for future in concurrent.futures.as_completed(future_to_repo) if future.result()]

    print(f"\nInactive Repositories (No commits in last 90 days):")
    for repo in inactive_repos:
        if repo: print(repo)

if __name__ == "__main__":
    main()
