'''Rob-roy Baetge'''
def main():
    print_name()


def print_name():
    name = get_name()
    for letter in range(1, len(name), 2):
        print(name[letter], end="")


def get_name():
    name = str(input("Please enter your name"))
    while name == "":
        print("Invalid name")
        name = str(input("Please enter your name"))
    return name


main()