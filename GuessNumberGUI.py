import tkinter as tk
import random


win = tk.Tk()
win.title("Guess Number")
win.geometry("500x500")
win.configure(bg = '#81ccf7')
win.resizable(False, False)


def start_game():
    num = random.randint(1, 10)
    attempts = 0
    print("I have a number from 1 to 10. Try to guess it")
    
    while True:
        try:
            guess = int(input("Enter a number: "))
        except ValueError:
            print("Error! Enter the number!")
            continue
        if guess < num:
            print("Your number is less than intended")
            attempts += 1
        elif guess > num:
            print("Your number is higher than intended")
            attempts += 1
        else:
            print("You guessed right!")
            print("Number of attempts:", attempts + 1)
            break
    game(True)

def game(retry: bool = False):
    text = "Can you guess a whole number between 1 and 10? (Yes/No): " if not retry else "Do you want to continue the game? (Yes/No):"
    start = input(text)
    
    while start.lower() not in ["yes", "no"]:
        start = input("Please answer 'Yes' or 'No': ")
    
    if start.lower() == "yes":
        start_game()
    else:
        print("Goodbye!")

label = tk.Label(win, text = "Я загадал число от 1 до 10, отгадаешь?", bg = "#81ccf7", font=('Times New Roman', 18) )
label.pack(pady = 20)

stop = 0

def pole():
    global stop
    stop += 1
    if stop == 1:
        entry = tk.Entry(win, bg = "#77A1B9")
        entry.place(x = 200, y = 69, width = 100, height = 25) 
        btnOk.place(x = 320, y = 69)
        label.config(text = "Попробуй Угадать")
        btn.destroy()
        btnNo.config(text = "Выйти", command=lambda: close(entry))
        btnNo.pack(expand = True)

def close(entry=None):
    label.config(text = "До Свидания!", font=('Times New Roman', 25))
    label.pack(expand = True)
    btn.destroy()
    btnNo.destroy()
    btnOk.destroy()
    entry.destroy() if entry else None
    win.after(1000, win.destroy)
btn = tk.Button(win, text = "Да", bg = '#FFC57E', activebackground = '#A66E29', width = 15, height = 2, command = pole)
btn.place(x = 200, y = 250)

btnNo = tk.Button(win, text = "Нет", bg = "#FFC57E", activebackground = "#A66E29", width = 15, height = 2, command = close)
btnNo.place(x = 200, y = 300)

btnOk = tk.Button(win, text = "ОК", bg = "#FFC57E", activebackground = "#A66E29", width = 3, height = 1)





win.mainloop()

