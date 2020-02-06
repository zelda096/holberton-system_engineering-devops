#!/usr/bin/python3
"""Find the number of subs"""
import requests


def number_of_subscribers(subreddit):
    """ show the number of subscribers in a subreddit """
    if subreddit is None or type(subreddit) is not str:
        return 0
    # Change the user agent
    try:
        headers = {'User-Agent': 'cmmolanos'}
        request = requests.get('https://api.reddit.com/r/{}/about'.
                               format(subreddit),
                               headers=headers)
        subscribers = request.json()

        sub = subscribers['data']['subscribers']
        return sub
    except:
        return 0
