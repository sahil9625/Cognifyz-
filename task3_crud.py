import os


FILE_NAME = "tasks.txt"

def load_tasks():
    tasks = []
    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, "r") as file:
                for line in file:
                    tasks.append(line.strip())
        except IOError:
            print("Error reading the file.")
    return tasks

def save_tasks(tasks):
    try:
        with open(FILE_NAME, "w") as file:
            for task in tasks:
                file.write(task + "\n")
    except IOError:
        print("Error writing to the file.")

def display_tasks(tasks):
    if not tasks:
        print("No tasks found.")
    else:
        print("Tasks:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

def add_task(tasks):
    task = input("Enter a new task: ")
    tasks.append(task)
    save_tasks(tasks)
    print("Task added.")

def update_task(tasks):
    display_tasks(tasks)
    try:
        task_number = int(input("Enter the task number to update: ")) - 1
        if 0 <= task_number < len(tasks):
            new_task = input("Enter the new task: ")
            tasks[task_number] = new_task
            save_tasks(tasks)
            print("Task updated.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def delete_task(tasks):
    display_tasks(tasks)
    try:
        task_number = int(input("Enter the task number to delete: ")) - 1
        if 0 <= task_number < len(tasks):
            tasks.pop(task_number)
            save_tasks(tasks)
            print("Task deleted.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def main():
    tasks = load_tasks()

    while True:
        print("\nTask Manager")
        print("1. Display tasks")
        print("2. Add a task")
        print("3. Update a task")
        print("4. Delete a task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            display_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            update_task(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


main()
