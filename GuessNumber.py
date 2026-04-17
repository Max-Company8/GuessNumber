import random

def game():
    num = random.randint(1, 10)
    tryes = 0
    print("Я загадал число от 1 до 10. Попробуй угадать")
    
    while True:
        guess = int(input("Введите число: "))
        
        if guess < num:
            print("Ваше число меньше, чем задумано")
            tryes += 1
        elif guess > num:
            print("Ваше число больше, чем задумано")
            tryes += 1
        else:
            print("Вы угадали!")
            print("Количество попыток:", tryes + 1)
            break

start = input("Угадаете целое число от 1 до 10? (Да/Нет): ")

while start.lower() not in ["да", "нет"]:
    start = input("Пожалуйста, ответьте 'Да' или 'Нет': ")

if start.lower() == "да":
    game()
else:
    print("До свидания!")
