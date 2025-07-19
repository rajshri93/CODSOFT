import json
import os

TASKS_FILE = "tasks.json"

def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r') as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)

def display_tasks(tasks):
    if not tasks:
        print("No tasks found.")
        return
    for idx, task in enumerate(tasks, 1):
        status = "Task is Done " if task["done"] else "Task is Not Done"
        print(f"{idx}. {task['title']} [{status}]")

def add_task(tasks):
    title = input("Enter task title: ")
    tasks.append({"title": title, "done": False})
    print("Task added Successfully.")

def mark_task_done(tasks):
    display_tasks(tasks)
    try:
        index = int(input("Enter task number to mark as done: ")) - 1
        tasks[index]["done"] = True
        print("Task marked as done.")
    except (IndexError, ValueError):
        print("Invalid task number.")

def delete_task(tasks):
    display_tasks(tasks)
    try:
        index = int(input("Enter task number to delete: ")) - 1
        removed = tasks.pop(index)
        print(f"Deleted: {removed['title']}")
    except (IndexError, ValueError):
        print("Invalid task number.")

def update_task(tasks):
    display_tasks(tasks)
    try:
        index = int(input("Enter task number to update: ")) - 1
        new_title = input("Enter new task title: ")
        old_title = tasks[index]['title']
        tasks[index]['title'] = new_title
        print(f"Updated task: '{old_title}' → '{new_title}'")
    except (IndexError, ValueError):
        print("Invalid task number.")

def main():
    tasks = load_tasks()
    while True:
        print("\n*Welcome to you your Day Planner*")
        print("\nTo-Do List Menu:")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Update Task")
        print("6. Exit from To-Do List")
        choice = input("Select from list about your day task: ")

        if choice == '1':
            display_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            mark_task_done(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            update_task(tasks)
        elif choice == '6':
            save_tasks(tasks)
            print("GoodBye !")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
