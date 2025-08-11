
items = {"Pizza":12.64 ,
         "Burger": 8.99 ,
         "Fries":5.75 ,
         "Shake":10 }

print("------------- MENU ---------------")
for key, value in items.items():
    print(f"{key:10}: {value:.2f}")

print("------------------------------")

purchased = []
total = 0
while True:
    item = input("What is your purchase item? (q to quit): ").capitalize()

    if item == "Q":
        break
    else:
        if item in items:
            purchased.append(item)
            print(f"You purchased {item}.")
        else:
            print("Item not found.")

print("------------- YOUR CART ---------------")
print("You Purchased: ")

for item in purchased:
    total += items[item]
    print(f"{item:10}: {items[item]:.2f}")

print(f"your total is: {total}")
print("------------------------------")



