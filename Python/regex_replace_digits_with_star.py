'''
input: "this is my car 12345 and there is a 0 and it is 12"
output: "this is my car ***** and there is a * and it is **"

'''
import re


def replace_digits(my_input: str) -> None:
    """
    Function to replace al digits with *.
    """
    result = re.sub(r'\d', "*", my_input)
    print(result)


def main():
    """
    Main function.
    """
    my_input = "this is my car 12345 and there is a 0 and it is 12"
    replace_digits(my_input)


if __name__ == "__main__":
    main()
