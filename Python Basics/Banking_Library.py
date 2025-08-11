

def deposit(current_amount,depositing_amount=0):
    if depositing_amount < 0:
        print("Depositing amount can't be negative !!")
    else:
        current_amount = current_amount + depositing_amount
    return current_amount

def withdraw(current_amount,withdrawing_amount=0):
    if current_amount < withdrawing_amount:
        print("Not enough money to withdraw !!")
    else:
        current_amount = current_amount - withdrawing_amount
    return current_amount

def show_balance(balance):
    print("Current Balance : ",balance)

def main():

    current_amount = 0
    is_running = True
    print("Banking Program")
    print("1. Show Balance")
    print("2. Deposit Amount")
    print("3. Withdraw Amount")

    while is_running:


        choice = input("Enter your choice : ")

        if choice == "1":
            show_balance(current_amount)
        elif choice == "2":
            da = int(input("Enter the amount you want to deposit : "))
            current_amount = deposit(current_amount , da)
        elif choice == "3":
            wa = int(input("Enter the amount you want to withdraw : "))
            current_amount = withdraw(current_amount,wa)
        else:
            print("Invalid choice !!")

        while True:
            c = input("Do you want to continue? (y/n) : ")

            if c == "n" or c == "N":
                is_running = False
                break
            elif c == "y" or c == "Y":
                break
            else:
                print("Invalid choice !!")



if __name__ == "__main__":
    main()
