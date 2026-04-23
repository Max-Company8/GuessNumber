import random


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

game()
