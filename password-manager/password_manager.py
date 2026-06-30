import os

FILE = "passwords.txt"

def add_password():
    website = input("Website: ")
    username = input("Username: ")
    password = input("Password: ")

    with open(FILE, "a") as f:
        f.write(f"{website} | {username} | {password}\n")

    print("Saved successfully.")

def view_passwords():
    if not os.path.exists(FILE):
        print("No passwords saved yet.")
        return

    with open(FILE, "r") as f:
        print("\nSaved Passwords\n")
        print(f.read())

while True:
    print("\n=== Password Manager ===")
    print("1. Add Password")
    print("2. View Passwords")
    print("3. Exit")

    choice = input("Choose: ")

    if choice == "1":
        add_password()

    elif choice == "2":
        view_passwords()

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid option.")
