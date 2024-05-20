#!/usr/bin/python3
"""Accessing a REST API for todo lists of employees"""

import requests
from sys import argv

if __name__ == "__main__":
    employeeId = argv[1]
    baseUrl = "https://jsonplaceholder.typicode.com/users"
    url = f"{baseUrl}/{employeeId}"

    response = requests.get(url)
    username = response.json().get('username')

    todoUrl = url + "/todos"
    response = requests.get(todoUrl)
    tasks = response.json()

    with open('{}.csv'.format(employeeId), 'w') as file:
        for task in tasks:
            file.write('"{}","{}","{}","{}"\n'
                       .format(employeeId, username, task.get('completed'),
                               task.get('title')))
