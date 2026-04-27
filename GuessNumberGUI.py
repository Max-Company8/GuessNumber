mport tkinter as tk
import random
from tkinter import messagebox

win = tk.Tk()
win.title("Guess Number")
win.geometry("500x500")
win.configure(bg = '#81ccf7')
win.resizable(False, False)

num = random.randint(1, 10)
attempts = 0
stop = 0
entry = None

def restart():
    global num, attempts, stop, entry

    num = random.randint(1, 10)
    attempts = 0
    stop = 0
    entry = None

    for widget in win.winfo_children():
        widget.destroy()

    create_widgets()

def create_widgets():
    global label, btn, btnNo, btnOk, btnAgain

    label = tk.Label(
        win,
        text = "Я загадал число от 1 до 10, отгадаешь?",
        bg = "#81ccf7",
        font = ('Times New Roman', 18))
    
    label.pack(pady = 20)

    btn = tk.Button(
        win,
        text = "Да",
        bg = '#FFC57E',
        activebackground = '#A66E29',
        width = 15,
        height = 2,
        command = pole)
    
    btn.place(x = 200, y = 250)

    btnNo = tk.Button(
        win,
        text = "Нет",
        bg = "#FFC57E",
        activebackground = "#A66E29",
        width = 15,
        height = 2,
        command = close)
    
    btnNo.place(x = 200, y = 300)

    btnOk = tk.Button(
        win,
        text = "ОК",
        bg = "#FFC57E",
        activebackground = "#A66E29",
        width = 3,
        height = 1,
        command = check)

    btnAgain = tk.Button(
        win,
        text = "Заново",
        bg = "#FFC57E",
        activebackground = "#A66E29",
        width = 15,
        height = 2,
        command = restart)

def pole():
    global stop, entry
    stop += 1
    if stop == 1:
        entry = tk.Entry(
            win,
            bg = "#77A1B9")
        
        entry.place(x = 200, y = 69, width = 100, height = 25)
        btnOk.place(x = 320, y = 69)
        label.config(text = "Попробуй Угадать")
        btn.destroy()
        btnNo.config(
            text = "Выйти",
            command = lambda: close(entry))
        
        btnNo.pack(expand = True)

def close(entry = None):
    label.config(text = "До Свидания!", font = ('Times New Roman', 25))
    label.pack(expand = True)
    btn.destroy()
    btnNo.destroy()
    btnOk.destroy()
    if entry:
        entry.destroy()
    btnAgain.destroy()
    win.after(1000, win.destroy)

def victory():
    label.config(text = f"Ты угадал! Количество попыток - {attempts}")
    label.pack(expand = True)
    btn.destroy()
    btnOk.destroy()
    entry.destroy()
    btnNo.pack(expand = True)
    btnAgain.place(x = 193, y = 300)

def check():
    global attempts, num
    value = entry.get().strip()

    if not value:
        messagebox.showerror(
            title = "Ошибка ввода!",
            message = "Поле пустое, введите число!")
        
        return
    try:
        user_num = int(value)
    except ValueError:
        messagebox.showerror(
            title = "Ошибка ввода!",
            message = "Вы ввели не число, введите целое число!")
        
        return

    if user_num < num:
        messagebox.showinfo(
            title = "Ой!",
            message = "Ваше число меньше загаданного")
        
        attempts += 1
    elif user_num > num:
        messagebox.showinfo(
            title = "Ой!",
            message = "Ваше число больше, чем загадано")
        
        attempts += 1
    else:
        attempts += 1
        victory()

create_widgets()

win.mainloop()
