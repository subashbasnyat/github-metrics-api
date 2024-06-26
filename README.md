# GitHub Metrics API

GitHub Metrics API is a Python module that allows you to fetch various metrics from GitHub repositories using the GitHub API. It provides an easy-to-use interface for retrieving repository statistics and commit activity.

## Installation

You can install the GitHub Metrics API using pip:

```bash
pip install github-metrics-api
```

## Usage

### As a Python module

```python
from github_metrics_api import GitHubMetricsAPI

# Initialize the API (with an optional access token)
api = GitHubMetricsAPI(access_token="your_github_token")

# Get repository stats
stats = api.get_repo_stats("owner", "repo")
print(stats)

# Get commit activity
commit_activity = api.get_commit_activity("owner", "repo")
print(commit_activity)
```

## Development

### Setting up the development environment

1. Clone the repository
2. Create a virtual environment: `python -m venv venv`
3. Activate the virtual environment:
   - On Windows: `venv\Scripts\activate`
   - On macOS and Linux: `source venv/bin/activate`
4. Install the development dependencies: `pip install -r requirements.txt`

### Running tests

To run the tests with coverage reporting:

```bash
./coverage.sh
```

This will run all the tests and display a coverage report, showing which lines of code are covered by the tests and which are not.

### Command-line interface

The module also provides a command-line interface:

```bash
github-metrics [--format {'pretty', 'json'}][--token YOUR_GITHUB_TOKEN] repo <owner> <repo> {info,contributors,languages,readme,issues,pulls,stats,commit_activity,code_frequency,contributors_stats,weekly_commits,punch_card}

github-metrics [--format {'pretty', 'json'}][--token YOUR_GITHUB_TOKEN] user <username> {info,repos,gists}

github-metrics [--format {'pretty', 'json'}][--token YOUR_GITHUB_TOKEN] org <org> {info,repos}

github-metrics [--format {'pretty', 'json'}][--token YOUR_GITHUB_TOKEN] search {repos,issues} <query> --sort <parameter> --order {asc,desc}
```

Example:

```bash
github-metrics --format pretty --token 213123132 repo pytorch pytorch info

github-metrics --format pretty --token 213123132 user torvalds info

github-metrics --format pretty --token 213123132 org microsoft info

github-metrics --format pretty --token 213123132 search repos 'machine learning' --sort stars --order desc
```

## Features

- Fetch repository statistics (stars, forks, open issues, watchers)
- Retrieve commit activity for the last 52 weeks
- Easy-to-use Python API
- Command-line interface for quick access to metrics

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.