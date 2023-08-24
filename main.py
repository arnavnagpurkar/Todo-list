# Function to add a task to the to-do list
def add_task(task, filename):
    with open(filename, 'a') as file:
        file.write(task + '\n')

# Function to list all tasks in the to-do list
def list_tasks(filename):
    with open(filename, 'r') as file:
        tasks = file.readlines()
        if tasks:
            print("To-Do List:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task.strip()}")
        else:
            print("Your to-do list is empty.")

# Function to remove a task from the to-do list
def remove_task(task_number, filename):
    with open(filename, 'r') as file:
        tasks = file.readlines()

    if 1 <= task_number <= len(tasks):
        removed_task = tasks.pop(task_number - 1)
        with open(filename, 'w') as file:
            file.writelines(tasks)
        print(f"Removed: {removed_task.strip()}")
    else:
        print("Invalid task number.")

# Main loop
todo_filename = 'todo.txt'

while True:
    print("\nOptions:")
    print("1. Add Task")
    print("2. List Tasks")
    print("3. Remove Task")
    print("4. Quit")

    choice = input("Enter your choice: ")

    if choice == '1':
        task = input("Enter the task: ")
        add_task(task, todo_filename)
    elif choice == '2':
        list_tasks(todo_filename)
    elif choice == '3':
        list_tasks(todo_filename)
        task_number = int(input("Enter the task number to remove: "))
        remove_task(task_number, todo_filename)
    elif choice == '4':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please choose a valid option.")
