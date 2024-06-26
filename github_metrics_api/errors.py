class GitHubAPIError(Exception):
    """Base exception for GitHub API errors"""

    def __init__(self, message, code):
        self.message = message
        self.code = code
        super().__init__(self.message)


class RateLimitExceededError(GitHubAPIError):
    """Raised when the GitHub API rate limit is exceeded"""

    def __init__(self, message="GitHub API rate limit exceeded"):
        super().__init__(message, code="RATE_LIMIT_EXCEEDED")


class AuthenticationError(GitHubAPIError):
    """Raised when there's an authentication error with the GitHub API"""

    def __init__(self, message="Invalid GitHub token"):
        super().__init__(message, code="AUTHENTICATION_ERROR")


class NotFoundError(GitHubAPIError):
    """Raised when the requested resource is not found"""

    def __init__(self, message="Requested resource not found"):
        super().__init__(message, code="NOT_FOUND")


class ServerError(GitHubAPIError):
    """Raised when GitHub API returns a server error"""

    def __init__(self, message="GitHub API server error"):
        super().__init__(message, code="SERVER_ERROR")
