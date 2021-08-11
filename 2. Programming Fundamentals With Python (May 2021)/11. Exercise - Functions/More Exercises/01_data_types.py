# Task 01. More Exercises Data Types

def data_type(data_input, data_type):
    if data_type == 'int':
        return int(data_input) * 2
    elif data_type == 'real':
        return f"{float(data_input) * 1.50:.2f}"
    elif data_type == 'string':
        return f"${data_input}$"


data_type_input = input()
data = input()

print(data_type(data, data_type_input))
