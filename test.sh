#!/bin/bash

# Set your GitHub API token here or export it as an environment variable
# export GITHUB_API_TOKEN="your_token_here"

# Define colors for output
GREEN='\033[0;32m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Function to run a command and check its exit status
run_test() {
    echo -e "${GREEN}Running: $1${NC}"
    eval $1
    if [ $? -eq 0 ]; then
        echo -e "${GREEN}Test passed${NC}"
    else
        echo -e "${RED}Test failed${NC}"
    fi
    echo
}

# Repository commands
run_test "python -m github_metrics_api --format pretty repo pytorch pytorch info"
run_test "python -m github_metrics_api --format json repo pytorch pytorch contributors"
run_test "python -m github_metrics_api repo pytorch pytorch languages"
run_test "python -m github_metrics_api repo pytorch pytorch readme"
run_test "python -m github_metrics_api repo pytorch pytorch issues"
run_test "python -m github_metrics_api repo pytorch pytorch pulls"
run_test "python -m github_metrics_api repo pytorch pytorch stats"
run_test "python -m github_metrics_api repo pytorch pytorch commit_activity"
run_test "python -m github_metrics_api repo pytorch pytorch code_frequency"
run_test "python -m github_metrics_api repo pytorch pytorch contributors_stats"
run_test "python -m github_metrics_api repo pytorch pytorch weekly_commits"
run_test "python -m github_metrics_api repo pytorch pytorch punch_card"

# User commands
run_test "python -m github_metrics_api user torvalds info"
run_test "python -m github_metrics_api user torvalds repos"
run_test "python -m github_metrics_api user torvalds gists"

# Organization commands
run_test "python -m github_metrics_api org microsoft info"
run_test "python -m github_metrics_api org microsoft repos"

# Search commands
run_test "python -m github_metrics_api search repos 'machine learning' --sort stars --order desc"
run_test "python -m github_metrics_api search issues 'bug in pytorch' --sort created --order desc"

echo -e "${GREEN}All tests completed${NC}"