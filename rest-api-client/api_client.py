import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

while True:
    print("\n=== REST API Client ===")
    print("1. View Posts")
    print("2. View Users")
    print("3. Create Post")
    print("4. Exit")

    choice = input("Choose: ")

    if choice == "1":
        response = requests.get(f"{BASE_URL}/posts")

        if response.status_code == 200:
            posts = response.json()[:5]

            print("\nLatest Posts\n")

            for post in posts:
                print(f"ID: {post['id']}")
                print(f"Title: {post['title']}")
                print("-" * 40)

    elif choice == "2":
        response = requests.get(f"{BASE_URL}/users")

        if response.status_code == 200:
            users = response.json()

            print("\nUsers\n")

            for user in users:
                print(f"{user['id']}. {user['name']} ({user['email']})")

    elif choice == "3":
        title = input("Title: ")
        body = input("Body: ")

        data = {
            "title": title,
            "body": body,
            "userId": 1
        }

        response = requests.post(f"{BASE_URL}/posts", json=data)

        print("\nServer Response\n")
        print(response.json())

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid option.")
