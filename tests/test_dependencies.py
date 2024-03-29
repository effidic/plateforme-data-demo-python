"""
This module describe the tests of dependancies
"""

import toml
import pytest

# Load the pyproject.toml file
pyproject_toml = toml.load("pyproject.toml")

# Get the "dev-dependencies" section
dependencies = pyproject_toml.get("tool", {}).get("poetry", {})
dependencies = dependencies.get("dependencies", {})

dev_dependencies = pyproject_toml.get("tool", {}).get("poetry", {})
dev_dependencies = dev_dependencies.get("dev-dependencies", {})


def test_google_cloud():
    """
    Test if 'google-cloud'
    is defined as a dependency with the correct version.
    """
    google_cloud = dependencies.get("google-cloud")
    assert google_cloud is not None


def test_additional_dependencies():
    """
    Test if additional dependencies have the correct versions specified.
    """
    assert dependencies.get("flake8") is not None
    assert dependencies.get("python-dotenv") is not None


if __name__ == "__main__":
    pytest.main()
