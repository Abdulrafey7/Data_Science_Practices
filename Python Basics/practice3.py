'''name: str = input("What is your name?")

# to find the length of the string
length = len(name)
print(length)

# to find the first occurance of a character in a string
f = name.find('r')
print(f)

# to find the last occurance of a character in a string
f2 = name.rfind('a')
print(f2)

# captalize the first letter
name = name.capitalize()
print(name)

# captalize the whole string
name2 = name.upper()
'''

# A program to take a correct password from the user
# It cannot include spaces

"""

password = input("Enter your password: ")

if len(password) < 4:
    print("Your password is too short")
elif len(password) > 16:
    print("Your password is too long")
elif not password.find(" ") == -1:
    print("Your passowrd must not contain spaces")
elif password.isalpha() == True:
    print("Your password must contain atleast one number")
else:
    print(f"Hi User you password is: {password}")

"""

# for string indexing u can use array[start:end:step]

ccn = "1234-4567-8912-3456"

#print(ccn[0:4]) // print from 0 to 3
#print(ccn[4::2]) // print from 4 to end jumping every 2nd digit
#print(ccn[::-1]) // printing in reverse order






