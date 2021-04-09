from tkinter import*
from main_settings import*
import keyboard

# Основное окно
tk = Tk()
tk.title('Teacher')
tk.geometry('150x0')
tk.wm_attributes('-alpha', float(SHOW_WINDOW))
tk.wm_attributes('-topmost', True)

# Пока что пустая переменная с данными из буфера
bufer_data = None

# Текстовая метка с содержимым bufer_data
bufer_label = Label(tk, text=bufer_data, justify=LEFT)
bufer_label.grid(row=0, column=0)

# Чтение из буфера
def read(e):
    global bufer_data
    bufer_data = tk.clipboard_get()
    if SHOW_BUFER_DATA:
        bufer_label['text'] = bufer_data
        tk.update()

if ADD_CUSTOM_KEY:
    keyboard.hook_key(CUSTOM_KEY, read)
else:
    keyboard.hook_key('c', read)

tk.mainloop()