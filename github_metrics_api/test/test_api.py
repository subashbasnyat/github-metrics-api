import pytest
from unittest.mock import patch, Mock
from github_metrics_api.api import GitHubMetricsAPI
from github_metrics_api.errors import GitHubAPIError, AuthenticationError


@pytest.fixture
def api():
    return GitHubMetricsAPI(access_token="test_token")


def test_get_repo_success(api):
    with patch.object(api.session, "request") as mock_request:
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "name": "test_repo",
            "description": "A test repo",
        }
        mock_request.return_value = mock_response

        repo = api.get_repo("test_owner", "test_repo")
        assert repo == {"name": "test_repo", "description": "A test repo"}

        mock_request.assert_called_once_with(
            "GET",
            "https://api.github.com/repos/test_owner/test_repo",
            params=None,
            json=None,
        )


def test_get_repo_failure(api):
    with patch.object(api.session, "request") as mock_request:
        mock_response = Mock()
        mock_response.status_code = 404
        mock_request.return_value = mock_response

        with pytest.raises(GitHubAPIError):
            api.get_repo("test_owner", "test_repo")


def test_list_repo_contributors_success(api):
    with patch.object(api.session, "request") as mock_request:
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = [{"login": "user1"}, {"login": "user2"}]
        mock_request.return_value = mock_response

        contributors = api.list_repo_contributors("test_owner", "test_repo")
        assert contributors == [{"login": "user1"}, {"login": "user2"}]

        mock_request.assert_called_once_with(
            "GET",
            "https://api.github.com/repos/test_owner/test_repo/contributors",
            params=None,
            json=None,
        )


def test_list_repo_contributors_failure(api):
    with patch.object(api.session, "request") as mock_request:
        mock_response = Mock()
        mock_response.status_code = 404
        mock_request.return_value = mock_response

        with pytest.raises(GitHubAPIError):
            api.list_repo_contributors("test_owner", "test_repo")


def test_list_repo_languages_success(api):
    with patch.object(api.session, "request") as mock_request:
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"Python": 1000, "JavaScript": 500}
        mock_request.return_value = mock_response

        languages = api.list_repo_languages("test_owner", "test_repo")
        assert languages == {"Python": 1000, "JavaScript": 500}

        mock_request.assert_called_once_with(
            "GET",
            "https://api.github.com/repos/test_owner/test_repo/languages",
            params=None,
            json=None,
        )


def test_list_repo_languages_failure(api):
    with patch.object(api.session, "request") as mock_request:
        mock_response = Mock()
        mock_response.status_code = 500
        mock_request.return_value = mock_response

        with pytest.raises(GitHubAPIError):
            api.list_repo_languages("test_owner", "test_repo")


def test_get_repo_readme_success(api):
    with patch.object(api.session, "request") as mock_request:
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"content": "test content"}
        mock_request.return_value = mock_response

        readme = api.get_repo_readme("test_owner", "test_repo")
        assert readme == {"content": "test content"}

        mock_request.assert_called_once_with(
            "GET",
            "https://api.github.com/repos/test_owner/test_repo/readme",
            params=None,
            json=None,
        )


def test_get_repo_readme_failure(api):
    with patch.object(api.session, "request") as mock_request:
        mock_response = Mock()
        mock_response.status_code = 404
        mock_request.return_value = mock_response

        with pytest.raises(GitHubAPIError):
            api.get_repo_readme("test_owner", "test_repo")


def test_list_repo_issues_success(api):
    with patch.object(api.session, "request") as mock_request:
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = [{"title": "Issue 1"}, {"title": "Issue 2"}]
        mock_request.return_value = mock_response

        issues = api.list_repo_issues("test_owner", "test_repo")
        assert issues == [{"title": "Issue 1"}, {"title": "Issue 2"}]

        mock_request.assert_called_once_with(
            "GET",
            "https://api.github.com/repos/test_owner/test_repo/issues",
            params={"state": "open"},
            json=None,
        )


def test_list_repo_issues_failure(api):
    with patch.object(api.session, "request") as mock_request:
        mock_response = Mock()
        mock_response.status_code = 404
        mock_request.return_value = mock_response

        with pytest.raises(GitHubAPIError):
            api.list_repo_issues("test_owner", "test_repo")


def test_list_pull_requests_success(api):
    with patch.object(api.session, "request") as mock_request:
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = [{"title": "PR 1"}, {"title": "PR 2"}]
        mock_request.return_value = mock_response

        prs = api.list_pull_requests("test_owner", "test_repo")
        assert prs == [{"title": "PR 1"}, {"title": "PR 2"}]
        mock_request.assert_called_once_with(
            "GET",
            "https://api.github.com/repos/test_owner/test_repo/pulls",
            params={'state': 'open'},
            json=None,
        )


def test_list_pull_requests_failure(api):
    with patch.object(api.session, "request") as mock_request:
        mock_response = Mock()
        mock_response.status_code = 500
        mock_request.return_value = mock_response

        with pytest.raises(GitHubAPIError):
            api.list_pull_requests("test_owner", "test_repo")


