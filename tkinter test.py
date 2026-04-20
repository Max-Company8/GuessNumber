from tkinter import *
 
root = Tk()     # создаем корневой объект - окно
root.title("Guess Number")     # устанавливаем заголовок окна
root.geometry("500x500")    # устанавливаем размеры окна
 
label = Label(text="Hello World! This is a Test!") # создаем текстовую метку
label.pack()    # размещаем метку в окне
 
root.mainloop()
