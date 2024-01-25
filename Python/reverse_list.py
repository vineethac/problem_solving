'''
Reverse a list.
'''

'''
def reverse_list(my_list: list) -> None:
    """
    This is another method by inserting at index 0 of the list.
    """
    rev_list = []
    for item in my_list:
        rev_list.insert(0, item)

    print(rev_list)
'''

def reverse_list(my_list: list) -> None:
    """
    This will traverse the list from last index to index 0.
    """
    len_my_list = len(my_list)
    i = len_my_list - 1
    rev_list= []

    while i >= 0:
        rev_list.append(my_list[i])
        i -= 1

    print(rev_list)


def main():
    my_list = [1, 4, 6, 2, 8]
    reverse_list(my_list)
    

if __name__ == "__main__":
    main()