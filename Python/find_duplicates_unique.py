'''
Find duplicate elements from a given list and print.
AND
Remove duplicate elements from a given list and print unique list.

Example:
Input list = [1, 2, 1, 4 ,6, 2, 11, 2]
Output 
unique_list = [1, 2, 4, 6, 11]
dup_list = [1, 2, 20]
'''

def find_duplicates_unique(my_list: list) -> list:
    uniq_list = []
    dup_list = []
    for item in my_list:
        if item not in uniq_list:
            uniq_list.append(item)
        else:
            dup_list.append(item)
    return dup_list, uniq_list


def main():
    my_list = [1, 2, 1, 4 ,6, 2, 11, 20, 21, 20, 25]

    dup_list, unique_list = find_duplicates_unique(my_list)
    print(f"\nOriginal list: {my_list}")
    print(f"\nDuplicate elements list: {dup_list}")
    print(f"\nUnique elements list: {unique_list}")


if __name__ == "__main__":
    main()