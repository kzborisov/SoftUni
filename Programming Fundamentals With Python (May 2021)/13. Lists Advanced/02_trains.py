# Task 02. Trains

wagons = int(input())
train = [0] * wagons

command = input()

while not command == "End":
    cmd = command.split()[0]
    cmd_args = command.split()[1:]
    if cmd == "add":
        train[-1] += int(cmd_args[0])
    elif cmd == "insert":
        train[int(cmd_args[0])] += int(cmd_args[1])
    elif cmd == "leave":
        train[int(cmd_args[0])] -= int(cmd_args[1])
    command = input()


print(train)
