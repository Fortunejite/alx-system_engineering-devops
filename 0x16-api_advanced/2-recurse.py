#!/usr/bin/python3
import requests

def recurse(subreddit, hot_list=[], after=None):
    """Returns a list of all hot articles for a given subreddit"""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    response = requests.get(url)
    params = {}
    if after:
        params["after"] = after
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        posts = data["data"]["children"]
        for post in posts:
            hot_list.append(post["data"]["title"])
        if data["data"]["after"] is not None:
            return recurse(subreddit, hot_list, data["data"]["after"])
        else:
            return hot_list
    return None