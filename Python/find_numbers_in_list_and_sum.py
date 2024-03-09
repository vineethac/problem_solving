'''
input = ["abc", "4", "talk", "2", "this"]
From the given input list, find the numbers and print their sum.
output: 4 + 2 = 6

'''

def find_numbers_sum(my_list: list) -> None:
    """
    Function find numbers in a given list and print their sum.
    """
    sum_of_num = 0
    for item in my_list:
        if item.isdigit():
            sum_of_num += int(item)
    print(sum_of_num)


def main():
    """
    Main function.
    """
    my_list = ["abc", "4", "talk", "2", "this", "0", "10"]
    find_numbers_sum(my_list)


if __name__ == "__main__":
    main()
