'''
Rotate a given array left by n elements.

Input arr[] = [1, 2, 3, 4, 5, 6, 7, 8] 
size = 8
d = 2

Output = [3, 4, 5, 6, 7, 8, 1, 2]

'''

def rotate_left(arr: list, d: int) -> None:
    """
    Rotate function.
    """
    print(f"Original array: {arr}")
    for _ in range(d):
        element = arr.pop(0)
        arr.append(element)

    print(f"Rotated array left by {d} elements: {arr}")


def main():
    """
    Main function.
    """
    arr = [1, 2, 3, 4, 5, 6, 7, 8]
    d = 2
    rotate_left(arr, d)


if __name__ == "__main__":
    main()
