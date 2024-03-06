'''
Convert two given lists to a dict.

list1 = [1, 2, 3]
list2 = ["one", "two", "three"]

output = {1: "one", 2: "two", 3: "three"}

'''

def list_to_dict(list1: list, list2: list) -> None:
    """
    Function to convert two lists to dict using the zip function.
    """
    result = dict(zip(list1, list2))
    print(result)


def main():
    """
    Main function.
    """
    list1 = [1, 2, 3]
    list2 = ["one", "two", "three"]

    list_to_dict(list1, list2)


if __name__ == "__main__":
    main()
