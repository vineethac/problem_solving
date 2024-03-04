'''
Print prime numbers within a given interval.
'''


def prime_numbers(lower: int, upper: int) -> None:
    """
    Function to find and print prime numbers within a given range.
    """
    for num in range(lower, upper + 1):
        if num > 1:
            for i in range(2, num):
                if num % i == 0:
                    break
            else:
                print(num)


def main():
    """
    Main function.
    """
    lower = 1
    upper = 15
    prime_numbers(lower, upper)


if __name__ == "__main__":
    main()
