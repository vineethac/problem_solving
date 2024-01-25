'''
Replace all occurrences of "apple" with "orange" in a string.
'''

import re

def regex_check(my_string: str) -> None:
    new_text = re.sub(r'\bapples\b', 'orange', my_string)
    print(new_text)   


def main():
    my_string = "I really like apples, but I don't like bananas or apples."
    regex_check(my_string)


if __name__ == "__main__":
    main()