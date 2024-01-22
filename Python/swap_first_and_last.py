'''
Swap first and last elements of a given list.
Multiple ways to solve it are given below.

'''

def swap3(my_list: list) -> None:
    """
    Using pop method.
    """
    print(f"Original list: {my_list}")
    first = my_list.pop(0)
    last = my_list.pop(-1)

    my_list.insert(0, last)
    my_list.append(first)
    print(f"List after swap: {my_list}")


def swap2(my_list: list) -> None:
    """
    Using operand method.
    """
    print(f"Original list: {my_list}")

    start, *middle, end = my_list
    my_list = [end, *middle, start]
    
    print(f"List after swap: {my_list}")


def swap1(my_list: list) -> None:
    """
    Using temp variable.
    """
    first_item = my_list[0]
    last_item = my_list[-1]
    
    print(f"Original list: {my_list}")

    my_list[0] = last_item
    my_list[-1] = first_item

    print(f"List after swap: {my_list}")


def main():
    my_list = [4, 7, 2, 1, 9, 6]
    swap1(my_list) #using temp variable
    swap2(my_list) #using operand method
    swap3(my_list) #using pop method

if __name__ == "__main__":
    main()