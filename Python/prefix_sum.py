'''
Prefix sum

Input: arr = [10, 20, 10, 5, 15]
Output: prefix_sum = [10, 30, 40, 45, 60]

'''

def prefix_sum(arr: list) -> list:
    """
    Function to calculate prefix sum.
    """
    prefixsum = [0]
    for i in range(len(arr)):

        # add current element of arr to the last element of prefix_sum
        sum = arr[i] + prefixsum[-1]
        prefixsum.append(sum)

    # remove the 0 from index 0 of prefix_sum list using del or pop
    # del prefixsum[0]
    prefixsum.pop(0)
    return prefixsum


def main():
    """
    Main function.
    """
    arr = [10, 20, 10, 5, 15]
    result = prefix_sum(arr)
    print(f"Original input: {arr}")
    print(f"Final result: {result}")


if __name__ == "__main__":
    main()
