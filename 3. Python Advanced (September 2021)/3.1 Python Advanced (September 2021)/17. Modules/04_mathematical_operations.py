from basic_calculations import perform_operation

equation = input().split()
number1 = float(equation[0])
operator = equation[1]
number2 = int(equation[2])

print(f"{perform_operation(number1, number2, operator):.2f}")
