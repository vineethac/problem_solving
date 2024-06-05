'''
Given a random password check if it satisfies 3 out of the 4 following criteria:

* should have atleast one capital letter
* should have atleast one digit
* should have atleast one small case letter
* should have atleast one special character

'''


def check_pass(my_str: str) -> None:
    """
    Password criteria checking function.
    """
    upper_case = 0
    lower_case = 0
    digit = 0
    special = 0
    count = 0

    for i in my_str:

        if i.isupper():
            upper_case = 1
        if i.islower:
            lower_case = 1
        if i.isdigit():
            digit = 1
        if i in ('@','#','!'):
            special = 1

    count = upper_case + lower_case + digit + special

    if count >= 3:
        print("Password satisfies conditions!")
    else:
        print("Password does not satisfy conditions!")


def main():
    """
    Main function.
    """

    my_str = "abcA@#12"
    check_pass(my_str)


if __name__ == "__main__":
    main()
