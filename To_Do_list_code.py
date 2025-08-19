todo_list = []

def show_menu():
    print("\nTo-Do List Menu:")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Delete Task")
    print("4. Clear all Tasks")
    print("5. Exit")

while True:
    show_menu()
    choice = input("Enter your choice (1-5): ")
    # user choice is 1
    if choice == '1':
        if not todo_list:
            print("No tasks yet.")
        else:
            for i, task in enumerate(todo_list, 1):
                print(f"{i}. {task}")
    #user choice is 2
    elif choice == '2':
        task_count=int(input("Enter number of tasks to be added: "))
        for _ in range(task_count):
            task = input("Enter new task: ")
            todo_list.append(task)
            print("Task added!")
        print("\nYour To-Do List:")
        for t in todo_list:
            print("-", t)
    # user choice is 3
    elif choice == '3':
        task_no = int(input("Enter task number to delete: "))
        if 0 < task_no <= len(todo_list):
            removed = todo_list.pop(task_no - 1)
            print(f"Removed: {removed}")
            print("\nUpdated To-Do List:")
            for i, task in enumerate(todo_list, start=1):
                print(f"{i}. {task}")
        else:
            print("Invalid task number!")
    # user choice is 4
    elif choice=='4':
        confirm = input("Are you sure do you want to remove all tasks? (y/n): ")
        if confirm.lower() == 'y':
           todo_list.clear()
           print("All tasks removed! Your to-do list is now empty.")
        else:
           print("No worries, I left your list as it is.")
    # user choice is 5
    elif choice == '5':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")
