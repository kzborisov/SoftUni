import pyfiglet


def ascii_art(text):
    return pyfiglet.print_figlet(text)


input_str = input()
print(ascii_art(input_str))
