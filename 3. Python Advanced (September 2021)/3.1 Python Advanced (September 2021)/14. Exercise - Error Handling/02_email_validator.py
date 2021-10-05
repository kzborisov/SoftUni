class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


def valid_name(email):
    return True if len(email.split("@")[0]) > 4 else False


def contains_symbol(email):
    return "@" in email


def valid_domain(email):
    return email.split(".")[-1] in ["com", "bg", "net", "org"]


while True:
    current_email = input()
    if current_email == "End":
        break

    if not valid_name(current_email):
        raise NameTooShortError("Name must be more than 4 characters")
    if not contains_symbol(current_email):
        raise MustContainAtSymbolError("Email must contain @")
    if not valid_domain(current_email):
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")

    print("Email is valid")
