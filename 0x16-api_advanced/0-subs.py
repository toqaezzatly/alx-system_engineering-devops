#!/usr/bin/python3
import requests

def number_of_subscribers(subreddit):
    """Queries the Reddit API and returns the number of subscribers for a given subreddit.
    
    Args:
        subreddit (str): The name of the subreddit.
        
    Returns:
        int: The number of subscribers. Returns 0 if the subreddit is invalid or an error occurs.
    """
    if not isinstance(subreddit, str) or subreddit == "":
        return 0
    
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {
        'User-Agent': 'python:my_reddit_script:v1.0.0 (by /u/my_username)'
    }
    
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        
        # Debugging: Print the status code and content of the response
        print(f"Status Code: {response.status_code}")
        print(f"Response Content: {response.content}")
        
        if response.status_code == 200:
            data = response.json().get('data', {})
            return data.get('subscribers', 0)
        else:
            return 0
    except requests.RequestException as e:
        # Debugging: Print the exception message
        print(f"RequestException: {e}")
        return 0

