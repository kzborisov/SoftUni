# Task 06 Electron Distribution

total_electrons = int(input())

shells = []
shell = 2 * 1 ** 2
counter = 1

while total_electrons - shell >= 0:
    total_electrons -= shell
    shells.append(shell)
    counter += 1
    shell = 2 * counter ** 2

if total_electrons > 0:
    shells.append(total_electrons)
print(shells)


print('-' * 20)
print("From Exercise")
#  From Exercise

total_electrons = int(input())
electron_config = []
current_layer = 1

while total_electrons > 0:
    current_layer_electrons = 2 * pow(current_layer, 2)

    if total_electrons >= current_layer_electrons:
        electron_config.append(current_layer_electrons)
    else:
        electron_config.append(total_electrons)

    total_electrons -= current_layer_electrons
    current_layer += 1

print(electron_config)
