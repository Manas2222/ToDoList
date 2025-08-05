TODO_FILE = "todo.txt"

def load_tasks():
    tasks = []
    try:
        with open(TODO_FILE, "r") as f:
            for line in f:
                line = line.strip()
                if line.startswith("[X]"):
                    tasks.append({"task": line[3:].strip(), "done": True})
                elif line.startswith("[ ]"):
                    tasks.append({"task": line[3:].strip(), "done": False})
    except FileNotFoundError:
        pass
    return tasks

def save_tasks(tasks):
    with open(TODO_FILE, "w") as f:
        for task in tasks:
            status = "[X]" if task["done"] else "[ ]"
            f.write(f"{status} {task['task']}\n")

def show_tasks(tasks):
    if not tasks:
        print("No tasks yet!")
        return
    print("\nYour To-Do List:")
    for i, task in enumerate(tasks):
        status = "✅" if task["done"] else "❌"
        print(f"{i + 1}. [{status}] {task['task']}")

def add_task(tasks):
    task_text = input("Enter the task: ").strip()
    if task_text:
        tasks.append({"task": task_text, "done": False})
        print("Task added.")
    else:
        print("Task cannot be empty.")

def complete_task(tasks):
    show_tasks(tasks)
    try:
        idx = int(input("Enter task number to mark as completed: ")) - 1
        if 0 <= idx < len(tasks):
            tasks[idx]["done"] = True
            print("Task marked as completed.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def delete_task(tasks):
    show_tasks(tasks)
    try:
        idx = int(input("Enter task number to delete: ")) - 1
        if 0 <= idx < len(tasks):
            removed = tasks.pop(idx)
            print(f"Deleted task: {removed['task']}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    tasks = load_tasks()

    while True:
        print("\nTo-Do List Menu")
        print("1. View tasks")
        print("2. Add task")
        print("3. Mark task as completed")
        print("4. Delete task")
        print("5. Exit")
        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            save_tasks(tasks)
            print("Goodbye! Exiting todo list")
            break
        else:
            print("Invalid choice. Please select a number from 1 to 5.")
        print("---------------------------------------------")

if __name__ == "__main__":
    main()
