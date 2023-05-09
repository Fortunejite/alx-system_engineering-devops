#!/usr/bin/python3
import requests

def number_of_subscribers(subreddit):
    """Returns the number of subscribers for a given subreddit"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    response = requests.get(url)
    if response.status_code == 200:
        return response.json().get("data").get("subscribers")
    return 0