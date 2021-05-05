import tkinter as tk
import tkinter.messagebox as msg
import keyboard
import requests
import configparser
import time


class App:
    def __init__(self):
        config = configparser.ConfigParser()
        config.read("settings.conf")

        try:
            self.SHOW_WINDOW = float(config["WINDOW"]["SHOW_WINDOW"])
            self.SERVER_IP = config["SERVER"]["SERVER_IP"]
            self.SERVER_PORT = int(config["SERVER"]["SERVER_PORT"])
        except KeyError as e:
            error("Неправильно составлен или отсутствует файл settings.conf")
            print(e)
        except ValueError as e:
            error("Неправильное значение параметров в файле settings.conf")
            print(e)

        self.root = tk.Tk()
        root = self.root
        root.title("App")
        root.geometry("200x0")
        root.resizable(width=False, height=False)
        root.wm_attributes("-alpha", SHOW_WINDOW)
        root.wm_attributes("-topmost", True)

        keyboard.add_hotkey("ctrl+c", send_data)

        root.mainloop()
    
    def send_data(self):
        time.sleep(0.1)
        try:
            bufer_data = self.root.clipboard_get()
            adress = f"http://{SERVER_IP}:{SERVER_PORT}/data"
            post = requests.post(adress, json={"data": bufer_data})
            if not post.ok:
                self.error("Данные не отправлены")
                print(adress, post.status_code)
        except requests.exceptions.ConnectionError as e:
            self.error("Не удается подключится к хосту")
            print(e)

    def error(self, message): msg.showerror("Ошибка", message)


if __name__ == "__main__":
    App()