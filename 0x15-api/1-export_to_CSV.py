#!/usr/bin/python3
"""Gets the TODO lists of an employee in a predefines url"""


if __name__ == '__main__':
    import requests
    import sys
    import json
    import csv

    id = sys.argv[1]
    id = int(id)
    todo = []
    uri = f'https://jsonplaceholder.typicode.com/users/{id}'
    result = requests.get(uri)
    result = result.text
    result = json.loads(result)
    name = result['username']
    uri = f'https://jsonplaceholder.typicode.com/todos/'
    result = requests.get(uri)
    result = result.text
    result = json.loads(result)
    for i in result:
        if i['userId'] == id:
            todo.append(i)

    field = ['userId', 'username', 'completed', 'title']
    for i in todo:
        i['username'] = name
        i['userId'] = str(id)
        del i['id']
    with open(f'{id}.csv', 'w', newline='') as fi:
        writer = csv.DictWriter(fi, fieldnames=field, quoting=csv.QUOTE_ALL)
        for row in todo:
            writer.writerow(row)
