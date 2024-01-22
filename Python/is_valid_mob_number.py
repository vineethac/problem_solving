'''
A valid mobile number is a ten digit number starting with a 7, 8, or 9.
Input Format

The first line contains an integer N, the number of inputs.
N lines follow, each containing some string.

Sample Input:

2
9587456281
1252478965

Sample Output:

YES
NO
'''

def verify_valid_mob_num(numbers_list: list ) -> None:
    for number in numbers_list:
        if (number[0] == '7' or number[0] == '8' or number[0] == '9') and number.isnumeric() and len(number) == 10:
            print("YES")
        else:
            print("NO")
        

def main():
    number_inputs = int(input())
    numbers_list = []
    
    for _ in range(number_inputs):
        number = input()
        numbers_list.append(number)
    
    verify_valid_mob_num(numbers_list)


if __name__ == "__main__":
    main()
    
    