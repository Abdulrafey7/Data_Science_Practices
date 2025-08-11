# List comprehensions

arr = [x^x for x in range(10)]


numbers = [-1,2,-3,4,-5,-6]
arr = [x for x in numbers if x > 0]


# switch satement

def hello_world(day):
    match day:
        case "Monday":
            print("Hi Monday")
        case "Tuesday":
            print("Hi Tuesday")
        case _:
            print("Hi Sunday")

hello_world("Tuesday")