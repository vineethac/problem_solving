'''
Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2]
Explanation: Your function should return length = 2, with the first two elements of nums being 2.
It doesn't matter what you leave beyond the returned length. For example if you return 2 with nums = [2,2,3,3] or nums = [2,3,0,0], your answer will be accepted.

Input: nums = [0,1,2,2,3,0,4,2], val = 2
Output: 5, nums = [0,1,4,0,3]
Explanation: Your function should return length = 5, with the first five elements of nums containing 0, 1, 3, 0, and 4. Note that the order of those five elements can be arbitrary. It doesn't matter what values are set beyond the returned length.

'''

def remove_element(nums: list, val: int) -> None:
    new_list = []
    for i in nums:
        if i != val:
            new_list.append(i)
    
    print(new_list)
    print(len(new_list))


def main():
    nums = [0,1,2,2,3,0,4,2]
    val = 2

    remove_element(nums, val)

if __name__ == "__main__":
    main()