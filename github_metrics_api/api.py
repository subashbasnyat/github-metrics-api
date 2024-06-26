import os
import requests
from .errors import (
    GitHubAPIError,
    RateLimitExceededError,
    AuthenticationError,
    NotFoundError,
    ServerError,
)


class GitHubMetricsAPI:
    BASE_URL = "https://api.github.com"

    def __init__(self, access_token=os.environ.get("GITHUB_API_TOKEN")):
        self.session = requests.Session()
        if access_token:
            self.session.headers.update({"Authorization": f"token {access_token}"})
        self.session.headers.update({"Accept": "application/vnd.github.v3+json"})

    def _make_request(self, method, endpoint, params=None, data=None):
        url = f"{self.BASE_URL}/{endpoint}"
        response = self.session.request(method, url, params=params, json=data)

        if response.status_code == 200:
            return response.json()
        elif response.status_code == 204:
            return None
        elif response.status_code == 401:
            raise AuthenticationError()
        elif (
            response.status_code == 403
            and "X-RateLimit-Remaining" in response.headers
            and int(response.headers["X-RateLimit-Remaining"]) == 0
        ):
            raise RateLimitExceededError()
        elif response.status_code == 404:
            raise NotFoundError()
        elif 500 <= response.status_code < 600:
            raise ServerError()
        else:
            raise GitHubAPIError(
                f"GitHub API request failed: {response.status_code}",
                code="UNKNOWN_ERROR",
            )

    # Repositories
    def get_repo(self, owner, repo):
        """Get repository information."""
        return self._make_request("GET", f"repos/{owner}/{repo}")

    def list_repo_contributors(self, owner, repo):
        """List contributors for a repository."""
        return self._make_request("GET", f"repos/{owner}/{repo}/contributors")

    def list_repo_languages(self, owner, repo):
        """List languages for a repository."""
        return self._make_request("GET", f"repos/{owner}/{repo}/languages")

    def get_repo_readme(self, owner, repo):
        """Get the README for a repository."""
        return self._make_request("GET", f"repos/{owner}/{repo}/readme")

    # Issues
    def list_repo_issues(self, owner, repo, state="open"):
        """List issues for a repository."""
        return self._make_request(
            "GET", f"repos/{owner}/{repo}/issues", params={"state": state}
        )

    # def create_issue(self, owner, repo, title, body=None, labels=None):
    #     """Create an issue in a repository."""
    #     data = {"title": title, "body": body, "labels": labels}
    #     return self._make_request("POST", f"repos/{owner}/{repo}/issues", data=data)

    # Pull Requests
    def list_pull_requests(self, owner, repo, state="open"):
        """List pull requests for a repository."""
        return self._make_request(
            "GET", f"repos/{owner}/{repo}/pulls", params={"state": state}
        )

    def get_pull_request(self, owner, repo, pull_number):
        """Get a specific pull request."""
        return self._make_request("GET", f"repos/{owner}/{repo}/pulls/{pull_number}")

    # Users
    def get_user(self, username):
        """Get information about a user."""
        return self._make_request("GET", f"users/{username}")

    def list_user_repos(self, username):
        """List repositories for a user."""
        return self._make_request("GET", f"users/{username}/repos")

    # Organizations
    def get_organization(self, org):
        """Get information about an organization."""
        return self._make_request("GET", f"orgs/{org}")

    def list_org_repos(self, org):
        """List repositories for an organization."""
        return self._make_request("GET", f"orgs/{org}/repos")

    # Projects
    def list_repo_projects(self, owner, repo):
        """List projects for a repository."""
        return self._make_request("GET", f"repos/{owner}/{repo}/projects")

    # Search
    def search_repositories(self, query, sort=None, order=None):
        """Search for repositories."""
        params = {"q": query, "sort": sort, "order": order}
        return self._make_request("GET", "search/repositories", params=params)

    def search_issues(self, query, sort=None, order=None):
        """Search for issues and pull requests."""
        params = {"q": query, "sort": sort, "order": order}
        return self._make_request("GET", "search/issues", params=params)

    # Gists
    def list_user_gists(self, username):
        """List public gists for a user."""
        return self._make_request("GET", f"users/{username}/gists")

    # Git Data
    def list_commits(self, owner, repo):
        """List commits for a repository."""
        return self._make_request("GET", f"repos/{owner}/{repo}/commits")

    def get_commit(self, owner, repo, sha):
        """Get a specific commit."""
        return self._make_request("GET", f"repos/{owner}/{repo}/commits/{sha}")

    # Actions
    def list_workflow_runs(self, owner, repo):
        """List workflow runs for a repository."""
        return self._make_request("GET", f"repos/{owner}/{repo}/actions/runs")

    # Webhooks
    def list_repo_webhooks(self, owner, repo):
        """List webhooks for a repository."""
        return self._make_request("GET", f"repos/{owner}/{repo}/hooks")

    # Additional repository statistics (from previous implementation)
    def get_repo_stats(self, owner, repo):
        """Get repository statistics."""
        data = self.get_repo(owner, repo)
        return {
            "stars": data["stargazers_count"],
            "forks": data["forks_count"],
            "open_issues": data["open_issues_count"],
            "watchers": data["subscribers_count"],
        }

    def get_commit_activity(self, owner, repo):
        """Get commit activity for a repository."""
        return self._make_request("GET", f"repos/{owner}/{repo}/stats/commit_activity")

    def get_code_frequency(self, owner, repo):
        """Get code frequency statistics for a repository."""
        return self._make_request("GET", f"repos/{owner}/{repo}/stats/code_frequency")

    def get_contributor_stats(self, owner, repo):
        """Get contributor statistics for a repository."""
        return self._make_request("GET", f"repos/{owner}/{repo}/stats/contributors")

    def get_weekly_commits(self, owner, repo):
        """Get weekly commit counts for a repository."""
        return self._make_request("GET", f"repos/{owner}/{repo}/stats/participation")

    def get_punch_card(self, owner, repo):
        """Get commit punch card data for a repository."""
        return self._make_request("GET", f"repos/{owner}/{repo}/stats/punch_card")
