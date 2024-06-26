from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="github_metrics_api",
    version="0.1.0",
    author="Subash Basnet",
    author_email="subash.basnet0123@gmail.com",
    description="A Python module to fetch various metrics using the GitHub API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/github_metrics_api",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    python_requires=">=3.6",
    install_requires=[
        "requests>=2.25.1",
    ],
    entry_points={
        "console_scripts": [
            "github-metrics=github_metrics_api.cli:main",
        ],
    },
)
