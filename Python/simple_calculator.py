'''
Write a program to add and sub two 
numbers using class.
'''

class Calulator():
    """
    Calculator class.
    """
    def add(self, a, b):
        """
        Add function.
        """
        return a + b

    def sub(self, a, b):
        """
        Sub function.
        """
        return a - b

def main():
    """
    Main function.
    """
    calc = Calulator()

    s1 = calc.add(2, 3)
    s2 = calc.sub(2, 3)
    print(s1)
    print(s2)

if __name__ == "__main__":
    main()
