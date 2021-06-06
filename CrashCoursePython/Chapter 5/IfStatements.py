## Conditional statements like if statements give coders the ability to filter out information based on what they want
## For example, we can run through a list using a for loop and use an if statement to handle certain values a different way

names = ['Eric', 'Max', 'Bryan', 'Nate', 'Edwin', 'Allinn', 'Josh', 'Daniel']
invitedList = ['Max', 'Daniel', 'Eric', 'Nate']
guestList = []


for name in names:
    for invite in invitedList:
        if(invite == name):
            guestList.append(name)

print(guestList)

## The code above runs through a bunch of names and checks whether they are on the invited list. If so, they are placed on the guest list.

## Check for equality using the double equal sign (==), which seems to work even when the strings don't come from the same place

## Because the equality is case sensitive, normally coders turn the input into lowercase so no case sensitive triggers can occur:

car = 'AuDI'
if(car.lower() == 'audi'):
    print(True)
else:
    print(False)

## We can check for inequality using the (!=) operator:

if(car.lower() != 'AuDI'):
    print('Unidentified name')

## Equality operators basically work for numbers too
## If we want to string multiple conditional operators together, we can use the 'and' keyword to check if both are true:

answer = 20
if(answer < 21 and answer > 19):
    print('The answer has to be 20')

if(answer < 21 and answer < 19):
    print('The answer is less than 19') ## Won't print because one of the conditional operators linked by and returned false

## If you only need one of the two conditional statements to return true, use the 'or' keyword:

answer2 = 50
if(answer2 == 50 or answer2 > 1000000000):
    print('The answer is either 50 or over some insanely high number')

print("")

## We can check whether an element is in a list using the 'in' keyword:

requested_toppings = ['pepperoni', 'mushrooms', 'fried egg', 'pickles']

print('spinach' in requested_toppings)
print('mushrooms' in requested_toppings)

available_topping = 'piss and shid'

if available_topping not in requested_toppings:
    print('This topping is not available')
else:
    print('This topping is available')

## You can set variables to hold boolean values:

isPresent = False

if 'mushrooms' in requested_toppings:
    isPresent = True

print(isPresent)

## Exercises

print("")

name = 'Eric'
print("Is name == 'Eric'? I predict true")
print(name == 'Eric')
print("Is name == 'Allinn'? I predict False")
print(name == "Allinn")

print()

isWildin = False
print("Are you wildin right now? I predict false")
print(isWildin == True)
print("Is you not wildin right now? I predict true")
print(isWildin == False)

print()

patronAge = 12
patronAge2 = 8

if (patronAge > 6 and patronAge < 14) and (patronAge2 > 7 and patronAge2 < 10):
    print('Both patrons are fit to work')
    




