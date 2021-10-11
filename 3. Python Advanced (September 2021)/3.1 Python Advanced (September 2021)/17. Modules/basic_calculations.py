def perform_operation(number1, number2, operator):
    if operator == "+":
        return number1 + number2
    elif operator == "-":
        return number1 - number2
    elif operator == "/":
        if number2 == 0:
            raise ValueError("In division, number 2 must not be equal to 0!")
        return number1 / number2
    elif operator == "*":
        return number1 * number2
    elif operator == "^":
        return number1 ** number2
    else:
        raise ValueError("Operator must be one of the following: ")