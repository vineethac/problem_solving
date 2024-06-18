'''
Given a list of IPs in a file. Read from the file and 
check if they are reachable over the network.

'''

import os


def ping_check(data: str) -> None:
    """
    Function that checks IP reachability.
    """
    for ip in data.splitlines():
        response = os.system("ping -c 1 " + ip + ">/dev/null 2>&1")
        if response == 0:
            print(f"{ip} is reachable.")
        else:
            print(f"{ip} is not reachable.")


def read_file(file_path: str) -> str:
    """
    Function to read from file.
    """
    with open(file_path, encoding="utf-8") as f:
        data = f.read()
    return data


def main():
    """
    Main function.
    """
    file_path = input("Enter the IP list file name: ")
    data = read_file(file_path)
    ping_check(data)


if __name__ == "__main__":
    main()
