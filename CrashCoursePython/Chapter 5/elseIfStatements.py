## We can use if else and else if statements to create multiple conditions and paths for the code to run through

age = 19

if age >= 21:
    print("You can legally buy alcohol")
elif age >= 18:
    print("You can get your license and legally drive a car")
else:
    print("You need to wait until your 18th birthday")

age2 = 3

if age2 >= 18:
    print("The price of admission is $10")
elif age2 >= 4 and age2 < 18:
    print("The price of admission is $5")
else:
    print("The price of admission is free")

## It's possible to link multiple elif statements together in blocks following the same format shown above
## Furthermore, an else statement is not required at the end of each if elif statement, and you can instead opt to choose an elif statement for clarity

## If you are only checking one test, an if elif conditional statement can check but ends after one of the conditionals checks off.
## Checking multiple conditionals works better using separate if statements:

requested_toppings = ['mushrooms', 'fried egg', 'pepperoni', 'sausage', 'anchovies']
available_toppings = requested_toppings[1:3]

for topping in requested_toppings:
    if topping in available_toppings:
        print(topping + " is available")

print([topping for topping in requested_toppings if topping in available_toppings])

## Exercises

print()

alien_color = 'red'

if alien_color == 'green':
    print("You just earned 5 points!")
elif alien_color == 'yellow':
    print("You just earned 10 points!")
else:
    print("You just earned 15 points!")

ages = [3, 12, 343, 23, 44, 2, 6]

for life in ages:
    if life < 2:
        print("Baby")
    elif life >= 2 and life < 4:
        print("Toddler")
    elif life >= 4 and  life < 13:
        print("Kid")
    elif life >= 13 and life < 20:
        print("Teenager")
    elif life >= 20 and life < 65:
        print("Adult")
    else:
        print("Elderly")

favorite = ['banana', 'apple', 'peach', 'mango']

if 'mango' in favorite:
    print("You really like mangoes!")
if 'grapes' in favorite:
    print("You really like grapes!")
if 'apple' in favorite:
    print("You really like apples!")

