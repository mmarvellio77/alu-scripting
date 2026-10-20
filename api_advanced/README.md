# API Advanced

Advanced API scripting tasks.

## Files

| File | Description |
| --- | --- |
| [0-subs.py](./0-subs.py) | `number_of_subscribers(subreddit)` — queries the Reddit API and returns the total number of subscribers for a subreddit, or `0` if the subreddit is invalid. |
| [1-top_ten.py](./1-top_ten.py) | `top_ten(subreddit)` — prints the titles of the first 10 hot posts of a subreddit, or `None` if the subreddit is invalid. |

## Usage

```python
#!/usr/bin/python3
import sys

if __name__ == '__main__':
    number_of_subscribers = __import__('0-subs').number_of_subscribers
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        print("{:d}".format(number_of_subscribers(sys.argv[1])))
```

```bash
$ python3 0-main.py programming
756024
$ python3 0-main.py this_is_a_fake_subreddit
0
```

```bash
$ python3 1-main.py programming
Firebase founder's response to last week's "Firebase Costs increased by 7000%!"
How a 64k intro is made
...
$ python3 1-main.py this_is_a_fake_subreddit
None
```

## Notes

- A custom `User-Agent` is set to avoid `Too Many Requests` errors.
- Redirects are not followed, since invalid subreddits redirect to search results.

Requirements:

- Python 3
- `requests` (`pip install requests`)
