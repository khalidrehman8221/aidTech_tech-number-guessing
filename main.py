import random

def play_game():
    name = input("Enter your name: ")
    print(f"Welcome, {name}! Lets play the number guessing game.")

    number = random.randint(1, 100)
    attempts = 0

    while attempts <10:
        guess = int(input("ENter your guess (between 1 to 100)"))

        if guess <number:
            print("Too low!")
        elif guess > number:
            print("Too high!")
        else:
            print(f"Congratulations, {name}! You guess the number correct")
            break

        attempts +=1
    if attempts == 10:
        print(f"Game over, You Lose")

    play_again = input("Do you want to play again? (yes/no)")

    if play_again.lower == "yes":
        play_game()
    else:
        print("Thank you")

play_game()
