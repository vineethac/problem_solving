'''
Find all pairs of an integer array whose sum is equal to a given number.
'''

def find_pairs_equal_to_sum(numbers: list, sum: int) -> None:
    all_pairs = []
    pair = []

    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if numbers[i] + numbers[j] == sum:
                if i != j:
                    print(f"Pair: {numbers[i]} {numbers[j]}")
                    pair.append(numbers[i])
                    pair.append(numbers[j])

                    # inner lists are converted to string and appended here
                    # then only we can convert it to set to find unique pairs
                    all_pairs.append(str(pair)) 
                    pair = []
    
    uniq_pairs = list(set(all_pairs))
    print("\nUnique pairs\n")
    for item in uniq_pairs:
        print((item))

def main():
    numbers = [1, 3, 4 , 1, 5, 6, 10, 5, 3, 4, 5, 0, 2]
    sum = 5
    find_pairs_equal_to_sum(numbers, sum)


if __name__ == "__main__":
    main()