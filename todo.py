"""
A simple command-line to-do list manager.

Milestone 1: store tasks in memory and print them.
(Milestone 2 will turn this into an interactive menu loop.)
"""

tasks = []


def add_task(task):
    """Add a new task to the list."""
    tasks.append(task) 
    print(f"Added: {task}")


def list_tasks():
    """Print all current tasks, numbered."""
    if not tasks:
        print("No tasks yet.")
        return
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task}")


# --- Quick manual test ---
# This section just proves the functions work. In milestone 2,
# you'll replace it with a menu so you don't have to edit code
# every time you want to add a task.

add_task("Buy milk")
add_task("Finish VS Code tutorial")
list_tasks()
