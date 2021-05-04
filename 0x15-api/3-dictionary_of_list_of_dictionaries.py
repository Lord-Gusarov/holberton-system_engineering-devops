#!/usr/bin/python3
"""Records all tasks from all employees, data obtain from an API and
exported in the JSON format."""
import json
import requests
from sys import argv, exit

if __name__ == "__main__":
    site = 'https://jsonplaceholder.typicode.com/'
    users = requests.get(site + 'users').json()
    if not users:
        print("No employee records found.")
        exit()

    record = dict()
    for user in users:
        userId = user.get('id')
        to_dos = requests.get(site + 'todos?userId={}'.format(userId)).json()
        out_to_dos = []
        for task in to_dos:
            my_task = {
                    'username': user.get('username'),
                    'task': task.get('title'),
                    'completed': task.get('completed')
                    }
            out_to_dos.append(my_task)
        record[userId] = out_to_dos

    with open('todo_all_employees.json', 'w') as outfile:
        json.dump(record, outfile)
