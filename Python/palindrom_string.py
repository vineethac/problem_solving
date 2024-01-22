'''
Palindrome string check.
eg: ABA, racecar, refer
'''
import sys

def check_palindrome(str: str) -> None:
    """
    Here we use slicing method.
    """
    rev_str = str[::-1]

    if rev_str == str:
        print("Its palindrome!")
    else:
        print("Its not palindrome!")

def main():
    str = sys.argv[1]
    check_palindrome(str)

if __name__ == "__main__":
    main()
    