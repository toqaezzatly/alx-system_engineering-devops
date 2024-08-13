#!/usr/bin/python3
import requests


def number_of_subscribers(subreddit):
    """Queries the Reddit API and returns the number of subscribers for a given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'custom-agent'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json().get('data', {})
        return data.get('subscribers', 0)
    return 0
