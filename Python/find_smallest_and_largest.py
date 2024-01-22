'''
Find smallest and largest element.
'''


def find_smallest_and_largest(my_list: list) -> int:
    smallest = my_list[0]
    largest = my_list[0]

    for i in range(len(my_list)):
        if my_list[i] < smallest:
            smallest = my_list[i]
        elif my_list[i] > largest:
            largest = my_list[i]
    
    return smallest, largest

def main():
    my_list = [1, 3, 4,7, 123, 54, 29, -65, 86, 98, 111]
    smallest, largest = find_smallest_and_largest(my_list)

    print(f"Smallest: {smallest}")
    print(f"Largest: {largest}")

if __name__ == "__main__":
    main()