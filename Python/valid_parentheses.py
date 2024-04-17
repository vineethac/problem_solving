'''
Given a string s = "{}()[]"
Print valid if:
* Open brackets must be closed by the same brackets
* Open brackets must be closed in the correct order
* Every close bracket has a corresponding open bracket of the same type

s = "()"    - valid
s = "(){}"  - valid
s = "(]"    - invalid

'''
import sys


def check_brackets(my_str: str) -> None:
    """
    This function checks whether the brackets are valid or not.
    Here we are using a stack.
    When open bracket comes push to top of stack, when closing bracket comes pop from top of stack.
    """
    my_stack = []
    for i in my_str:
        if i in ("(", "{", "["):
            my_stack.append(i)
        elif i == "}":
            top_item = my_stack.pop()
            if top_item != "{":
                print("Not valid!")
                sys.exit(0)
        elif i == ")":
            top_item = my_stack.pop()
            if top_item != "(":
                print("Not valid!")
                sys.exit(0)
        elif i == "]":
            top_item = my_stack.pop()
            if top_item != "[":
                print("Not valid!")
                sys.exit(0)

    if len(my_stack) > 0:
        print("Not valid!")
    else:
        print("Valid")


def main():
    """
    Main function.
    """
    my_str = "[()][]{({[]})}"

    check_brackets(my_str)


if __name__ == "__main__":
    main()
