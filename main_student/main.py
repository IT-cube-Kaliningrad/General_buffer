from tkinter import*
from tkinter import messagebox
import requests
from bs4 import BeautifulSoup
import configparser
import pyperclip
import threading
import time


text = None


def new_data():
    label_data['text'] = text
    root.wm_attributes('-alpha', 1.0)

def get_data():
    global text
    while True:
        try:
            adress = f'http://{SERVER_IP}:{SERVER_PORT}/'
            res = requests.get(adress)
            soup = BeautifulSoup(res.text, features='lxml')
            textarea_text = soup.find('textarea').text
            if textarea_text != text:
                text = textarea_text
                new_data()
        except requests.exceptions.ConnectionError as e:
                print(e)
                messagebox.showerror(title='Ошибка', message='Не удается подключится к хосту',)
                root.destroy()

def copy():
    pyperclip.copy(text)
    root.wm_attributes('-alpha', 0.0)

def main():
    global root, label_data, SERVER_IP, SERVER_PORT, SCREEN_WIDTH

    config = configparser.ConfigParser()
    config.read('main_settings.conf')
    SERVER_IP = config['SERVER']['SERVER_IP']
    SERVER_PORT = config['SERVER']['SERVER_PORT']

    root = Tk()
    root.title('Main')
    root.overrideredirect(True)
    SCREEN_WIDTH = root.winfo_screenwidth()
    root.config(bg='white')
    root.wm_attributes('-topmost', True)
    root.wm_attributes('-alpha', 0.0)
    root.geometry(f'300x100+{SCREEN_WIDTH - 300}+0')
    

    label_data = Label(root, justify='left', bg='white')
    label_data.pack()

    button_copy_data = Button(root, text='Копировать', command=copy)
    button_copy_data.pack(expand=True, anchor=SW)

    thread_data = threading.Thread(target=get_data, daemon=True)
    thread_data.start()
    
    root.mainloop()

if __name__ == '__main__':
    try: 
        main()
    except KeyError as e:
        messagebox.showerror(
            title='Ошибка',
            message='Неправильно составлен или отсутствует файл main_settings.conf',
        )
    except ValueError as e:
        messagebox.showerror(
            title='Ошибка',
            message='Неправильное значение параметров в файле main_settings.conf',
        )