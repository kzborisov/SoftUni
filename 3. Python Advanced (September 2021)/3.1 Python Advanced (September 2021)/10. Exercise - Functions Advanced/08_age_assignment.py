def age_assignment(*args, **kwargs):
    result = {}
    for first_letter, age in kwargs.items():
        for name in args:
            if name.startswith(first_letter):
                result[name] = age
    return result


print(age_assignment("Peter", "George", G=26, P=19))
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))
