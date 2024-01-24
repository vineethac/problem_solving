'''
Remove duplicate elements from a given list.
Example:
Input list = [1, 2, 1, 4 ,6, 2, 11, 2]
Output = [1, 2, 4, 6, 11]

'''

def remove_duplicates(my_list: list) -> list:
    uniq_list = []
    for item in my_list:
        if item not in uniq_list:
            uniq_list.append(item)
    return uniq_list


def main():
    my_list = [1, 2, 1, 4 ,6, 2, 11, 20, 21, 20, 25]

    uniq_list = remove_duplicates(my_list)
    print(uniq_list)


if __name__ == "__main__":
    main()