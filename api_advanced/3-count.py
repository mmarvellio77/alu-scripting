#!/usr/bin/python3
"""Recursively count keyword occurrences in a subreddit's hot titles."""
import requests


def parse_titles(subreddit, titles=[], after=None):
    """Recursively collect the titles of all hot articles of a subreddit."""
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

    collected = [post.get("data", {}).get("title", "") for post in children]

    next_after = data.get("after")
    if next_after is None:
        return titles + collected

    return parse_titles(subreddit, titles + collected, next_after)


def tally_words(words, keywords, counter):
    """Recursively count keyword occurrences in a list of words."""
    if not words:
        return counter

    word = words[0].lower()
    if word in keywords:
        counter[word] = counter.get(word, 0) + 1

    return tally_words(words[1:], keywords, counter)


def tally_titles(titles, keywords, counter, index=0):
    """Recursively count keyword occurrences across every title."""
    if index >= len(titles):
        return counter

    tally_words(titles[index].split(), keywords, counter)

    return tally_titles(titles, keywords, counter, index + 1)


def print_results(results):
    """Recursively print the sorted (word, count) results."""
    if not results:
        return

    word, count = results[0]
    print("{}: {}".format(word, count))

    print_results(results[1:])


def count_words(subreddit, word_list):
    """Print a sorted count of the given keywords found in hot titles."""
    titles = parse_titles(subreddit)
    if titles is None:
        return

    keywords = [word.lower() for word in word_list]

    counter = tally_titles(titles, keywords, {})

    results = [(word, count) for word, count in counter.items() if count]
    results.sort(key=lambda item: (-item[1], item[0]))

    print_results(results)
