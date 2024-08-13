#!/usr/bin/python3
import requests
def number_of_subscribers(subreddit):
    """Return the number of subscribers for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        int: The number of subscribers, or 0 if the subreddit is invalid.
    """
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }

    try:
        response = requests.get(url, headers=headers, allow_redirects=True)
        if response.status_code == 200:
            data = response.json()
            return data.get(data, {}).get('subscribers', 0)
        else:
            return 0
    except Exception:
        return 0