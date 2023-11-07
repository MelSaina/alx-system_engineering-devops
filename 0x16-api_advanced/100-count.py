#!/usr/bin/python3
""" Module for storing the count_words function. """

import requests

def count_words(subreddit, word_list, after=None, counts=None):
    if counts is None:
        counts = {}
    
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'my_bot/1.0'}  # Set a custom User-Agent to avoid Too Many Requests errors
    params = {'limit': 100, 'after': after}

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']

        for post in posts:
            title = post['data']['title'].lower()
            words = title.split()

            for word in word_list:
                if word.lower() in words:
                    if word in counts:
                        counts[word] += 1
                    else:
                        counts[word] = 1

        next_page = data['data']['after']
        if next_page is not None:
            return count_words(subreddit, word_list, after=next_page, counts=counts)
    elif len(counts) > 0:
        # Print the results in descending order by count and ascending order by word
        sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
        for word, count in sorted_counts:
            print(f"{word}: {count}")
    else:
        print("No posts match or the subreddit is invalid.")

if __name__ == '__main__':
    import sys

    if len(sys.argv) < 3:
        print("Usage: {} <subreddit> <list of keywords>".format(sys.argv[0]))
        print("Ex: {} programming 'python java javascript'".format(sys.argv[0]))
    else:
        subreddit = sys.argv[1]
        word_list = [x.lower() for x in sys.argv[2].split()]
        count_words(subreddit, word_list)
