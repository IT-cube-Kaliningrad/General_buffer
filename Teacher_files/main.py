from tkinter import*
import keyboard

# Основное окно
tk = Tk()
tk.title('Teacher')
tk.geometry('0x0')
tk.overrideredirect(True)

# Пока что пустая переменная с данными из буфера
bufer_data = None

# Текстовая метка с содержимым bufer_data
bufer_label = Label(tk, text = bufer_data)
bufer_label.pack()

# Чтение из буфера
def read(e):
    global bufer_data
    bufer_data = tk.clipboard_get()
    print(bufer_data)
    bufer_label['text'] = bufer_data
    tk.update()

tk.bind('<Control-c>', read)

tk.mainloop()