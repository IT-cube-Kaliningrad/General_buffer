import threading
import tkinter as tk
from tkinter.constants import END
import tkinter.messagebox as msg
import configparser
import keyboard
import socket
import time


class Server(socket.socket):
    def __init__(self, host, port, max_connections=5):
        self.connections = []
        address = host, port
        try:
            super().__init__(socket.AF_INET, socket.SOCK_STREAM)
            self.bind(address)
            self.listen(max_connections)
        except OSError as e:
            print(f"{e}\n{':'.join(map(str, address))} - Этот адрес уже используется или IP не действительный")
            exit()
    
    def check_connections(self):
        while True:
            time.sleep(1)
            self.send_data("¤")

    def start(self):
        threading.Thread(target=self.check_connections, daemon=True).start()
        while True:
            connection, sockname = self.accept()
            socknames = map(lambda obj: obj[1], self.connections)
            if sockname[1] in socknames:
                connection.close()
                continue
            self.connections.append((connection, sockname[1]))
            print(f"\nID({sockname[1]}) подключился")
    
    def send_data(self, data):
        for connection in self.connections:
            try:
                connection[0].send(data.encode("utf-8"))
            except (ConnectionResetError, BrokenPipeError) as e:
                print(f"\n{e}\nID({connection[1]}) закрыл соединение")
                self.connections.remove(connection)
                continue

class App:
    def __init__(self):
        self.MAX_COUNT_CHAR = 60
        self.bufer_text = None

        config = configparser.ConfigParser()
        config.read("settings.conf")
        try:
            self.SHOW_WINDOW = int(config["APP"]["SHOW_WINDOW"])
            self.SHOW_DATA = int(config["APP"]["SHOW_DATA"])

            SERVER_PORT = int(config["SERVER"]["SERVER_PORT"])
            SERVER_HOST = config["SERVER"]["SERVER_HOST"]

            MAX_CONNECTIONS = int(config["CONNECTIONS"]["MAX_CONNECTIONS"])
        except KeyError as e:
            self._error("Неправильно составлен или отсутствует файл settings.conf", error=e)
        except ValueError as e:
            self._error("Неправильное значение параметров в файле settings.conf", error=e)
        
        self.server = Server(SERVER_HOST, SERVER_PORT, max_connections=MAX_CONNECTIONS)

        self.root = tk.Tk()
        self.root.withdraw()
        self.root.resizable(False, False)

        if self.SHOW_WINDOW:
            self.root.deiconify()
            self.root.title("App")
            self.root.geometry(f"200x{100*self.SHOW_DATA}")
            self.root.wm_attributes("-topmost", True)

            if self.SHOW_DATA:
                self.root.resizable(True, True)
                self.text_data = tk.Text(self.root, text=self.bufer_text, state=tk.DISABLED)
                self.text_data.pack(expand=True, fill="both")

        keyboard.add_hotkey("ctrl+c", self._send_data)
        keyboard.add_hotkey("ctrl+x", self._send_data)

        threading.Thread(target=self.server.start, daemon=True).start()

        self.root.mainloop()

    def _send_data(self):
        time.sleep(0.1)
        self.bufer_text = self.root.clipboard_get()
        self.server.send_data(self.bufer_text)
        if self.SHOW_DATA: self._show_data()

    def _show_data(self):
        self.root.lift()
        self.text_data.configure(state=tk.NORMAL)
        self.text_data.delete(1.0, END)
        self.text_data.insert(1.0, self.bufer_text)
        self.text_data.configure(state=tk.DISABLED)

    def _error(self, message, error=None):
        msg.showerror("Ошибка", message)
        print(error)