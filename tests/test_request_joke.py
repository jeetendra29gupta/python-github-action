from unittest.mock import patch, Mock

from request_joke import get_joke


def test_get_joke_success():
    """Tests that get_joke() prints a joke on a successful API call."""
    # We need to mock the requests.get() call to avoid making a real API request
    # and ensure our test is fast and reliable.
    with patch('requests.get') as mock_get:
        # Configure the mock object to return a successful response
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"value": "Test joke from pytest."}
        mock_get.return_value = mock_response

        joke = get_joke()
        assert joke == "Test joke from pytest."
