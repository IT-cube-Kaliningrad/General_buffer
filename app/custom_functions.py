import os

os_translate = {'nt' : 'Windows', 'posix' : 'Linux', 'mac' : 'MacOS', 'os2' : 'os2', 'ce' : 'ce', 'java' : 'java'}

def get_ip(OS):
    if OS == 'posix' or OS == 'mac':
        os.system('ifconfig | grep "inet" --max-count=1 > ipconfig.file')
        with open('ipconfig.file', 'r') as f:
            text = f.read()
            text = text.split()
            index_inet = text.index('inet')
            return text[index_inet + 1]
    elif OS == 'nt':
        os.system('ipconfig | find "IPv4" > ipconfig.file')
        with open('ipconfig.file', 'r') as f:
            text = f.read()
            text = text.split('\n')
            ip = text[len(text) - 3].split(':')[1]
            return ip.replace(' ', '')
    else:
        print('Не поддерживаемая платформа')
        return '127.0.0.1'