'''
How many occurances of "balloon" can be found/ created from a given string.
my_string = "nlaebolko"

'''


def check_occurance(my_string: str, word: str) -> None:
    """
    This function checks the number of occurance of word that can be
    created from given string.
    We will use dict here.
    """

    my_string_dict = {}
    word_dict = {}

    for i in my_string:
        my_string_dict[i] = my_string.count(i)
    for i in word:
        word_dict[i] = word.count(i)

    print(my_string_dict)
    print(word_dict)

    count = 0
    flag = 0

    while True:

        for key,value in word_dict.items():
            if key in my_string_dict and my_string_dict[key] >= word_dict[key]:
                my_string_dict[key] = my_string_dict[key] - word_dict[key]
                # print(my_string_dict)
            else:
                flag = 1
                break

        if flag != 1:
            count += 1
        else:
            break

    print(f"balloon word count: {count}")

def main():
    """
    Main function.
    """

    my_string = "ballbbalballoonloonalloonoon"
    word = "balloon"

    check_occurance(my_string, word)


if __name__ == "__main__":
    main()
