import random


def start_game():
    num = random.randint(1, 10)
    attempts = 0
    print("Я загадал число от 1 до 10. Попробуй угадать")
    
    while True:
        try:
            guess = int(input("Введите число: "))
        except ValueError:
            print("Ошибка! Введите число!")
            continue
        if guess < num:
            print("Ваше число меньше, чем задумано")
            attempts += 1
        elif guess > num:
            print("Ваше число больше, чем задумано")
            attempts += 1
        else:
            print("Вы угадали!")
            print("Количество попыток:", attempts + 1)
            break
    game(True)


def game(retry: bool = False):
    text = "Угадаете целое число от 1 до 10? (Да/Нет): " if not retry else "Хотите продолжить игру? (Да/Нет):"
    start = input(text)
    
    while start.lower() not in ["да", "нет"]:
        start = input("Пожалуйста, ответьте 'Да' или 'Нет': ")
    
    if start.lower() == "да":
        start_game()
    else:
        print("До свидания!")

game()
