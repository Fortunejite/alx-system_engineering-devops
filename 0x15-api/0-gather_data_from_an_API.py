#!/usr/bin/python3
"""Gets the TODO lists of an employee in a predefines url"""

import json
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

    todo = []
    uri = 'https://jsonplaceholder.typicode.com/users/{}'.format(id)
    result = requests.get(uri).json()
    name = result['name']
    uri = f'https://jsonplaceholder.typicode.com/todos?userId={id}'
    result = requests.get(uri).json()
    todo = result

    completed = [i for i in todo if i['completed']]
    out = f'Employee {name} is done with tasks({len(completed)}/{len(todo)}):'
    print(out)

    for i in completed:
        title = i.get('title')
        print(f'\t {title}')
