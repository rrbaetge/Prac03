def main():
    letter = get_letter()
    ascii_char = ord(letter)
    print("The ASCII code for {1} is {0} ".format(letter, ascii_char))

    number = get_num()
    ascii_num = chr(number)
    print("The Character for {} is {} ".format(number, ascii_num))
    # for number in range(33, 127, 1):
    #     print("{:3} {:>6}".format(number, chr(number)))


def get_num():
    while True:
        try:
            number = int(input("Please enter a valid number"))
            if number > 32 and number < 128:
                return number
        except ValueError:
            print("Please enter a valid interger")


def get_letter():
    letter = (input("Please eneter a letter"))
    while letter not in "abcdefghijklmnopqrstuvwxyz":
        print("invalid letter")
        letter = (input("Please eneter a letter"))
    return letter


main()