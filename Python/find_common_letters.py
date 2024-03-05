'''
s1 = COMPUTER
s2 = CAR

Result: C, R

'''


def find_common_letters(s1: str, s2: str) -> list:
    """
    Function that finds common letters.
    """
    s1_dict = {}
    s2_dict = {}
    common_letters = []

    for letter in s1:
        count = s1.count(letter)
        s1_dict[letter] = count

    for letter in s2:
        count = s2.count(letter)
        s2_dict[letter] = count

    print(s1_dict, s2_dict)

    for key, value in s1_dict.items():
        if key in s2_dict:
            common_letters.append(key)

    return common_letters

def main():
    """
    Main function.
    """
    s1 = "COMPUTER"
    s2 = "CAR"
    common_letters = find_common_letters(s1, s2)
    print(common_letters)


if __name__ == "__main__":
    main()
