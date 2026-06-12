import pytest
from unittest.mock import patch, MagicMock
from github_client import get_public_repo_count


@patch("github_client.requests.get")
def test_get_public_repo_count_success(mock_get):
    # create a fake response object
    fake_response = MagicMock()
    fake_response.status_code = 200

    # tell fake response what its fake JSON dictionary looks like
    fake_response.json.return_value = {"public_repos": 14}


    # intercept requests.get and hand back the fake response instead
    mock_get.return_value = fake_response

    # execute the final code 
    result = get_public_repo_count("someuser")

    # assertions
    assert result == 14

@patch('github_client.requests.get')
def test_get_public_repo_count_failure(mock_get):
    # setup a failing mock response
    fake_response = MagicMock()
    fake_response.status_code = 404
    mock_get.response_value = fake_response

    with pytest.raises(ValueError):
        get_public_repo_count("nonexistent-user")