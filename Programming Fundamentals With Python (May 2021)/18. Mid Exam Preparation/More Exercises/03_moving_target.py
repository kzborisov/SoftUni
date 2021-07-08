class Shooter:
    def __init__(self, tragets):
        self.targets = targets

    def shoot(self, idx, value):
        if idx in range(len(self.targets)):
            self.targets[idx] -= value
            if self.targets[idx] <= 0:
                self.targets.pop(idx)

    def add_target(self, idx, value):
        if idx in range(len(self.targets)):
            self.targets.insert(idx, value)
        else:
            print("Invalid placement!")

    def strike(self, idx, value):
        if idx - value < 0 or idx + value > len(self.targets) - 1:
            print("Strike missed!")
        else:
            self.targets = self.targets[:idx - value] + \
                           self.targets[idx + value+1:]


targets = [int(x) for x in input().split()]
command = input()
shooter = Shooter(targets)

while not command == "End":
    cmd = command.split()[0]
    idx = int(command.split()[1])
    value = int(command.split()[2])

    if cmd == "Shoot":
        shooter.shoot(idx, value)
    elif cmd == "Add":
        shooter.add_target(idx, value)
    elif cmd == "Strike":
        shooter.strike(idx, value)
    command = input()


print(*shooter.targets, sep="|")

