'''
Given a list of IP or hostnames of machines.
Write a script that will check whether ssh connection 
to it is successful or not.

'''
import getpass
import paramiko

def verify_ssh_connetion(hosts: list, username: str, password: str) -> None:
    """
    Function that checks ssh connection.
    """
    for host in hosts:
        client = paramiko.client.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            client.connect(host, username=username, password=password)
            print(f"SSH connection to host {host} successful.")
            client.close()
        except:
            print(f"SSH connection to host {host} failed.")

def main():
    """
    Main function.
    """
    hosts = ["h1", "h2", "h3"]
    username = input("Enter username: ")
    password = getpass.getpass(prompt="Enter password: ")

    verify_ssh_connetion(hosts, username, password)


if __name__ == "__main__":
    main()
