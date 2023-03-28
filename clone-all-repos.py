import requests
import git

# Replace <company-name> with the name of the company whose repositories you want to clone.
company_name = "<company-name>"

# Replace <your-github-username> with your GitHub username.
username = "<your-github-username>"

# Replace <your-github-access-token> with your personal access token obtained from GitHub.
access_token = "<your-github-access-token>"

# Create a session object and set the access token in the headers to authenticate requests.
session = requests.Session()
session.auth = (username, access_token)

# Get a list of all repositories for the company.
url = f"https://api.github.com/orgs/{company_name}/repos?type=all&per_page=1000"
response = session.get(url)

# Check if the response is successful, and if so, clone each repository using GitPython.
if response.status_code == 200:
    repos = response.json()
    for repo in repos:
        repo_name = repo["name"]
        repo_url = repo["ssh_url"]
        print(f"Cloning repository {repo_name}...")
        git.Repo.clone_from(repo_url, repo_name)
else:
    print(f"Error retrieving repositories: {response.content}")
