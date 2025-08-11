# a interest calculator that founds out how much amount you will owe after a time period
# A = P (1 + R/100)^T

p = float(input("Enter Amount : "))
while not p>0:
    print("Please enter a positive number")
    p = float(input("Enter Amount : "))

r = float(input("Enter Interest Rate : "))
while not r>0:
    print("Please enter a positive number")
    p = float(input("Enter Interest Rate : "))

t = int(input("Enter Number of Years : "))
while not t>0:
    print("Please enter a positive number")
    t = int(input("Enter Number of Years : "))

A = p * pow((1+r/100),t)

print(f"${p:,.2f}")
print(f"${r:,.2f}")
print(f"{t:,}")

print(f"The total amount earned after {t:,} years is ${A:,.2f}")

