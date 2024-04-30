'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

'''

def find_longest_prefix(strs: str) -> None:
    """
    Function to find longest common prefix.
    """
    strs.sort(key=len)
    check_word = strs[0]
    longest_prefix = ""
    flag = 0

    for i in range(len(check_word)):
        for word in strs[1:]:
            if check_word[i] != word[i]:
                flag = 1
        
        if flag == 0:
            longest_prefix += check_word[i]

    if not longest_prefix:
        print("No longest common prefix!")
    else:
        print(f"Longest common prefix: {longest_prefix}")

def main():
    """
    Main function.
    """
    strs = ["fabo","fabb","fab"]
    find_longest_prefix(strs)


if __name__ == "__main__":
    main()
