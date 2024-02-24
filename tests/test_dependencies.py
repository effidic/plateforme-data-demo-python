"""
This module describe the tests of dependancies
"""
import toml
import pytest

# Load the pyproject.toml file
pyproject_toml = toml.load("pyproject.toml")

# Get the "dev-dependencies" section
dependencies = pyproject_toml.get("tool", {}).get("poetry", {}).get("dependencies", {})
dev_dependencies = (
    pyproject_toml.get("tool", {}).get("poetry", {}).get("dev-dependencies", {})
)


def test_snowflake_sqlalchemy():
    """
    Test if 'snowflake-sqlalchemy'
    is defined as a dependency with the correct version.
    """
    snowflake_sqlalchemy = dependencies.get("snowflake-sqlalchemy")
    assert snowflake_sqlalchemy is not None
    assert snowflake_sqlalchemy == "1.4.7"


def test_additional_dependencies():
    """
    Test if additional dependencies have the correct versions specified.
    """
    assert dependencies.get("pandas") == "1.5.3"
    assert dependencies.get("python-dotenv") == "1.0.0"


if __name__ == "__main__":
    pytest.main()
