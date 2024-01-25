'''
Find words that contains exactly five letters.
'''

import re

def regex_check(my_string: str) -> None:
    words = re.findall(r'\b\w{5}\b', my_string)
    print(words)   


def main():
    my_string = "The quick brown fox jumps over the lazy dog"
    regex_check(my_string)


if __name__ == "__main__":
    main()