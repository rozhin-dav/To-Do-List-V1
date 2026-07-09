# To-Do List V1
# Created by Rozhin

print("===== To-Do List =====")

tasks = []

while True:
    print("1. Add Task")
    print("2. Show Tasks")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        task = input("Enter a task: ")
        tasks.append(task)
        print("Task added!")

    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks found!")
        else:
            print("Your Tasks:")
            for task in tasks:
                print(task)

    elif choice == "3":
        task = input("Which task? ")

        if task in tasks:
            tasks.remove(task)
            print("Task removed!")
        else:
            print("Task not found!")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice! Please choose 1-4.")
