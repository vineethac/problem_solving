"""
Input: ar1[] = {-5, 3, 6, 12, 15}
       ar2[] = {-12, -10, -6, -3, 4, 10}
Output : The median is 3.
Explanation : The merged array is :
        ar3[] = {-12, -10, -6, -5 , -3,
                 3, 4, 6, 10, 12, 15},
       So the median of the merged array is 3

Input: ar1[] = {2, 3, 5, 8}
       ar2[] = {10, 12, 14, 16, 18, 20}
Output : The median is 11.
Explanation : The merged array is :
        ar3[] = {2, 3, 5, 8, 10, 12, 14, 16, 18, 20}
        if the number of the elements are even, 
        so there are two middle elements,
        take the average between the two :
        (10 + 12) / 2 = 11.
"""


def median(arr1: list, arr2: list) -> int or float:
    # merge the two arrays
    arr1 += arr2

    # sort
    arr1.sort()

    # find median logic
    if len(arr1) % 2 != 0:
        median = int((len(arr1) + 1) / 2)
        median_element = arr1[median - 1]
    else:
        median = int(len(arr1) / 2)
        median_element = (arr1[median - 1] + arr1[median]) / 2

    return median_element


def main():
    arr1 = [-5, 3, 6, 12, 15, -25]
    arr2 = [-12, -10, 55, 75, -6, -3, 4, 11]

    median_value = median(arr1, arr2)
    print(median_value)
    

if __name__ == "__main__":
    main()
