"""
Project 2: Expense Tracker

Goal:
Allow users to enter expense amounts one by one.
The program calculates and displays the total amount spent.

Extra Features:
- Input validation
- Running total
- Expense summary
- Average expense

Author: Ayush Bodade
"""

def main():
    total = 0.0
    expenses = []

    print("=" * 35)
    print("        EXPENSE TRACKER")
    print("=" * 35)
    print("Enter your expenses one at a time.")
    print("Type 'done' when you're finished.\n")

    while True:
        entry = input("Enter an expense amount (or 'done' to finish): ").strip()

        if entry.lower() == "done":
            break

        try:
            expense = float(entry)

            if expense < 0:
                print("\n⚠️ Expense cannot be negative. Please try again.\n")
                continue

            expenses.append(expense)
            total += expense

            print(f"✅ Added: ₹{expense:.2f}")
            print(f"💰 Running Total: ₹{total:.2f}\n")

        except ValueError:
            print("\n❌ Invalid input! Please enter a valid number.\n")

    print("\n" + "=" * 35)
    print("           EXPENSE SUMMARY")
    print("=" * 35)

    if expenses:
        print("\nExpenses Entered:")

        for index, amount in enumerate(expenses, start=1):
            print(f"{index}. ₹{amount:.2f}")

        print("\n-----------------------------------")
        print(f"Total Expenses : {len(expenses)}")
        print(f"Total Spent    : ₹{total:.2f}")
        print(f"Average Expense: ₹{total / len(expenses):.2f}")
    else:
        print("No expenses were entered.")

    print("\nThank you for using Expense Tracker! 🚀")


if __name__ == "__main__":
    main()