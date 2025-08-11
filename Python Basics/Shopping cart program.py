# list : [] , ordered , changeable , Duplicates OK
# Sets : {} , unordered , changeable , Duplicates not OK
# tuples: () , ordered , unchangeable , Duplicates OK

# SHOPPING CART PROGRAM

items = []
prices = []
total = 0

while True:
    item = input("Enter a item you want to add (Enter 'q' to quit ) : ")
    if item.lower() == 'q':
        break
    else:
        price = input(f"Enter price for {item} $")
        prices.append(float(price))
        items.append(item)

print("\n-------------- YOUR CART --------------\nItems: ", end="")
for item in items:
    print(item, end=" ")

for price in prices:
    total += price

print()
print(f"Your total is: ${total}")
