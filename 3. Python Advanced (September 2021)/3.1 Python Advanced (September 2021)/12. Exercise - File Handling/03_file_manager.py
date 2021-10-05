import os


class FileManipulator:
    def __init__(self):
        pass

    def create_file(self, file_name):
        file = open(f"./{file_name}", "w")
        file.close()

    def add_to_file(self, file_name, content):
        with open(file_name, "a") as f:
            f.write(content + "\n")

    def replace_in_file(self, file_name, old_string, new_string):
        try:
            with open(file_name, 'r') as file:
                content = file.read()
            content = content.replace(old_string, new_string)
            with open(file_name, 'w') as file:
                file.write(content)
        except FileNotFoundError:
            print("An error occurred")

    def delete_file(self, file_name):
        try:
            os.remove(file_name)
        except FileNotFoundError:
            print("An error occurred")


manipulator = FileManipulator()

while True:
    command = input()
    if command == "End":
        break

    command_args = command.split("-")
    cmd = command_args[0]
    file_name = command_args[1]
    if cmd == "Create":
        manipulator.create_file(file_name)
    elif cmd == "Add":
        new_content = command_args[2]
        manipulator.add_to_file(file_name, new_content)
    elif cmd == "Replace":
        old_content = command_args[2]
        new_content = command_args[3]
        manipulator.replace_in_file(file_name, old_content, new_content)
    elif cmd == "Delete":
        manipulator.delete_file(file_name)
