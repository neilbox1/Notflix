from sqlite_utils import Database
import sqlite3
import json

#Creating the database all_users
list2 = "[1, 2, 3, 4, 5]"
db = Database(sqlite3.connect("./var/all_users.db"))
# users table inside all_users.db
user = db["users"]
user.insert({
    "username": "test",
    "email": "test@test.com",
    "password": "password",
}, pk = "username",
    not_null={"username", "email", "password", "favorites"})

user.insert({
    "username": "kitloo",
    "email": "kit@test.com",
    "password": "",
    "favorites": "hello",
})

# Query practice goes here
query_string = f"SELECT * FROM users WHERE username='kitloo'"

# print(db.query(query_string))
result = db.query(query_string)
print(result)
for x in result:
    print(x)
    print(type(list2))
    print(type(x))
    print(type(x["favorites"]))