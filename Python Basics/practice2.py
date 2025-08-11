n = 5
n **= 3
print(n)

f = 10
rem = f%3
print(rem)


x = 3.14

# result = round(x) round the float number to the nearest int
# result = abs(x)  change any value into positive
# result = pow(x,y) x raised to the power y
# result = min(x,y,z) // min or maximum value in the bunch

import math

# math.pi
# math.e
# result = math.sqrt(x) for square root of a number
# math.floor = round the float number to the lowest int
# math.ceil = round the float number to the highest int

# calculate the circumference of a circle
import math

r = int(input("Enter the radius"))
r **=2
sq = math.ceil(math.pi * r)

print(f"The Circumference is : {sq}")


# if statements

age = int(input("Enter age"))

if age >= 18:
    print("You are signed")
elif age < 0:
    print("You are not born yet")
else:
    print("you need to be above 18")