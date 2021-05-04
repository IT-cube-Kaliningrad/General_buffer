import tkinter as tk
from tkinter import messagebox
import requests
import configparser
import pyperclip
import threading
import time


MAX_CHARS_LEN = 60

bufer_text = None


def show():
    if len(bufer_text) > MAX_CHARS_LEN:
        label_data['text'] = bufer_text[:MAX_CHARS_LEN] + '...'
    else:
        label_data['text'] = bufer_text
    root.wm_attributes('-alpha', 1.0)

def get_data():
    global bufer_text
    while True:
        try:
            adress = f'http://{SERVER_IP}:{SERVER_PORT}/data'
            res = requests.get(adress)
            if res.ok:
                text_getted = res.text
                if text_getted != bufer_text:
                    bufer_text = text_getted
                    if AUTOCOPY:
                        copy()
                    else:
                        show()
                        root.wm_attributes('-alpha', 0.0)
            else:
                messagebox.showerror(
                title='Ошибка', message='Данные не обнаружены',
            )
        except requests.exceptions.ConnectionError as e:
            messagebox.showerror(
                title='Ошибка', message='Не удается подключится к хосту',
            ); print(e)
            root.destroy()
        time.sleep(1)


def copy():
    pyperclip.copy(bufer_text)

def main():
    global root, label_data, SERVER_IP, SERVER_PORT, AUTOCOPY

    config = configparser.ConfigParser()
    config.read('settings.conf')
    SERVER_IP = config['SERVER']['SERVER_IP']
    SERVER_PORT = config['SERVER']['SERVER_PORT']

    AUTOCOPY = config['APP']['AUTOCOPY']

    root = tk.Tk()
    root.title('App')
    root.geometry(f'300x100+{root.winfo_screenwidth() - 300}+0')
    root.resizable(False, False)
    root.wm_attributes('-topmost', True)
    root.wm_attributes('-alpha', 0.0)

    label_data = tk.Label(root, justify='left')
    label_data.grid(row=0, column=0, sticky='W')

    button_copy_data = tk.Button(root, text='Копировать', command=copy)
    button_copy_data.grid(row=1, column=0, sticky='SW')

    thread_data = threading.Thread(target=get_data, daemon=True)
    thread_data.start()

    root.mainloop()


if __name__ == '__main__':
    try:
        main()
    except KeyError as e:
        messagebox.showerror(
            title='Ошибка',
            message='Неправильно составлен или отсутствует файл settings.conf',
        ); print(e)
    except ValueError as e:
        messagebox.showerror(
            title='Ошибка',
            message='Неправильное значение параметров в файле settings.conf',
        ); print(e)
