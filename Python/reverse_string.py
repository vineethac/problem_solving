'''
Reverse a given string
Example: 
Input = "abc"
Output = "cba"
'''
import sys

def reverse_string(s: str) -> str:
    """
    This function will return a reversed string.
    """
    rev_s = ""
    for i in s:
        rev_s = i + rev_s
    return rev_s


def main():
    s = sys.argv[1]
    print(f"Original string: {s}")

    rev_s = reverse_string(s)
    print(f"Reversed string is: {rev_s}")


if __name__ == "__main__":
    main()