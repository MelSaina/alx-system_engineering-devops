#!/usr/bin/python3
"""
Recursive function that queries the Reddit API and returns
a list containing the titles of all hot articles for a given subreddit.
If no results are found for the given subreddit,
the function should return None.
"""

import requests

def recurse(subreddit, hot_list=[], after=None):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'my_bot/1.0'}  # Set a custom User-Agent to avoid Too Many Requests errors
    params = {'limit': 100, 'after': after}

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']

        if len(posts) == 0:
            return hot_list
        else:
            hot_list.extend([post['data']['title'] for post in posts])

            # Recursively call the function with the 'after' parameter for pagination
            next_page = data['data']['after']
            if next_page is not None:
                return recurse(subreddit, hot_list, after=next_page)
            else:
                return hot_list
    else:
        return None  # Invalid subreddit or other error

if __name__ == '__main__':
    import sys

    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        subreddit = sys.argv[1]
        result = recurse(subreddit)
        if result is not None:
            print(len(result))
        else:
            print("None")
