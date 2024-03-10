'''
Merge two given dict.

d1 = {1: "one", 2: "two"}
d2 = {3: "three", 2: "four"}

'''

def merge_method2(d1, d2):
    """
    This method uses ** method.
    """
    d3 = {**d1, **d2}
    return d3


def merge_method1(d1, d2):
    """
    This function uses update method.
    """
    d1.update(d2)
    return d1


def main():
    """
    Main function.
    """
    d1 = {1: "one", 2: "two"}
    d2 = {3: "three", 4: "four"}

    result1 = merge_method1(d1, d2)
    result2 = merge_method2(d1, d2)
    print(result1)
    print(result2)



if __name__ == "__main__":
    main()
    