#!/usr/bin/python3
import requests

def top_ten(subreddit):
    """Returns the top ten hot posts for a given subreddit"""
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    response = requests.get(url)
    if response.status_code == 200:
        for post in response.json().get("data").get("children"):
            print(post.get("data").get("title"))
        return
    print("None")
    return