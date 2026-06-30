import sqlite3

conn = sqlite3.connect("expenses.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS expenses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    item TEXT,
    amount REAL
)
""")

while True:
    print("\n=== Expense Tracker ===")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Exit")

    choice = input("Choose: ")

    if choice == "1":
        item = input("Item: ")
        amount = float(input("Amount: "))

        cursor.execute(
            "INSERT INTO expenses (item, amount) VALUES (?, ?)",
            (item, amount)
        )
        conn.commit()

        print("Expense saved.")

    elif choice == "2":
        cursor.execute("SELECT * FROM expenses")

        total = 0

        print("\nExpenses\n")

        for expense in cursor.fetchall():
            print(expense)
            total += expense[2]

        print(f"\nTotal Spent: {total}")

    elif choice == "3":
        conn.close()
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")
