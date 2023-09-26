# Define an empty list to store tasks
tasks = []

# Function to add a task to the list
def add_task(task):
    tasks.append(task)
    print(f"Task '{task}' added successfully!")

# Function to list all tasks
def list_tasks():
    if tasks:
        print("Tasks:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")
    else:
        print("No tasks found!")

# Function to mark a task as done
def mark_done(task_index):
    if 1 <= task_index <= len(tasks):
        task = tasks.pop(task_index - 1)
        print(f"Task '{task}' marked as done!")
    else:
        print("Invalid task index!")

# Main loop for the to-do list app
while True:
    print("\nTo-Do List App")
    print("A. Add Task")
    print("B. List Tasks")
    print("C. Mark Task as Done")
    print("D. Quit")

    choice = input("Enter your choice (A/B/C/DA): ")

    if choice == "1":
        task = input("Enter the task: ")
        add_task(task)
    elif choice == "2":
        list_tasks()
    elif choice == "3":
        task_index = int(input("Enter the index of the task to mark as done: "))
        mark_done(task_index)
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
