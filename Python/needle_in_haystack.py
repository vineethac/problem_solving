'''
haystack = "seebutsad"
needle = "sad"

"sad" occurs at index 6, so return 6.
if it does not occur, return -1
if it occurs at two indexs, return index of the first occurance.
'''


def check_using_find(haystack: str, needle: str) -> None:
    """
    Using find method. 
    find() returns the first index position where substring is found, else returns -1.
    """
    index = haystack.find(needle)
    print(index)
    if index >= 0:
        print(f"Starting index of the occurance: {index}")
    else:
        print("No occurance!")


def main():
    """
    Main function.
    """

    haystack = "seebutsad"
    needle = "sad"

    check_using_find(haystack, needle)


if __name__ == "__main__":
    main()
