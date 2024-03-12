'''
Reverse words in the given string.

input = "you can suppress this message"

output = "message this suppress can you"

'''

def reverse_str(my_str: str) -> None:
    """
    Function to reverse words in the string.
    """
    new_str = ""
    new_list = my_str.split()
    rev_list = new_list[::-1]

    for item in rev_list:
        new_str += item + " "

    print(new_str)


def main():
    """
    Main function.
    """
    my_str = "you can suppress this message"
    reverse_str(my_str)


if __name__ == "__main__":
    main()
