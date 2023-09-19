# Define a list to store tasks.
tasks = []

# Function to add a task to the list.
def add_task(title):
    task = {"title": title, "done": False}
    tasks.append(task)

# Function to mark a task as completed.
def complete_task(index):
    try:
        # <= 0 should also be checked b/c int overflow...

        tasks[index]["done"] = True
        print()
        display_tasks()
    except IndexError:
        print("Invalid index. Please enter a valid index.")

# Function to display the To-Do List.
def display_tasks():
    print("To-Do List:")
    for i, task in enumerate(tasks, 1):
        status = " "
        if task["done"]:
            status = "✓"
        print(f"{i}. [{status}] {task['title']}")

while True:
    # Display the menu and options.
    print("\nOptions:")
    print("1. Add Task")
    print("2. Mark Task as Completed")
    print("3. Display Tasks")
    print("4. Quit")

    choice = input("Enter your choice: ")

    print()

    if choice == "1":
        # Add a task.
        title = input("Enter task title: ")
        print()
        add_task(title.strip())
        display_tasks()
    elif choice == "2":
        # Mark a task as completed.
        display_tasks()
        index = int(input("Enter task index to mark as completed: ")) - 1
        complete_task(index)
    elif choice == "3":
        # Display the To-Do List.
        display_tasks()
    elif choice == "4":
        # Quit the program.
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please choose a valid option.")
