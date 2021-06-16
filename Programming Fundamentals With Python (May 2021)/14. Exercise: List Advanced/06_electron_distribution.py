# Task 06 Electron Distribution

electrons_cnt = int(input())

shells = []
shell = 2 * 1 ** 2
counter = 1

while electrons_cnt - shell >= 0:
    electrons_cnt -= shell
    shells.append(shell)
    counter += 1
    shell = 2 * counter ** 2

if electrons_cnt > 0:
    shells.append(electrons_cnt)
print(shells)
