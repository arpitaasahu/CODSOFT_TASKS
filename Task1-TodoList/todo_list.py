
my_tasks = []

while True:
    print("\n===== TO-DO LIST =====")
    print("1. Add New Task")
    print("2. View All Tasks")
    print("3. Remove Completed Task")
    print("4. Exit")

    choice = input("Enter your choice(1-4): ")

    # Option 1: Add anew task
    if choice == "1":
        task = input("Enter a new task: ").strip()
        if task:
            my_tasks.append(task)
            print("New task added successfully!")
        else:
            print("Task cannot be empty")

    # Option 2: Display all Tasks
    elif choice == "2":
        if len(my_tasks) == 0:
            print("Your task list is currently empty.")
        else:
            print("\nCurrent Tasks:")
            for i in range(len(my_tasks)):
                print(f"{i + 1}. {my_tasks[i]}")

    # Option 3: Remove a task
    elif choice == "3":
        if len(my_tasks) == 0:
            print("There are no tasks available to remove.")
        else:
            for i in range(len(my_tasks)):
                print(f"{i + 1}. {my_tasks[i]}")

            num = int(input("Enter task number to remove: "))

            if 1 <= num <= len(my_tasks):
                completed_task = my_tasks.pop(num - 1)
                print(f"Task '{completed_task}' completed and removed successfully!")
            else:
                print("\nEnter a valid task number.")

    # Option 4: Exit program
    elif choice == "4":
        print("\nThank you for using My To-Do List.")
        print("Your tasks have been managed successfully!")
        break

    else:
        print("Invalid choice. Please select a number between 1 and 4.")



