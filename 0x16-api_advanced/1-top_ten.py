#!/usr/bin/python3
"""
Function that queries the Reddit API and prints the titles
of the first 10 hot posts listed for a given subreddit.
"""

import requests

def top_ten(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'my_bot/1.0'}  # Set a custom User-Agent to avoid Too Many Requests errors

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']

        if len(posts) == 0:
            print("No posts found in this subreddit.")
        else:
            for i, post in enumerate(posts[:10]):
                print(f"{i + 1}: {post['data']['title']}")

    else:
        print("None")  # Invalid subreddit or other error

if __name__ == '__main__':
    import sys

    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        subreddit = sys.argv[1]
        top_ten(subreddit)
