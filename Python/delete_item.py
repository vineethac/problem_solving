'''
my_list = [5, 7, 2 , 1, 7 , 9, 3]
remove an element from the given list and add it to the end of the list.
'''

def delete_item(my_list: list, element: int) -> None:
    my_list.remove(element)
    print(f"List after deleting element: {my_list}")
    my_list.append(element)
    print(f"List after adding element: {my_list}")

def main():
    my_list = [5, 7, 2 , 1, 7 , 9, 3]
    print(f"Original list: {my_list}")
    
    element = int(input("Enter the item to delete: "))
    delete_item(my_list, element)


if __name__ == "__main__":
    main()

