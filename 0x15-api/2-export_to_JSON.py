#!/usr/bin/python3
"""For a given employee ID, returns JSON"""

if __name__ == "__main__":
    """ __main__ """

    import collections
    import csv
    import json
    import sys
    import requests

    if len(sys.argv) != 2:
        exit(1)

    url = 'https://jsonplaceholder.typicode.com/'
    empID = sys.argv[1]

    urlUser = url + 'users/' + empID
    urlTodos = url + 'todos?userId=' + empID

    user = requests.get(urlUser).json()
    todos = requests.get(urlTodos).json()

    if (len(user) == 0):
        exit(1)

    username = user.get("username")

    data = collections.OrderedDict()
    values = []

    for todo in todos:
        t = collections.OrderedDict()
        t["task"] = todo.get("title")
        t["completed"] = todo.get("completed")
        t["username"] = username
        values.append(t)
        data[empID] = values

    fp = empID + ".csv"
    with open(fp, "w") as fp:
        fp.write(json.dumps(data))
