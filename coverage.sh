#!/bin/bash
# # Run all tests
# pytest

# # Run tests with verbose output
# pytest -v

# Run tests and show coverage report
pytest --cov=github_metrics_api

# # Run a specific test file
# pytest github_metrics_api/test/test_api.py

# # Run a specific test function
# pytest github_metrics_api/test/test_api.py::test_get_repo_stats_success