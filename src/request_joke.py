import requests


def get_joke():
    """Fetches a Chuck Norris joke from an API."""
    try:
        response = requests.get("https://api.chucknorris.io/jokes/random", timeout=5)
        response.raise_for_status()  # Raise an exception for bad status codes
        joke_data = response.json()
        return joke_data['value']
    except requests.RequestException as e:
        print(f"An error occurred: {e}")
        return None


if __name__ == "__main__":
    joke = get_joke()
    if joke:
        print(f"Here's a Chuck Norris joke: {joke}")
