#!/usr/bin/python3
"""Find the number of subs"""
import requests


def recurse(subreddit, hot_list=[], after=""):
    """ show the top 10 posts in a subreddit """
    try:
        # Change the user agent
        headers = {'User-Agent': 'cmmolanos'}
        payload = {'t': 'all', 'after': after}
        request = requests.get('https://api.reddit.com/r/{}/hot'.
                               format(subreddit), headers=headers,
                               params=payload)
        top_posts = request.json()

        for post in top_posts['data']['children']:
            hot_list.append(post['data']['title'])

        after = top_posts['data']['after']
        # print(after)
        if after is not None:
            recurse(subreddit, hot_list, after)
        return hot_list
    except:
        return None

    """    while (top_posts['data']['after'] is not None):
        print(after)
        headers = {'User-Agent': 'cmmolanos'}
        payload = {'t': 'all', 'after': after}
        request = requests.get('https://api.reddit.com/r/{}/top'.
                               format(subreddit), headers=headers,
                               params=payload)
        top_posts = request.json()
        for post in top_posts['data']['children']:
            hot_list.append(post['data']['title'])
        after = top_posts['data']['after']
    return hot_list """
