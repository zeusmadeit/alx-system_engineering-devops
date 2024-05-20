#!/usr/bin/python3
"""
This script uses a REST API, for a given employee ID, 
returns information about his/her TODO list progress.
"""
import requests as req
from sys import argv

if __name__ == "__main__":
    baseUrl = "https://jsonplaceholder.typicode.com/users"
    url = f"{baseUrl}/{argv[1]}"

    response = req.get(url)
    employeeName = response.json().get('name')

    todoUrl = url + "/todos"
    response = req.get(todoUrl)

    tasks = response.json()
    done = 0
    done_tasks = []

    for task in tasks:
        if task.get('completed'):
            done_tasks.append(task)
            done += 1

    print("Employee {} is done with tasks({}/{}):"
          .format(employeeName, done, len(tasks)))

    for task in done_tasks:
        print("\t {}".format(task.get('title')))
