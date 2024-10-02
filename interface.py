import tkinter as tk
import subprocess
from tkinter import ttk
from file import *
# Функция для шифрования (заглушка)
def encrypt():
    Code(key_var_e, key_var_f)

def decrypt():
    Code(key_var_e1, key_var_f1)
 
# Функция для открытия файла
def open_file(filename):
    try:
        subprocess.run(['start', filename], shell=True)
    except FileNotFoundError:
        print(f"File {filename} not found.")

def readMSGinfile(filename): 
    f1 = open(filename, "r", encoding='utf8')
    msg = f1.read()
    f1.close()
    return msg
 
# Создание главного окна
root = tk.Tk()
root.title("Feistel Network")
root.geometry("500x500")


# Создание вкладок
tab_control = ttk.Notebook(root)

tab_encrypt = ttk.Frame(tab_control)
tab_decrypt = ttk.Frame(tab_control)

tab_control.add(tab_encrypt, text='Encode'  )
tab_control.add(tab_decrypt, text='Decode'  )

# Добавление элементов на вкладку "Шифрование"
label_key_encrypt = tk.Label(tab_encrypt, text="Key:")
label_key_encrypt.grid(row=1, column=0, padx=10, pady=0)
button_view_ci_key = tk.Button(tab_encrypt, text="View key", command=lambda: open_file("ci_key.txt"))
button_view_ci_key.grid(row=1, column=4, padx=10, pady=0)

label_key_encrypt = tk.Label(tab_encrypt, text="Result message:")
label_key_encrypt.grid(row=2, column=0, padx=10, pady=0)
button_view_ci_key = tk.Button(tab_encrypt, text="View message", command=lambda: open_file("ci_message.txt"))
button_view_ci_key.grid(row=2, column=4, padx=10, pady=0)

button_decrypt = tk.Button(tab_encrypt, text="Encode", command=encrypt, font=15, bg='lightblue')
button_decrypt.grid(row=4, column=0, columnspan=4, rowspan=4, pady=20)

# Переключатель для выбора типа ключа
key_var_e = tk.StringVar()
key_var_e.set("0")  # Значение по умолчанию

key_type_frame = tk.Frame(tab_encrypt)
key_type_frame.grid(row=1, column=1, padx=10, pady=10)

key_type_label = tk.Label(key_type_frame, text="Choose subkey:")
key_type_label.pack()

key_type_scramble1 = tk.Radiobutton(key_type_frame, text="a", variable=key_var_e, value="0")
key_type_scramble1.pack(anchor='w')

key_type_scramble2 = tk.Radiobutton(key_type_frame, text="b", variable=key_var_e, value="1")
key_type_scramble2.pack(anchor='w')

# Переключатель для выбора функции
key_var_f = tk.StringVar()
key_var_f.set("0")  # Значение по умолчанию

key_type_frame = tk.Frame(tab_encrypt)
key_type_frame.grid(row=1, column=2, padx=10, pady=10)

key_type_label = tk.Label(key_type_frame, text="Choose generating function:")
key_type_label.pack()

key_type_scramble1 = tk.Radiobutton(key_type_frame, text="a", variable=key_var_f, value="0")
key_type_scramble1.pack(anchor='w')

key_type_scramble2 = tk.Radiobutton(key_type_frame, text="b", variable=key_var_f, value="1")
key_type_scramble2.pack(anchor='w')

# Добавление элементов на вкладку "Дешифрование"
label_message_encrypt = tk.Label(tab_decrypt, text="Message:")
label_message_encrypt.grid(row=1, column=0, padx=10, pady=10)

button_open_message_encrypt = tk.Button(tab_decrypt, text="View decode message", command=lambda: open_file("decode_message.txt"))
button_open_message_encrypt.grid(row=1, column=4, padx=10, pady=10)

label_key_encrypt = tk.Label(tab_decrypt, text="Key:")
label_key_encrypt.grid(row=0, column=0, padx=1, pady=10)
button_view_ci_key = tk.Button(tab_decrypt, text="View key", command=lambda: open_file("ci_key.txt"))
button_view_ci_key.grid(row=0, column=4, padx=10, pady=0)
# Переключатель для выбора типа ключа
key_var_e1 = tk.StringVar()
key_var_e1.set("0")  # Значение по умолчанию

key_type_frame = tk.Frame(tab_decrypt)
key_type_frame.grid(row=0, column=1, padx=10, pady=10)

key_type_label = tk.Label(key_type_frame, text="Choose subkey:")
key_type_label.pack()

key_type_scramble1 = tk.Radiobutton(key_type_frame, text="a", variable=key_var_e1, value="0")
key_type_scramble1.pack(anchor='w')

key_type_scramble2 = tk.Radiobutton(key_type_frame, text="b", variable=key_var_e1, value="1")
key_type_scramble2.pack(anchor='w')

# Переключатель для выбора функции
key_var_f1 = tk.StringVar()
key_var_f1.set("0")  # Значение по умолчанию

key_type_frame = tk.Frame(tab_decrypt)
key_type_frame.grid(row=0, column=2, padx=10, pady=10)

key_type_label = tk.Label(key_type_frame, text="Choose generating function:")
key_type_label.pack()

key_type_scramble1 = tk.Radiobutton(key_type_frame, text="a", variable=key_var_f1, value="0")
key_type_scramble1.pack(anchor='w')

key_type_scramble2 = tk.Radiobutton(key_type_frame, text="b", variable=key_var_f1, value="1")
key_type_scramble2.pack(anchor='w')

button_decrypt = tk.Button(tab_decrypt, text="Decode", command=decrypt, font=15, bg='lightblue')
button_decrypt.grid(row=4, column=0, columnspan=4, rowspan=4, pady=20)

# Кнопка для просмотра начального значения ключа
button_view_initial_value = tk.Button(root, text="View initial key", command=lambda: open_file("key.txt"))
button_view_initial_value.pack(pady=10)

button_open_message_encrypt = tk.Button(root, text="View message", command=lambda: open_file("message.txt"))
button_open_message_encrypt.pack(pady=10)

# Добавление вкладок в главное окно
tab_control.pack(expand=1, fill='both')

# Запуск главного цикла обработки событий
root.mainloop()