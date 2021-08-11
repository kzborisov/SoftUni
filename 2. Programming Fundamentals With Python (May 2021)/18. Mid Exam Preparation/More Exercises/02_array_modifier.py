class Modifier:
    def __init__(self, lst):
        self.lst = lst

    def swap(self, index_1, index_2):
        self.lst[index_1], self.lst[index_2] = self.lst[index_2], self.lst[index_1]

    def multiply(self, index_1, index_2):
        self.lst[index_1] = int(self.lst[index_1]) * int(self.lst[index_2])

    def decrease(self):
        self.lst = [int(x) - 1 for x in self.lst]


initial_list = input().split()
command = input()
modifier = Modifier(initial_list)

while not command == "end":
    cmd = command.split()[0]
    if cmd == "swap":
        idx_1 = int(command.split()[1])
        idx_2 = int(command.split()[2])
        modifier.swap(idx_1, idx_2)
    elif cmd == "multiply":
        idx_1 = int(command.split()[1])
        idx_2 = int(command.split()[2])
        modifier.multiply(idx_1, idx_2)
    elif cmd == "decrease":
        modifier.decrease()

    command = input()

print(*modifier.lst, sep=", ")
