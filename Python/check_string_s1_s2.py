'''
Check if string s1 can be made from string s2.
Upper case and lower case are considered differently.

Input : s1 = ABHISHEKsinGH
      : s2 = gfhfBHkooIHnfndSHEKsiAnG
Output : Possible

'''

def check_string(s1: str, s2: str) -> None:
    """
    Function to check if s1 can be made from s2.
    """
    s2_dict = {}
    s1_dict = {}

    for item in s2:
        count = s2.count(item)
        s2_dict[item] = count

    print(s2_dict)

    for item in s1:
        count = s1.count(item)
        s1_dict[item] = count

    print(s1_dict)

    p = 0
    for key, value in s1_dict.items():
        if key in s2_dict and s1_dict[key] <= s2_dict[key]:
            p = 0
        else:
            p = 1
            break

    if p == 0:
        print("Possible")
    else:
        print("Not possible")



def main():
    """
    Main function.
    """
    s1 = "ABHISHEKsinGH"
    s2 = "gfhfBHkooIHnfndSHEKsiAnG"
    check_string(s1, s2)


if __name__ == "__main__":
    main()
