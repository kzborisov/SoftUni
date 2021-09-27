def operate(operator, *args):
    return eval(operator.join([str(x) for x in args]))


print(operate("+", 1, 2, 3))
print(operate("*", 3, 4))
