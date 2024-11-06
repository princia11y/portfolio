import json

# Initialize the to-do list
todo_list = []

# Load existing to-do list from file (if available)
try:
    with open("todo_list.json", "r") as file:
        todo_list = json.load(file)
except FileNotFoundError:
    pass  # No existing file found, so we'll start with an empty list

def display_menu():
    print("\n--- To-Do List Menu ---")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Delete Task")
    print("4. Mark Task as Completed")
    print("5. Save and Exit")

def view_tasks():
    print("\n--- To-Do List ---")
    if not todo_list:
        print("Your to-do list is empty.")
    else:
        for i, task in enumerate(todo_list, start=1):
            status = "✓" if task["completed"] else "✗"
            print(f"{i}. {task['description']} [{status}]")

def add_task():
    description = input("Enter the task description: ")
    todo_list.append({"description": description, "completed": False})
    print("Task added successfully.")

def delete_task():
    view_tasks()
    try:
        task_num = int(input("Enter the task number to delete: "))
        if 1 <= task_num <= len(todo_list):
            deleted_task = todo_list.pop(task_num - 1)
            print(f"Task '{deleted_task['description']}' deleted successfully.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def mark_task_completed():
    view_tasks()
    try:
        task_num = int(input("Enter the task number to mark as completed: "))
        if 1 <= task_num <= len(todo_list):
            todo_list[task_num - 1]["completed"] = True
            print("Task marked as completed.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def save_and_exit():
    with open("todo_list.json", "w") as file:
        json.dump(todo_list, file)
    print("To-do list saved. Goodbye!")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ")
        
        if choice == "1":
            view_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            mark_task_completed()
        elif choice == "5":
            save_and_exit()
            break
        else:
            print("Invalid choice. Please try again.")

# Start the program
main()
