#!/usr/bin/python3
"""For a given employee ID return data"""

if __name__ == "__main__":
    """ __main__ """

    import json
    import requests
    import sys

    if len(sys.argv) != 2:
        exit(1)

    empID = sys.argv[1]
    url = 'https://jsonplaceholder.typicode.com/'

    url_empID = url + 'users/' + str(empID)
    user = requests.get(url_empID).json()

    if (len(user) == 0):
        exit(1)

    empName = user.get("name")

    url_TodoCompleted = url + 'todos?userId=' + empID + '&completed=true'
    t = requests.get(url_TodoCompleted)
    tJson = t.json()
    nTodoDone = len(tJson)

    url_TodoTotal = url + 'todos?userId=' + empID
    tot = requests.get(url_TodoTotal)
    totJson = tot.json()
    nTodo = len(totJson)

    print("Employee {} is done with tasks({}/{}):".format(
        empName, nTodoDone, nTodo))
    for i in range(nTodoDone):
        print("\t {}".format(tJson[i].get("title")))
