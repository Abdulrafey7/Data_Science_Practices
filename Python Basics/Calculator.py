#python calculator

print("=========== CALCLATOR ==========")
a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))
op = input("Enter operand (+,-,*,/): ")

if op == '+':
    print(f"Sum is {a+b}")
elif op == '-':
    print(f"Subtraction is {a-b}")
elif op == '*':
    print(f"Multiplication is {a*b}")
elif op == '/':
    print(f"Division is {a/b}")
else:
    print("Unknown operand")

