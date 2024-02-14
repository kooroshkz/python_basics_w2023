import json
import os

# Load database from JSON file
def load_db():
    if not os.path.exists('db.json'):
        with open('db.json', 'w') as outfile:
            json.dump({}, outfile)
    with open('db.json', 'r') as myfile:
        data = myfile.read()
    return json.loads(data)

# Save database to JSON file
def save_db(db):
    with open('db.json', "w") as outfile:
        json.dump(db, outfile)

# Display the meals options
def display_meals():
    meals = {
        0: "Not Reserved",
        1: "Pizza",
        2: "Fish",
        3: "Burger"
    }
    for i, meal in meals.items():
        print(f"{i}. {meal}")

# Display user meals reservations
def display_reservations(db):
    meals = {
        0: "Not Reserved",
        1: "Pizza",
        2: "Fish",
        3: "Burger"
    }
    for user, info in db.items():
        print(f"User {user} has {meals[info['meal']]}")

# Register a new user
def register_user(db):
    new_user = int(input("Student Number: "))
    db[new_user] = {
        "pass": int(input("Enter Password: ")), 
        "meal": 0
    }
    save_db(db)
    print("User registered successfully!")

# Allow user to log in and reserve a meal
def login_user(db):
    if not db:
        print("You don't have any users.")
        return
    user = int(input("Enter username: "))
    if user in db:
        pwd = int(input("Enter password: "))
        if pwd == db[user]["pass"]:
            display_meals()
            db[user]["meal"] = int(input("Enter your meal number: "))
            save_db(db)
            print("Meal reserved successfully!")
            display_reservations(db)
        else:
            print("Password is wrong.")
    else:
        print("User not found.")

def main():
    db = load_db()
    choice = int(input("1. Login\n2. Register\n"))

    if choice == 2:
        register_user(db)
    elif choice == 1:
        login_user(db)
    else:
        print("Invalid choice.")
    
if __name__ == "__main__":
    main()
