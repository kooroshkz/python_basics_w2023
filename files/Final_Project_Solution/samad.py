import json

myfile = open('files/db.json', 'a+')
data = myfile.read()
obj = json.loads(data)

print(obj)

db = {}

meals = {0: "Not Reserved",
         1: "Pizza",
         2: "Fish",
         3: "Burger"}

if int(input("1. Login\n2. Register\n")) == 2:
    new_user = int(input("Student Number: "))
    db[new_user] = {"pass" : int(input("Enter Password: ")), "meal" : 0}
else:
    pass



def show():
    for i in (db):
        print(f"User {i} have {meals[int(db[i]['meal'])]}")

user = int(input("Enter username: "))
if user in db:
    pwd = int(input("Enter password: "))
    if pwd == db[user]["pass"]:
        print(meals)
        db[user]["meal"] = int(input("Enter your meal number: "))
        show()
    else:
        print("Password is wrong")
else:
    print("User not found")