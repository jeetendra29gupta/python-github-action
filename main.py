import datetime

import requests


def main():
    print(f"Hello from GitHub Actions! Today's date and time is: {datetime.datetime.now()}")


def get_joke():
    """Fetches a Chuck Norris joke from an API."""
    try:
        response = requests.get("https://api.chucknorris.io/jokes/random", timeout=5)
        response.raise_for_status()  # Raise an exception for bad status codes
        joke_data = response.json()
        print(f"Here's a Chuck Norris joke: {joke_data['value']}")
    except requests.RequestException as e:
        print(f"An error occurred: {e}")


if __name__ == '__main__':
    main()
    get_joke()
