def concatenate(*args):
    concatenated_string = ""
    for arg in args:
        concatenated_string += arg
    return concatenated_string


print(concatenate("Soft", "Uni", "Is", "Great", "!"))
print(concatenate("I", " ", "Love", " ", "Python"))
