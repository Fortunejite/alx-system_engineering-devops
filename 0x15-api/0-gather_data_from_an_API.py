#!/usr/bin/python3
"""Gets the TODO lists of an employee in a predefines url"""

import requests
import sys

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Error: Please provide an employee ID as a command-line argument.")
        sys.exit(1)

    try:
        id = int(sys.argv[1])
    except ValueError:
        print("Error: Employee ID must be an integer.")
        sys.exit(1)

    user_uri = 'https://jsonplaceholder.typicode.com/users/{}'.format(id)
    todo_uri = 'https://jsonplaceholder.typicode.com/todos?userId={}'.format(id)
    user = requests.get(user_uri).json()
    name = user['name']
    todos = requests.get(todo_uri).json()

    completed = [i for i in todos if i['completed']]
    out = 'Employee {} is done with tasks({}/{}):'.format(name, len(completed), len(todos))
    print(out)

    for i in completed:
        title = i.get('title')
        print('\t {}'.format(title))
