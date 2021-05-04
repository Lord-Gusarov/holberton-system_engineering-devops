#!/usr/bin/python3
"""Gather data from an API and exports data in the JSON format."""
import json
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
    out_to_dos = []
    for task in to_dos:
        my_task = {
                'task': task.get('title'),
                'completed': task.get('completed'),
                'username': username
                }
        out_to_dos.append(my_task)
    record = {userId: out_to_dos}

    with open('{}.json'.format(userId), 'w') as outfile:
        json.dump(record, outfile)
