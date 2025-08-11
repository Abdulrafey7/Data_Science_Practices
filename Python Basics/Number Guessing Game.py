#Number Guessing game
import random

x = random.randint(1,100)
guesses = 3

while guesses > 0 :

    guess = int(input("Guess a number between 1 and 100: "))
    if guess == x :
        print("You guessed right!")
        break
    elif guess < x:
        print(f"Your guess is too low.\n{guesses - 1} guess Left !!")
        guesses -= 1
    elif guess > x:
        print(f"Your guess is too high.\n{guesses - 1} guess Left !!")
        guesses -= 1
    if guesses == 0:
        print("Thank You For Playing.")