def test_get_repo_stats_success(api):
    with patch.object(api.session, "request") as mock_request:
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "stargazers_count": 1000,
            "forks_count": 500,
            "open_issues_count": 50,
            "subscribers_count": 1500,
        }
        mock_request.return_value = mock_response

        stats = api.get_repo_stats("test_owner", "test_repo")
        assert stats == {
            "stars": 1000,
            "forks": 500,
            "open_issues": 50,
            "watchers": 1500,
        }

        mock_request.assert_called_once_with(
            "GET",
            "https://api.github.com/repos/test_owner/test_repo",
            params=None,
            json=None,
        )


def test_get_repo_stats_failure(api):
    with patch.object(api.session, "request") as mock_request:
        mock_response = Mock()
        mock_response.status_code = 404
        mock_request.return_value = mock_response
        with pytest.raises(GitHubAPIError):
            api.get_repo_stats("test_owner", "test_repo")


def test_get_commit_activity_success(api):
    with patch.object(api.session, "request") as mock_request:
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = [
            {"week": 1, "total": 10},
            {"week": 2, "total": 20},
        ]
        mock_request.return_value = mock_response

        activity = api.get_commit_activity("test_owner", "test_repo")
        assert activity == [{"week": 1, "total": 10}, {"week": 2, "total": 20}]

        mock_request.assert_called_once_with(
            "GET",
            "https://api.github.com/repos/test_owner/test_repo/stats/commit_activity",
            params=None,
            json=None,
        )


def test_get_commit_activity_failure(api):
    with patch.object(api.session, "request") as mock_request:
        mock_response = Mock()
        mock_response.status_code = 404
        mock_request.return_value = mock_response

        with pytest.raises(GitHubAPIError):
            api.get_commit_activity("test_owner", "test_repo")


def test_get_code_frequency_success(api):
    with patch.object(api.session, "request") as mock_request:
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = [
            [1609459200, 100, -50],
            [1609545600, 200, -75],
        ]
        mock_request.return_value = mock_response

        frequency = api.get_code_frequency("test_owner", "test_repo")
        assert frequency == [[1609459200, 100, -50], [1609545600, 200, -75]]

        mock_request.assert_called_once_with(
            "GET",
            "https://api.github.com/repos/test_owner/test_repo/stats/code_frequency",
            params=None,
            json=None,
        )


def test_get_code_frequency_failure(api):
    with patch.object(api.session, "request") as mock_request:
        mock_response = Mock()
        mock_response.status_code = 404
        mock_request.return_value = mock_response

        with pytest.raises(GitHubAPIError):
            api.get_code_frequency("test_owner", "test_repo")


def test_get_contributor_stats_success(api):
    with patch.object(api.session, "request") as mock_request:
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = [
            {"author": {"login": "user1"}, "total": 50},
            {"author": {"login": "user2"}, "total": 30},
        ]
        mock_request.return_value = mock_response

        stats = api.get_contributor_stats("test_owner", "test_repo")
        assert stats == [
            {"author": {"login": "user1"}, "total": 50},
            {"author": {"login": "user2"}, "total": 30},
        ]

        mock_request.assert_called_once_with(
            "GET",
            "https://api.github.com/repos/test_owner/test_repo/stats/contributors",
            params=None,
            json=None
        )


def test_get_contributor_stats_failure(api):
    with patch.object(api.session, "request") as mock_request:
        mock_response = Mock()
        mock_response.status_code = 404
        mock_request.return_value = mock_response

        with pytest.raises(GitHubAPIError):
            api.get_contributor_stats("test_owner", "test_repo")


def test_get_weekly_commits_success(api):
    with patch.object(api.session, "request") as mock_request:
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"all": [10, 20, 30], "owner": [5, 10, 15]}
        mock_request.return_value = mock_response

        commits = api.get_weekly_commits("test_owner", "test_repo")
        assert commits == {"all": [10, 20, 30], "owner": [5, 10, 15]}

        mock_request.assert_called_once_with(
            "GET",
            "https://api.github.com/repos/test_owner/test_repo/stats/participation",
            params=None,
            json=None,
        )


def test_get_weekly_commits_failure(api):
    with patch.object(api.session, "request") as mock_request:
        mock_response = Mock()
        mock_response.status_code = 500
        mock_request.return_value = mock_response

        with pytest.raises(GitHubAPIError):
            api.get_weekly_commits("test_owner", "test_repo")


def test_get_punch_card_success(api):
    with patch.object(api.session, "request") as mock_request:
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = [[0, 0, 5], [0, 1, 10], [1, 0, 15]]
        mock_request.return_value = mock_response
        punch_card = api.get_punch_card("test_owner", "test_repo")
        assert punch_card == [[0, 0, 5], [0, 1, 10], [1, 0, 15]]

        mock_request.assert_called_once_with(
            "GET",
            "https://api.github.com/repos/test_owner/test_repo/stats/punch_card",
            params=None,
            json=None,
        )


def test_get_punch_card_failure(api):
    with patch.object(api.session, "request") as mock_request:
        mock_response = Mock()
        mock_response.status_code = 404
        mock_request.return_value = mock_response

        with pytest.raises(GitHubAPIError):
            api.get_punch_card("test_owner", "test_repo")
