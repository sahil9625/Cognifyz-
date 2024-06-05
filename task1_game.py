import random

def guessing_game():
    
    number_to_guess = random.randint(1, 100)
    attempts = 10  

    print("Welcome to the Guessing Game!")
    print("I have selected a number between 1 and 100.")
    print(f"You have {attempts} attempts to guess it correctly.\n")

    
    while attempts > 0:
        guess = int(input("Enter your guess: "))

        if guess < number_to_guess:
            print("Too low!")
        elif guess > number_to_guess:
            print("Too high!")
        else:
            print("Congratulations! You guessed the number correctly.")
            break

        attempts -= 1
        print(f"You have {attempts} attempts left.\n")

    if attempts == 0:
        print(f"Sorry, you have used all your attempts. The number was {number_to_guess}.")


guessing_game()
