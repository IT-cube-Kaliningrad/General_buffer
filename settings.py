import os
import sys
import argparse

OS = os.name

def update_ip():
    if OS == 'nt':
        os.system("ipconfig > ipconfig.txt")
    elif OS == 'posix' or OS == 'mac':
        os.system("ifconfig > ipconfig.txt")

if __name__ == '__main__':
    args = sys.argv[1:]
    if args == [] or args[0] == '--help':
