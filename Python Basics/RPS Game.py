# Rock Paper Scissors game
import random

print("Welcome to Rock Paper Scissors Game :) ")

options = ["Rock", "Paper" , "Scissors"]

running = True

while running:

    choice = input("Choose your option (Rock , Paper , Scissors): ")
    choice = choice.capitalize()

    while choice not in options:
        print("That is not a valid option. Please try again.")
        choice = input("Choose your option (Rock , Paper , Scissors): ")

    option = random.choice(options)
    print(f"Computer : {option}")

    if choice == option:
        print("Its a draw.")
    elif choice == "Rock" and option == "Scissors":
        print("You Win.")
    elif choice == "Paper" and option == "Rock":
        print("You Win.")
    elif choice == "Scissors" and option == "Paper":
        print("You Win.")
    else:
        print("You Lose.")

    re = input("Thank You For Playing.Do you want to play again? (Y/N): ")
    re = re.capitalize()

    if re == "N":
        running = False
