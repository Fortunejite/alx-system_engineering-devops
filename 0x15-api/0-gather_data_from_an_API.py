#!/usr/bin/python3
"""Gets the TODO lists of an employee in a predefines url"""


if __name__ == '__main__':
    import requests
    import sys
    import json

    id = sys.argv[1]
    id = int(id)s
    todo = []
    uri = f'https://jsonplaceholder.typicode.com/users/{id}'
    result = requests.get(uri)
    result = result.text
    result = json.loads(result)
    name = result['name']
    uri = f'https://jsonplaceholder.typicode.com/todos/'
    result = requests.get(uri)
    result = result.text
    result = json.loads(result)
    for i in result:
        if i['userId'] == id:
            todo.append(i)

    completed = []
    for i in todo:
        if i['completed'] is True:
            completed.append(i)

    out = f'Employee {name} is done with tasks({len(completed)}/{len(todo)}):'
    print(out)

    for i in completed:
        title = i.get('title')
        print(f'\t {title}')
