#!/usr/bin/python3
"""Gather data from an API and export in CVS format"""
import requests
from sys import argv, exit

if __name__ == "__main__":
    if len(argv) < 2:
        print("Usage: {} <employeeID>".format(argv[0]))
        exit()

    userId = argv[1]
    site = 'https://jsonplaceholder.typicode.com/'
    user = requests.get(site + 'users?id={}'.format(userId)).json()
    if not user:
        print("No employee record found for ID: {}".format(userId))
        exit()
    username = user[0].get('username')
    to_dos = requests.get(site + 'todos?userId={}'.format(userId)).json()

    with open('{}.cvs'.format(userId), 'w') as out:
        for task in to_dos:
            out.write('"{}","{}","{}","{}"\n'.format(userId, username,
                                                     task.get('completed'),
                                                     task.get('title')))
