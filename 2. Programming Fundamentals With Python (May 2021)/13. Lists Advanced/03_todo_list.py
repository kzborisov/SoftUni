# Task 03. To Do List

task = input()
todo_list = []

while not task == "End":
    todo_list.append(task)
    task = input()

todo_list = sorted(todo_list, key=lambda x: int(x.split("-")[0]))
print([x.split("-")[1] for x in todo_list])
