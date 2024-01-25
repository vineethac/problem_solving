'''
Get email address from given string.
Example: text = "Please contact john.doe@example.com or jane_doe@example.com"
'''

import re

def regex_check(my_string: str) -> None:
    words = re.findall(r'\b[a-zA-Z0-9._+-]+@[a-zA-Z0-9._+-]+.[com]\b', my_string)
    print(words)   


def main():
    my_string = "Please contact john.doe@example.com or jane_doe@example.com."
    regex_check(my_string)


if __name__ == "__main__":
    main()