from datetime import datetime


def format_repo_info(repo):
    return f"""Repository Information:
Name: {repo['name']}
Owner: {repo['owner']['login']}
Description: {repo['description'] or 'N/A'}
Stars: {repo['stargazers_count']}
Forks: {repo['forks_count']}
Open Issues: {repo['open_issues_count']}
Language: {repo['language'] or 'N/A'}
Created: {format_date(repo['created_at'])}
Last Updated: {format_date(repo['updated_at'])}
"""


def format_repo_contributors(contributors):
    formatted = "Repository Contributors:\n"
    for contributor in contributors:
        formatted += f"- {contributor['login']} (Contributions: {contributor['contributions']})\n"
    return formatted


def format_repo_languages(languages):
    total = sum(languages.values())
    formatted = "Repository Languages:\n"
    for language, bytes in languages.items():
        percentage = (bytes / total) * 100
        formatted += f"- {language}: {percentage:.1f}% ({bytes} bytes)\n"
    return formatted


def format_repo_readme(readme):
    return f"""Repository README:
Name: {readme['name']}
Size: {readme['size']} bytes
Encoding: {readme['encoding']}
Content: 
{readme['content']}
"""


def format_repo_issues(issues):
    formatted = "Repository Issues:\n"
    for issue in issues:
        formatted += f"""- #{issue['number']}: {issue['title']}
  State: {issue['state']}
  Created: {format_date(issue['created_at'])}
  Comments: {issue['comments']}
  
"""
    return formatted


def format_pull_requests(prs):
    formatted = "Pull Requests:\n"
    for pr in prs:
        formatted += f"""- #{pr['number']}: {pr['title']}
  State: {pr['state']}
  Created: {format_date(pr['created_at'])}
  User: {pr['user']['login']}
  
"""
    return formatted


def format_user_info(user):
    return f"""User Information:
Login: {user['login']}
Name: {user['name'] or 'N/A'}
Bio: {user['bio'] or 'N/A'}
Location: {user['location'] or 'N/A'}
Public Repos: {user['public_repos']}
Followers: {user['followers']}
Following: {user['following']}
Created: {format_date(user['created_at'])}
"""


def format_user_repos(repos):
    formatted = "User Repositories:\n"
    for repo in repos:
        formatted += f"""- {repo['name']}
  Description: {repo['description'] or 'N/A'}
  Stars: {repo['stargazers_count']}
  Forks: {repo['forks_count']}
  Language: {repo['language'] or 'N/A'}
  
"""
    return formatted


def format_user_gists(gists):
    formatted = "User Gists:\n"
    for gist in gists:
        formatted += f"""- {list(gist['files'].keys())[0]}
  Description: {gist['description'] or 'N/A'}
  Created: {format_date(gist['created_at'])}
  Updated: {format_date(gist['updated_at'])}
  Comments: {gist['comments']}
  
"""
    return formatted


def format_org_info(org):
    return f"""Organization Information:
Login: {org['login']}
Name: {org['name'] or 'N/A'}
Description: {org['description'] or 'N/A'}
Location: {org['location'] or 'N/A'}
Public Repos: {org['public_repos']}
Followers: {org['followers']}
Following: {org['following']}
Created: {format_date(org['created_at'])}
"""


def format_org_repos(repos):
    return format_user_repos(repos)  # The format is the same as user repos


def format_search_repos(search_results):
    formatted = f"Search Results (Total: {search_results['total_count']}):\n"
    for repo in search_results["items"]:
        formatted += f"""- {repo['full_name']}
  Description: {repo['description'] or 'N/A'}
  Stars: {repo['stargazers_count']}
  Forks: {repo['forks_count']}
  Language: {repo['language'] or 'N/A'}
  
"""
    return formatted


def format_search_issues(search_results):
    formatted = f"Search Results (Total: {search_results['total_count']}):\n"
    for issue in search_results["items"]:
        formatted += f"""- {issue['title']} (#{issue['number']})
  Repository: {issue['repository_url'].split('/')[-2]}/{issue['repository_url'].split('/')[-1]}
  State: {issue['state']}
  Created: {format_date(issue['created_at'])}
  Comments: {issue['comments']}
  
"""
    return formatted


def format_repo_stats(stats):
    return f"""Repository Statistics:
Stars: {stats['stars']}
Forks: {stats['forks']}
Open Issues: {stats['open_issues']}
Watchers: {stats['watchers']}
"""


def format_commit_activity(activity):
    formatted = "Weekly Commit Activity:\n"
    for week in activity:
        date = datetime.fromtimestamp(week["week"]).strftime("%Y-%m-%d")
        formatted += f"Week of {date}: {week['total']} commits\n"
        formatted += "  Sun: {0}, Mon: {1}, Tue: {2}, Wed: {3}, Thu: {4}, Fri: {5}, Sat: {6}\n".format(
            *week["days"]
        )
    return formatted


def format_code_frequency(frequency):
    formatted = "Weekly Code Frequency:\n"
    for week in frequency:
        date = datetime.fromtimestamp(week[0]).strftime("%Y-%m-%d")
        formatted += f"Week of {date}: +{week[1]} additions, -{week[2]} deletions\n"
    return formatted


def format_contributor_stats(stats):
    formatted = "Contributor Statistics:\n"
    for contributor in stats:
        formatted += f"Username: {contributor['author']['login']}\n"
        formatted += f"  Total Commits: {contributor['total']}\n"
        formatted += "  Weekly Commits:\n"
        for week in contributor["weeks"][-4:]:  # Show only last 4 weeks
            date = datetime.fromtimestamp(week["w"]).strftime("%Y-%m-%d")
            formatted += f"    Week of {date}: {week['c']} commits\n"
        formatted += "\n"
    return formatted


def format_weekly_commits(commits):
    formatted = "Weekly Commit Counts:\n"
    formatted += f"  Owner: {commits['owner']}\n"
    formatted += f"  All: {commits['all']}\n"
    return formatted


def format_punch_card(punch_card):
    days = [
        "Sunday",
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
    ]
    formatted = "Commit Punch Card:\n"
    for day, hour, count in punch_card:
        formatted += f"{days[day]} {hour:02d}:00 - {hour:02d}:59: {count} commits\n"
    return formatted


def format_date(date_string):
    return datetime.strptime(date_string, "%Y-%m-%dT%H:%M:%SZ").strftime(
        "%Y-%m-%d %H:%M:%S"
    )
