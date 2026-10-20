#!/usr/bin/python3
"""Recursively gather the titles of all hot articles of a subreddit."""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """Return a list of titles of all hot articles for a subreddit.

    Returns None if the subreddit is invalid or has no results.
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        "User-Agent": "linux:alu.api.advanced:v1.0 (by /u/mmarvellio77)"
    }
    params = {"limit": 100, "after": after}

    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    if response.status_code != 200:
        return None

    data = response.json().get("data") or {}
    children = data.get("children")
    if children is None:
        return None

    titles = [post.get("data", {}).get("title") for post in children]

    next_after = data.get("after")
    if next_after is None:
        if not titles and not hot_list:
            return None
        hot_list.extend(titles)
        return hot_list

    return recurse(subreddit, hot_list + titles, next_after)
