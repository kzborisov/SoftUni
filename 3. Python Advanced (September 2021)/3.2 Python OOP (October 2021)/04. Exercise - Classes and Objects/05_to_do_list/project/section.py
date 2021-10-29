class Section:
    def __init__(self, name):
        self.name = name
        self.tasks = []

    def add_task(self, new_task):
        if new_task in self.tasks:
            return f"Task is already in the section {self.name}"

        self.tasks.append(new_task)
        return f"Task {new_task.details()} is added to the section"

    def complete_task(self, task_name):
        for task in self.tasks:
            if task.name == task_name:
                task.completed = True
                return f"Completed task {task_name}"
        return f"Could not find task with the name {task_name}"

    def clean_section(self):
        tasks_count = len(self.tasks)
        self.tasks = [task for task in self.tasks if not task.completed]
        removed_tasks = tasks_count - len(self.tasks)
        return f"Cleared {removed_tasks} tasks."

    def view_section(self):
        msg = f"Section {self.name}:\n"
        msg += "\n".join([task.details() for task in self.tasks])
        return msg
