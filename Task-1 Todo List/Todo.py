"""
Task 1: To-Do List Manager

Goal:
Build a program where users can add tasks to a list and view them.

Extra Features:
- Add tasks
- View tasks
- Remove tasks
- Simple menu-driven interface
- Input validation

Author: Ayush Bodade
"""

# Function to display all tasks
def show_tasks(tasks):
    if not tasks:
        print("\nYour to-do list is empty.\n")
        return

    print("\n========== YOUR TO-DO LIST ==========")
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task}")
    print()


# Main function
def main():
    tasks = []

    while True:
        print("=" * 35)
        print("      TO-DO LIST MANAGER")
        print("=" * 35)
        print("1. Add a Task")
        print("2. View Tasks")
        print("3. Remove a Task")
        print("4. Exit")

        choice = input("\nEnter your choice (1-4): ").strip()

        # Add Task
        if choice == "1":
            task = input("Enter the task: ").strip()

            if task:
                tasks.append(task)
                print(f"\n✅ Task '{task}' added successfully!\n")
            else:
                print("\n⚠️ Task cannot be empty.\n")

        # View Tasks
        elif choice == "2":
            show_tasks(tasks)

        # Remove Task
        elif choice == "3":
            show_tasks(tasks)

            if tasks:
                try:
                    number = int(input("Enter task number to remove: "))

                    if 1 <= number <= len(tasks):
                        removed_task = tasks.pop(number - 1)
                        print(f"\n🗑️ Task '{removed_task}' removed successfully!\n")
                    else:
                        print("\n⚠️ Invalid task number.\n")

                except ValueError:
                    print("\n⚠️ Please enter a valid number.\n")

        # Exit
        elif choice == "4":
            print("\nThank you for using the To-Do List Manager!")
            print("Have a productive day! 🚀")
            break

        # Invalid Input
        else:
            print("\n❌ Invalid choice. Please enter a number between 1 and 4.\n")


# Run the program
if __name__ == "__main__":
    main()