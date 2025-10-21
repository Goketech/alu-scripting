#!/usr/bin/python3
"""Prints the title of the first 10 hot posts listed for a given subreddit"""
import requests


def top_ten(subreddit):
    """Prints the title of the first 10 hot posts listed for a given subreddit"""
    reddit_url = "https://www.reddit.com/r/{}/hot.json" \
        .format(subreddit)
    headers = headers = {'User-agent': 'Mozilla/5.0'}
    response = requests.get(reddit_url, headers=headers)

    if response.status_code == 200:
        data = response.json()['data']
        for post in data['children'][:10]:
            print(post['data']['title'])
    else:
        print(None)
