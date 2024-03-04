'''
Move all zeros to the end of the list.

my_list = [1, 0, 3, 6, 0, 9, 11, 0, 31]

output = [1, 3, 6, 9 , 11, 31, 0, 0, 0]

'''

def move_zeros(my_list: list) -> None:
    """
    Function to move all zeros to end of the list.
    """
    for num in my_list:
        if num == 0:
            my_list.remove(num)
            my_list.append(num)

    print(my_list)

def main():
    """
    Main function.
    """
    my_list = [1, 0, 3, 6, 0, 9, 11, 0, 31]
    move_zeros(my_list)


if __name__ == "__main__":
    main()
