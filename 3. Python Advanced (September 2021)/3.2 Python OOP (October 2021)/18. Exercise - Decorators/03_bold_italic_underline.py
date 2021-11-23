def make_bold(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return "<b>" + result + "</b>"

    return wrapper


def make_italic(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return "<i>" + result + "</i>"

    return wrapper


def make_underline(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return "<u>" + result + "</u>"

    return wrapper


@make_bold
@make_italic
@make_underline
def greet(name):
    return f"Hello, {name}"


print(greet("Peter"))


@make_bold
@make_italic
@make_underline
def greet_all(*args):
    return f"Hello, {', '.join(args)}"


print(greet_all("Peter", "George"))
