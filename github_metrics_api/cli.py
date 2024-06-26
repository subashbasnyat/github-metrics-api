import argparse
import json
import os
from dotenv import load_dotenv
from .api import GitHubMetricsAPI
from .errors import GitHubAPIError
from .formatters import (
    format_repo_info,
    format_repo_contributors,
    format_repo_languages,
    format_repo_readme,
    format_repo_issues,
    format_pull_requests,
    format_user_info,
    format_user_repos,
    format_user_gists,
    format_org_info,
    format_org_repos,
    format_search_repos,
    format_search_issues,
    format_repo_stats,
    format_commit_activity,
    format_code_frequency,
    format_contributor_stats,
    format_weekly_commits,
    format_punch_card,
)

load_dotenv()


def main():
    parser = argparse.ArgumentParser(description="Fetch GitHub metrics and data")
    parser.add_argument(
        "--token", help="GitHub API token", default=os.getenv("GITHUB_API_TOKEN")
    )
    parser.add_argument(
        "--format",
        choices=["json", "pretty"],
        default="pretty",
        help="Output format (default: pretty)",
    )

    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Repository commands
    repo_parser = subparsers.add_parser("repo", help="Repository-related commands")
    repo_parser.add_argument("owner", help="Repository owner")
    repo_parser.add_argument("repo", help="Repository name")
    repo_parser.add_argument(
        "action",
        choices=[
            "info",
            "contributors",
            "languages",
            "readme",
            "issues",
            "pulls",
            "stats",
            "commit_activity",
            "code_frequency",
            "contributors_stats",
            "weekly_commits",
            "punch_card",
        ],
        help="Action to perform on the repository",
    )

    # User commands
    user_parser = subparsers.add_parser("user", help="User-related commands")
    user_parser.add_argument("username", help="GitHub username")
    user_parser.add_argument(
        "action",
        choices=["info", "repos", "gists"],
        help="Action to perform on the user",
    )

    # Organization commands
    org_parser = subparsers.add_parser("org", help="Organization-related commands")
    org_parser.add_argument("org", help="Organization name")
    org_parser.add_argument(
        "action",
        choices=["info", "repos"],
        help="Action to perform on the organization",
    )

    # Search commands
    search_parser = subparsers.add_parser("search", help="Search-related commands")
    search_parser.add_argument(
        "type", choices=["repos", "issues"], help="Type of search to perform"
    )
    search_parser.add_argument("query", help="Search query")
    search_parser.add_argument("--sort", help="Sort parameter")
    search_parser.add_argument("--order", choices=["asc", "desc"], help="Sort order")

    args = parser.parse_args()

    api = GitHubMetricsAPI(access_token=args.token)

    try:
        if args.command == "repo":
            if args.action == "info":
                data = api.get_repo(args.owner, args.repo)
                if args.format == "pretty":
                    data = format_repo_info(data)
            elif args.action == "contributors":
                data = api.list_repo_contributors(args.owner, args.repo)
                if args.format == "pretty":
                    data = format_repo_contributors(data)
            elif args.action == "languages":
                data = api.list_repo_languages(args.owner, args.repo)
                if args.format == "pretty":
                    data = format_repo_languages(data)
            elif args.action == "readme":
                data = api.get_repo_readme(args.owner, args.repo)
                if args.format == "pretty":
                    data = format_repo_readme(data)
            elif args.action == "issues":
                data = api.list_repo_issues(args.owner, args.repo)
                if args.format == "pretty":
                    data = format_repo_issues(data)
            elif args.action == "pulls":
                data = api.list_pull_requests(args.owner, args.repo)
                if args.format == "pretty":
                    data = format_pull_requests(data)
            elif args.action == "stats":
                data = api.get_repo_stats(args.owner, args.repo)
                if args.format == "pretty":
                    data = format_repo_stats(data)
            elif args.action == "commit_activity":
                data = api.get_commit_activity(args.owner, args.repo)
                if args.format == "pretty":
                    data = format_commit_activity(data)
            elif args.action == "code_frequency":
                data = api.get_code_frequency(args.owner, args.repo)
                if args.format == "pretty":
                    data = format_code_frequency(data)
            elif args.action == "contributors_stats":
                data = api.get_contributor_stats(args.owner, args.repo)
                if args.format == "pretty":
                    data = format_contributor_stats(data)
            elif args.action == "weekly_commits":
                data = api.get_weekly_commits(args.owner, args.repo)
                if args.format == "pretty":
                    data = format_weekly_commits(data)
            elif args.action == "punch_card":
                data = api.get_punch_card(args.owner, args.repo)
                if args.format == "pretty":
                    data = format_punch_card(data)

        elif args.command == "user":
            if args.action == "info":
                data = api.get_user(args.username)
                if args.format == "pretty":
                    data = format_user_info(data)
            elif args.action == "repos":
                data = api.list_user_repos(args.username)
                if args.format == "pretty":
                    data = format_user_repos(data)
            elif args.action == "gists":
                data = api.list_user_gists(args.username)
                if args.format == "pretty":
                    data = format_user_gists(data)

        elif args.command == "org":
            if args.action == "info":
                data = api.get_organization(args.org)
                if args.format == "pretty":
                    data = format_org_info(data)
            elif args.action == "repos":
                data = api.list_org_repos(args.org)
                if args.format == "pretty":
                    data = format_org_repos(data)

        elif args.command == "search":
            if args.type == "repos":
                data = api.search_repositories(
                    args.query, sort=args.sort, order=args.order
                )
                if args.format == "pretty":
                    data = format_search_repos(data)
            elif args.type == "issues":
                data = api.search_issues(args.query, sort=args.sort, order=args.order)
                if args.format == "pretty":
                    data = format_search_issues(data)

        if args.format == "json":
            print(json.dumps(data, indent=2))
        else:
            print(data)

    except GitHubAPIError as e:
        print(f"Error: {e.message} (Code: {e.code})")


if __name__ == "__main__":
    main()
