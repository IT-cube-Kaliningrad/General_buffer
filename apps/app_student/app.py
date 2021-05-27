import tkinter as tk
import tkinter.messagebox as msg
import socket
import configparser
import threading


class Client(socket.socket):
    def __init__(self, host, port, id=None):
        address = host, port
        super().__init__(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.connect(address)
            print("ID:", self.getsockname()[1])
        except (ConnectionRefusedError, BrokenPipeError) as e:
            print(e, f"\nНе удается подключиться к серверу {':'.join(map(str, address))}")
            exit()
    
    def get_data(self, size=1024):
        data = self.recv(size).decode("utf-8")
        if data and not "¤" in data:
            return data
        return None

class App:
    def __init__(self):
        self.bufer_text = "NULL"

        config = configparser.ConfigParser()
        config.read("settings.conf")

        try:
            SERVER_PORT = int(config["SERVER"]["SERVER_PORT"])
            SERVER_IP = config["SERVER"]["SERVER_IP"]

            self.AUTOCOPY = int(config["APP"]["AUTOCOPY"])

            self.client = Client(SERVER_IP, SERVER_PORT)
        except KeyError as e:
            self._error("Неправильно составлен или отсутствует файл settings.conf", error=e)
        except ValueError as e:
            self._error("Неправильное значение параметров в файле settings.conf", error=e)

        self.root = tk.Tk()
        if not self.AUTOCOPY:
            root = self.root
            root.title("App")
            root.columnconfigure(0, weight=True)
            root.rowconfigure(0, weight=True)
            root.geometry(f"300x150+{root.winfo_screenwidth() - 300}+0")
            root.wm_attributes("-topmost", True)
            root.withdraw()

            self.text_data = tk.Text(self.root)
            self.text_data.insert(0.0, self.text_data)
            self.text_data.config(bd=0, highlightthickness=0, state="disabled")
            self.text_data.grid(row=0, column=0, sticky="NSWE")

            tk.Button(root, text="Копировать", command=self._copy).grid(row=1, column=0, sticky="WE")

            threading.Thread(target=self._auto_data, daemon=True).start()

            root.mainloop()
            exit()

        self._auto_data()
        
    def _auto_data(self):
        while True:
            data = self.client.get_data()
            if data and data != self.bufer_text:
                self.bufer_text = data
                (self._show, self._copy)[self.AUTOCOPY]()

    def _show(self):
        self.root.lift()
        self.text_data["state"] = "normal"
        self.text_data.delete(0.0, "end")
        self.text_data.insert(0.0, self.bufer_text)
        self.text_data["state"] = "disabled"
        self.root.deiconify()

    def _copy(self):
        self.root.clipboard_append(self.bufer_text)
        self.root.withdraw()
    
    def _error(self, message, error=None):
        msg.showerror("Ошибка", message)
        print(error)

def main():
    try:
        App()
    except KeyboardInterrupt:
        print("\nПриложение принудительно остановлено")
    except Exception as e:
        print(f"Неизвестная ошибка\nError: {e}")

if __name__ == "__main__":
    main()