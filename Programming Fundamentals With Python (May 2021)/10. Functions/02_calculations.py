# Task 02. Calculations

def calculations(operation, first_operand, second_operand):
    operations = {
        'multiply': first_operand * second_operand,
        'divide': first_operand // second_operand,
        'add': first_operand + second_operand,
        'subtract': first_operand - second_operand
    }
    return operations[operation]


input_operator = input()
first_int = int(input())
second_int = int(input())

print(calculations(input_operator, first_int, second_int))
