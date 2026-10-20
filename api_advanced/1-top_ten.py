#!/usr/bin/python3
"""Query the Reddit API and print the first 10 hot posts of a subreddit."""
import requests


def top_ten(subreddit):
    """Print the titles of the first 10 hot posts of a given subreddit.

    Prints None if the subreddit is invalid.
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        "User-Agent": "linux:alu.api.advanced:v1.0 (by /u/mmarvellio77)"
    }
    params = {"limit": 10}

    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    if response.status_code != 200:
        print("None")
        return

    children = (response.json().get("data") or {}).get("children")
    if not children:
        print("None")
        return

    for post in children[:10]:
        print((post.get("data") or {}).get("title"))
