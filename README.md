# find-inactive-repos

This Python script is designed to automate the process of checking for inactive repositories within a GitHub organization. It leverages the GitHub API to fetch all repositories under a specified organization and then determines which ones have not had any commits in the last 90 days. The script runs these checks in parallel to improve efficiency, making it suitable for organizations with a large number of repositories.

## Features

- Fetches all repositories from a specified GitHub organization.
- Checks if a repository has been inactive (no commits) in the last 90 days.
- Processes repositories in parallel to speed up the checking process.
- Utilizes GitHub's REST API with proper authentication.

## Prerequisites

Before you start using this script, make sure you have:

- Python installed on your system.
- `requests` library installed. You can install it via pip: `pip install requests`.
- A GitHub Personal Access Token with appropriate permissions to access the organization's repositories.
- The name of the GitHub organization you wish to check.

## Usage

1. Clone or download this script to your local machine.
2. Open the script with your favorite text editor or IDE.
3. Replace `{ORG_NAME}` with the name of your organization.
4. Replace `{YOUR_TOKEN}` with your GitHub Personal Access Token.
5. Run the script: `python script_name.py`.

## How It Works

1. **Setting Up Authentication**: The script uses your GitHub Personal Access Token for authentication, allowing it to fetch repository data from your organization.

2. **Fetching Repositories**: It fetches a list of all repositories from the specified organization through the GitHub API.

3. **Checking Activity**: For each repository, it checks the date of the last commit to determine if it has been inactive for more than 90 days.

4. **Parallel Processing**: The script uses `concurrent.futures.ThreadPoolExecutor` to process multiple repositories in parallel, making the script efficient even for organizations with a large number of repositories.

5. **Reporting**: Inactive repositories are reported in the console output, allowing you to take further action if necessary.

## Important Notes

- Ensure your GitHub Personal Access Token has the necessary permissions to access repository data.
- The script assumes a repository is active if it cannot fetch the last commit date, erring on the side of caution.

## Customization

You can customize the script by changing the `days` parameter in the `is_repo_inactive` function if you wish to check for a different period of inactivity.

## Contributing

Feel free to fork this repository, make improvements, and submit pull requests. We appreciate contributions that improve the script's functionality and usability.
