import tkinter as tk

win = tk.Tk()

win.title("Guess Number")
win.geometry("500x500")
win.configure(bg = 'lightblue')
win.resizable(False, False)

label = tk.Label(win, text = "Hello World! This is a Test!")
label.pack(pady = 20)

def on_button_click():
    label.config(text = "Button is dawn!")

btn = tk.Button(win, text = "Test me", bg = 'white', fg = 'black', command = on_button_click)
btn.pack(expand = True)

btnclose = tk.Button(win, text = "Close", bg = "red", fg = "black", command = win.destroy)
btnclose.place(x = 230, y = 350)

win.mainloop()

