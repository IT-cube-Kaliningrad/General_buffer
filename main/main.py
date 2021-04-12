from tkinter import Tk, messagebox
import keyboard
import requests
import configparser


def send_data():
    try:
        bufer_data = root.clipboard_get()
        adress = f'http://{SERVER_IP}:{SERVER_PORT}/'
        requests.post(adress, json={'data': bufer_data})
    except requests.exceptions.ConnectionError as e:
            print(e)
            messagebox.showerror(title='Ошибка', message='Не удается подключится к хосту',)
            root.destroy()

def check_keys(event):
    if event.modifiers:
        try:
            if event.modifiers[0] == 'ctrl' and event.name == 'c':
                send_data()
        except IndexError:
            pass
    else:
        if event.name == 'c':
            send_data()

def main():
    global root, SERVER_IP, SERVER_PORT

    config = configparser.ConfigParser()
    config.read('main_settings.conf')
    SHOW_WINDOW = config['WINDOW']['SHOW_WINDOW']
    SERVER_IP = config['SERVER']['SERVER_IP']
    SERVER_PORT = config['SERVER']['SERVER_PORT']

    root = Tk()
    root.title('Main')
    root.geometry('200x0')
    root.resizable(width=False, height=False)
    root.wm_attributes('-alpha', float(SHOW_WINDOW))
    root.wm_attributes('-topmost', True)
    keyboard.hook(check_keys)
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