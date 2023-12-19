import json
import os

class Task:
    def __init__(self, description, completed=False):
        self.description = description
        self.completed = completed

class TaskManager:
    def __init__(self):
        self.tasks = []
        self.load_tasks()

    def save_tasks(self):
        with open('tasks.json', 'w') as file:
            tasks_data = [{'description': task.description, 'completed': task.completed} for task in self.tasks]
            json.dump(tasks_data, file)

    def load_tasks(self):
        if os.path.exists('tasks.json'):
            with open('tasks.json', 'r') as file:
                tasks_data = json.load(file)
                self.tasks = [Task(task['description'], task['completed']) for task in tasks_data]

    def add_task(self, description):
        task = Task(description)
        self.tasks.append(task)
        self.save_tasks()
        print(f'Task "{description}" added successfully.')

    def view_tasks(self, show_completed=False):
        tasks_to_show = [task for task in self.tasks if task.completed == show_completed]

        if not tasks_to_show:
            print(f'No {"completed" if show_completed else "pending"} tasks available.')
        else:
            print(f'{"Completed" if show_completed else "Pending"} Tasks:')
            for i, task in enumerate(tasks_to_show, 1):
                status = 'Completed' if task.completed else 'Pending'
                print(f'{i}. {task.description} - {status}')

    def mark_completed(self, task_index):
        try:
            task = self.tasks[task_index - 1]
            task.completed = True
            self.save_tasks()
            print(f'Task "{task.description}" marked as completed.')
        except IndexError:
            print('Invalid task index.')

    def delete_task(self, task_index):
        try:
            deleted_task = self.tasks.pop(task_index - 1)
            self.save_tasks()
            print(f'Task "{deleted_task.description}" deleted.')
        except IndexError:
            print('Invalid task index.')

def main():
    task_manager = TaskManager()

    while True:
        print("\nTask Manager Menu:")
        print("1. Add Task")
        print("2. View Pending Tasks")
        print("3. View Completed Tasks")
        print("4. Mark Task as Completed")
        print("5. Delete Task")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            description = input("Enter task description: ")
            task_manager.add_task(description)
        elif choice == '2':
            task_manager.view_tasks(show_completed=False)
        elif choice == '3':
            task_manager.view_tasks(show_completed=True)
        elif choice == '4':
            task_index = int(input("Enter the task index to mark as completed: "))
            task_manager.mark_completed(task_index)
        elif choice == '5':
            task_index = int(input("Enter the task index to delete: "))
            task_manager.delete_task(task_index)
        elif choice == '6':
            print("Exiting Task Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
