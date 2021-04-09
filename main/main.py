from tkinter import Tk, Label, messagebox, LEFT
import keyboard
import requests
import configparser
import sys


# Функция для отправки данных на сервер
def send_data(data):
    requests.post(f'http://{SERVER_IP}:{SERVER_PORT}/', json={'data': data})

# Функция чтения буфера
def read_clipboard(e):
    global bufer_data
    # Получение записи из буфера
    bufer_data = root.clipboard_get()
    # Отправка данных на сервер
    try:
        send_data(bufer_data)
    except requests.exceptions.ConnectionError as e:
        messagebox.showerror(title='Ошибка', message=f'Ошибка отправки данных на сервер\nСкорее всего, вы указали неверный адрес сервера')
    # Изменение текста Label в root
    bufer_label['text'] = bufer_data


if __name__ == '__main__':
    # Инициализация класса для чтения конфигурационных файлов
    config = configparser.ConfigParser()
    config.read('main_settings.conf')
    # Установка переменных
    try:
        SHOW_WINDOW = config['Window']['SHOW_WINDOW']
        KEY = config['Key']['KEY']
        SERVER_IP = config['Server']['SERVER_IP']
        SERVER_PORT = config['Server']['SERVER_PORT']
    except KeyError:
        messagebox.showerror(title='Ошибка', message=f'Не правильно составлен файл конфигурации main_settings.conf')
        sys.exit()

    # Создание основного окна
    root = Tk()
    root.title('Main')
    root.geometry('150x0')
    # Установка прозрачности
    root.wm_attributes('-alpha', float(SHOW_WINDOW))
    # Для того, чтобы окно было всегда поверх других. Это нужно для корректного захвата клавиши
    root.wm_attributes('-topmost', True)

    # Текстовая метка
    bufer_label = Label(root, text=None, justify='left')
    bufer_label.grid(row=0, column=0)

    # Захват клавиши
    keyboard.hook_key(KEY, read_clipboard)

    root.mainloop()