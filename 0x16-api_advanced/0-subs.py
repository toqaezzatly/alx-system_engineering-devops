#!/usr/bin/python3
import requests
<<<<<<< HEAD
=======


def number_of_subscribers(subreddit):
    """Queries the Reddit API and returns the number of subscribers for a given subreddit.
>>>>>>> 664973be384d442d1dfc7d0b47c232a645421fb5

def number_of_subscribers(subreddit):
    """Queries the Reddit API and returns the number of subscribers for a given subreddit.
    
    Args:
        subreddit (str): The name of the subreddit.
        
    Returns:
        int: The number of subscribers. Returns 0 if the subreddit is invalid or an error occurs.
    """
    if not isinstance(subreddit, str) or subreddit == "":
        return 0
<<<<<<< HEAD
    
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {
        'User-Agent': 'python:my_reddit_script:v1.0.0 (by /u/my_username)'
    }
    
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        
        # Debugging: Print the status code and content of the response
        print(f"Status Code: {response.status_code}")
        print(f"Response Content: {response.content}")
        
=======

    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'custom-agent'}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)

>>>>>>> 664973be384d442d1dfc7d0b47c232a645421fb5
        if response.status_code == 200:
            data = response.json().get('data', {})
            return data.get('subscribers', 0)
        else:
            return 0
<<<<<<< HEAD
    except requests.RequestException as e:
        # Debugging: Print the exception message
        print(f"RequestException: {e}")
        return 0

=======
    except requests.RequestException:
        return 0
>>>>>>> 664973be384d442d1dfc7d0b47c232a645421fb5
