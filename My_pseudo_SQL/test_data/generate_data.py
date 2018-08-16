#!python2.7
import json

# users data
# ["id", "user name", "number of friends"]
users = [
    [0, "Hero", 0],
    [1, "Dunn", 2],
    [2, "Sue", 3],
    [3, "Chi", 3],
    [4, "Thor", 3],
    [5, "Clive", 2],
    [6, "Hicks", 3],
    [7, "Devin", 2],
    [8, "Kate", 2],
    [9, "Klein", 3],
    [10, "Jen", 1]
]

with open("user.json", "w") as f:
    json.dump(users, f, indent=4)

user_interests = [
    ["user_id", "interest"],
    [0, "SQL"],
    [0, "NoSQL"],
    [2, "SQL"],
    [2, "MySQL"],
    [3, "Java"],
    [3, "Python"],
    [4, "Flask"],
    [4, "JavaScripts"],
    [6, "Shell"],
    [6, "Python"],
    [8, "Java"],
    [8, "Spring"],
    [9, "NoSQL"],
    [10, "Python"]
]

with open("interests.json", "w") as f:
    json.dump(user_interests, f, indent=4)
