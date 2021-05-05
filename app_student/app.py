import tkinter as tk
import tkinter.messagebox as msg
import requests
import configparser
import pyperclip
import threading
import time


class App:
    def __init__(self):
        self.MAX_CHARS = 60
        self.bufer_text = None
        try:
            config = configparser.ConfigParser()
            config.read('settings.conf')

            self.SERVER_IP = config['SERVER']['SERVER_IP']
            self.SERVER_PORT = int(config['SERVER']['SERVER_PORT'])

            self.AUTOCOPY = int(config['APP']['AUTOCOPY'])

            {0: self.gui, 1: self.auto_data}[self.AUTOCOPY]()
        except KeyError as e:
            self.error("Неправильно составлен или отсутствует файл settings.conf")
            print(e)
        except ValueError as e:
            self.error("Неправильное значение параметров в файле settings.conf")
            print(e)
    
    def gui(self):
        self.root = tk.Tk()
        root = self.root
        root.title('App')
        root.geometry(f'300x100+{root.winfo_screenwidth() - 300}+0')
        root.resizable(False, False)
        root.wm_attributes('-topmost', True)
        root.wm_attributes('-alpha', 0.0)

        self.label_data = tk.Label(root, justify='left')
        self.label_data.grid(row=0, column=0, sticky='W')

        button_copy_data = tk.Button(root, text='Копировать', command=lambda: self.copy(root))
        button_copy_data.grid(row=1, column=0, sticky='SW')

        thread_data = threading.Thread(target=self.auto_data, daemon=True)
        thread_data.start()

        root.mainloop()
    
    def auto_data(self):
        while True:
            try:
                adress = f'http://{self.SERVER_IP}:{self.SERVER_PORT}/data'
                res = requests.get(adress)
                if res.ok:
                    text_getted = res.text
                    if text_getted != self.bufer_text:
                        self.bufer_text = text_getted
                        {0: self.show, 1: self.copy}[self.AUTOCOPY]()
                else:
                    self.error('Данные не обнаружены')
            except requests.exceptions.ConnectionError as e:
                self.error('Не удается подключится к хосту')
                print(e)
                exit(1)
            time.sleep(1)
    
    def error(self, message):
        msg.showerror("Ошибка", message)

    def show(self):
        self.label_data['text'] = self.bufer_text[:self.MAX_CHARS]
        self.root.wm_attributes('-alpha', 1.0)

    def copy(self, root=None):
        pyperclip.copy(self.bufer_text)
        if root: root.wm_attributes('-alpha', 0.0)

if __name__ == '__main__':
    App()