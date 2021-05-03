#!/usr/bin/python3
"""Gather data from an API"""
import requests
from sys import argv, exit

if __name__ == "__main__":
    if len(argv) < 2:
        print("Usage: {} <employeeID>".format(argv[0]))
        exit()

    userId = argv[1]
    site = 'https://jsonplaceholder.typicode.com/'
    to_dos = requests.get(site + 'todos?userId={}'.format(userId)).json()
    done = [t['title'] for t in to_dos if t['completed'] is True]
    user = requests.get(site + 'users?id={}'.format(userId)).json()
    name = user[0].get('name')
    print('Employee {} is done with tasks({}/{}):'.format(name, len(done),
                                                          len(to_dos)))
    for task in done:
        print('\t {}'.format(task))
