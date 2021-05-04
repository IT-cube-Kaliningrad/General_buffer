import tkinter as tk
from tkinter import messagebox
import keyboard
import requests
import configparser


def send_data():
    try:
        bufer_data = root.clipboard_get()
        adress = f'http://{SERVER_IP}:{SERVER_PORT}/data'
        res = requests.post(adress, json={'data': bufer_data})
        if not res.ok:
            messagebox.showerror(
                title='Ошибка', message='Данные не отправлены',
            )
    except requests.exceptions.ConnectionError as e:
        messagebox.showerror(
            title='Ошибка', message='Не удается подключится к хосту',
        ); print(e)


def main():
    global root, SERVER_IP, SERVER_PORT

    config = configparser.ConfigParser()
    config.read('settings.conf')
    SHOW_WINDOW = config['WINDOW']['SHOW_WINDOW']
    SERVER_IP = config['SERVER']['SERVER_IP']
    SERVER_PORT = config['SERVER']['SERVER_PORT']

    root = tk.Tk()
    root.title('App')
    root.geometry('200x0')
    root.resizable(width=False, height=False)
    root.wm_attributes('-alpha', float(SHOW_WINDOW))
    root.wm_attributes('-topmost', True)
    keyboard.add_hotkey('ctrl+c', send_data)
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
