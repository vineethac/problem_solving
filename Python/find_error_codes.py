'''
my_input = ['get https//:abc.ex.com webservereer-ekaf213 401 531',
            'put https//:abc.ex.com webservffereer-ekaf213 403 531', 
            'get https//:abc.ex.com webservereer-ekaf213 401 531', 
            'get https//:abc.ex.com webservereer-ekaf213 404 531']

print the code: ['401', '403', '401', '404'] as output from the above given list
also print the number of occurrences of each code

output: 
401 - 2
403 - 1
404 - 1 

'''

def find_error_code(my_input):
    """
    Function to find error codes and their total count.
    """
    error_code_dict = {}
    for line in my_input:
        error_code = line.split()[-2]
        if error_code in error_code_dict:
            error_code_dict[error_code] += 1
        else:
            error_code_dict[error_code] = 1

    print(error_code_dict)


def main():
    """
    Main function.
    """
    my_input = ['get https//:abc.ex.com webservereer-ekaf213 401 531',
                'put https//:abc.ex.com webservffereer-ekaf213 403 531',
                'get https//:abc.ex.com webservereer-ekaf213 401 531',
                'get https//:abc.ex.com webservereer-ekaf213 404 531'
    ]
    find_error_code(my_input)


if __name__ == "__main__":
    main()
