'''
Count frequency of words in a given string.

my_str = "Vineeth loves eating apple and mango Lets eat apple and mango"

Output:

Vineeth : 1
loves : 1
eating : 1
apple : 2
mango : 2
and : 2
eat : 1
Lets : 1

'''


def count_words(my_str: str) -> None:
    """
    Function to count frequency of words.
    """
    my_str_dict = {}
    my_str_list = my_str.split()

    for word in my_str_list:
        count = my_str_list.count(word)
        my_str_dict[word] = count

    print(my_str_dict)


def main():
    """
    Main function.
    """
    my_str = "Vineeth loves eating apple and mango Lets eat apple and mango"
    count_words(my_str)


if __name__ == "__main__":
    main()
    