# Task 08. Seize the Fire

def validate_cell(fire_cell):
    fire_type = fire_cell.split(' = ')[0]
    cell_value = int(fire_cell.split(' = ')[1])
    if fire_type == 'High' and 81 <= cell_value <= 125 or \
            fire_type == 'Medium' and 51 <= cell_value <= 80 or \
            fire_type == 'Low' and 1 <= cell_value <= 50:
        return True
    return False


fires_cells = input().split('#')
water = int(input())

total_fire = 0
effort = 0
cell_values = [int(x.split(' = ')[1]) for x in fires_cells]
print('Cells:')

for ind, value in enumerate(cell_values):
    if water - value < 0:
        continue

    if validate_cell(fires_cells[ind]):
        print(f' - {value}')
        water -= value
        effort += value * 0.25
        total_fire += value

print(f'Effort: {effort:.2f}')
print(f'Total Fire: {total_fire}')
