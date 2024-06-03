'''
Factorial of a given number.
num = 3
factorial = 3 x 2 x 1 = 6

'''

class Factorial():
    """
    Factorial class.
    """
    def factorial(self, num: int) -> int:
        """
        Factorial method.
        """
        if (num == 0 or num == 1):
            return 1
        return num * self.factorial(num - 1)


def main():
    """
    Main function.
    """
    num = int(input("Enter a number: "))
    fac = Factorial()
    result = fac.factorial(num)
    print(f"Factorial of {num} is {result}")


if __name__ == "__main__":
    main()
