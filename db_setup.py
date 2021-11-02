from sqlite_utils import Database
import sqlite3
from passlib.hash import pbkdf2_sha256 as encrypt

#Creating the database all_users
list2 = "[1, 2, 3, 4, 5]"
db = Database(sqlite3.connect("./var/all_users.db"))
# users table inside all_users.db
hash = encrypt.hash("password")
hash2 = encrypt.hash("pass")
print(hash)
print(hash2)
user = db["users"]
# user.insert({
#     "username": "test",
#     "email": "test@test.com",
#     "password": hash,
# }, pk = "username",
#     not_null={"username", "email", "password"})

# user.insert({
#     "username": "kitloo",
#     "email": "kit@test.com",
#     "password": hash2,
# })

# Query practice goes here
query_string = f"SELECT password FROM users WHERE username='test'"

# print(db.query(query_string))
result = db.query(query_string)
print(result)
for x in result:
    print(x)
    print(encrypt.verify("password", x["password"]))
