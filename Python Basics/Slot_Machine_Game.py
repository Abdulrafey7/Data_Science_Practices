import random , time

def rotaterow(row):
    return [random.choice(row) for _ in range(3)]

def printrow(row):

    print("Rotating Machine")
    for i in range(3):
        print(row[i] , end = " ")
        time.sleep(1)
    print()

def calcuatePayout(row , bet):

    if row[0] == row[1] == row[2]:
        if row[0] == "💲":
            return bet * 20
        elif row[0] == "🍌":
            return bet * 2
        elif row[0] == "🍒":
            return bet * 10
        else:
            return 0
    else:
        print("Too bad you lost !! better luck next time")
        return 0

def main():

    balance = 100

    print("Welcome to Slot Machine!")
    running = True

    while running:

        print("Balance =", balance)
        choice = input("Enter the amount you would like to bet: ")

        if not choice.isdigit():
            print("Invalid choice !!")
            continue

        choice = int(choice)

        if choice<0:
            print("Bet Can't be less than 0 !!")
            continue

        if choice>=balance:
            print("Bet cannot be greater than your balance !!")
            continue

        balance -= choice

        emoji = ["💲","🍌","🍒","❌"]

        row = rotaterow(emoji)

        printrow(row)

        payout = calcuatePayout(row, balance)

        print("Payout = $", payout)

        balance += payout

        end = input("Press any key to continue and E to exit : ")

        if end=="E" or end=="e":
            running = False

if __name__ == '__main__':
    main()













"""
def rotate(slot1,slot2,slot3):
    for j in range(3):
        rotation_factor = random.randint(1,6)
        for i in range(rotation_factor):
            temp = slot1[j]
            slot1[j] = slot2[j]
            slot2[j] = slot3[j]
            slot3[j] = temp
    return slot1 , slot2 , slot3




slot1 = ["*","*","*"]
slot2 = ["@","@","@"]
slot3 = ["$","$","$"]

if __name__ == "__main__":
    print("Welcome To Slot Machine Game ")
    print("* = $1 , @ = $2 , $ = 5$ , if u score 3 of same kind you will win a jackpot of $100 ")

    running = True
    while running:

        inp = input("To Start Press A")
        if inp == "A" or 'a':
            slot1, slot2, slot3 = rotate(slot1,slot2,slot3)
            print("The slot is: ",slot2)
            prize = 0

            if slot2[0] == slot2[1] == slot2[2]:
                prize = 100
                print(" CONGRATULATIONS YOU WON THE JACKPOT OF $100 ")
            else:
                for i in range(3):
                    if slot1[i] == '*':
                        prize = prize + 1
                    elif slot1[i] == '@':
                        prize = prize + 2
                    else:
                        prize = prize + 5
                print("The prize is: ", prize)

        else:
            print("Invalid choice !!")

"""