import requests
import sys

def main(*args):
    args = args[0]
    try:
        if args[2] == '--post' or args[2] == '-p':
            req = requests.post(args[1], json={args[5]: args[3]})
            print(req)
    except ArithmeticError:
        print('USAGE: python3 server_test.py {web} [-p|--post] {data} [-h|--header] {header}')

if __name__ == '__main__':
    print(sys.argv)
    main(sys.argv)