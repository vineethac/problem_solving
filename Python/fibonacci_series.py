'''
Print Fibonacci series.
'''

def fibonacii_series(nterms: int) -> None:
    """
    Function to print Fibonacci series.
    """
    n1 = 0
    n2 = 1
    count = 0

    if nterms <= 0:
        print("Please enter a positive integer!")
    elif nterms == 1:
        print(n1)
    else:
        while count < nterms:
            print(n1)
            nth = n1 + n2
            n1 = n2
            n2 = nth
            count += 1


def main():
    """
    Main function.
    """
    nterms = 5
    fibonacii_series(nterms)


if __name__ == "__main__":
    main()
