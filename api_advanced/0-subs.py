#!/usr/bin/python3
"""Query the Reddit API and return the number of subscribers."""
import requests


def number_of_subscribers(subreddit):
    """Return the total number of subscribers for a given subreddit.

    Returns 0 if the subreddit is invalid.
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "linux:alu.api.advanced:v1.0 (by /u/mmarvellio77)"
    }

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        return 0

    data = response.json().get("data")
    if not data:
        return 0

    return data.get("subscribers", 0)
