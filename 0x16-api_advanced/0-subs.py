#!/usr/bin/python3
"""Gather data from an API and exports data in the JSON format."""
import json
import requests


def number_of_subscribers(subreddit):
    """ Fetches thye number of subscribers"""
    site = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    head = {'User-Agent': 'My Super Agetnt'}
    response = requests.get(site, headers=head)
    try:
        if response.status_code != 200:
            return 0
        return response.json()['data']['subscribers']
    except:
        return 0
