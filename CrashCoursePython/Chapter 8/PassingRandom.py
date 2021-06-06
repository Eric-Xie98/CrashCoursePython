## Sometimes we don't know how many arguments we're going to pass into the function, so Python let's use the * 
## and create a tuple that takes in arguments:

def make_pizza(*toppings):

    for topping in toppings:
        print(topping)

## No matter how many arguments are given, Python treats them the same and packs them into the tuple

make_pizza('macaroni', 'bacon', 'pepperoni', 'joe')
print()
make_pizza('me')

## If we want the function to accept both positional and arbitrary arguments, the arbitrary argument must
## go last, so it can have an unlimited number:

def userList(ageAll, *names):
    print("Age: " + str(ageAll))
    
    print("Names: ", end = '')
    for name in names:
        print(name.title(), end = " ")

userList(17, 'eric', 'max', 'alina', 'edwin', 'nate')

## Now that we know arbitrary arguments, what about arbitrary keyword arguments? Oh yeah.
## You can now write functions that accept as many key value pairs as necessary:

print()

def buildProfile(first, last, **user_info):     ## double asterisk indicates arbitrary keyword arguments

    profile = {}
    profile['first_name'] = first.title()
    profile['last_name'] = last.title()

    for key, value in user_info.items():
        profile[key] = value
    
    return profile

## This time Python creates a dictionary for the arbitrary keyword arguments. Similar to the previous arbitrary,
## we access the elements this time like a dictionary

user1 = buildProfile('albert', 'einstein', location = 'princeton', age = '67', field = 'physics')
print(user1)

## Exercises

print()

def sandwich(*ingredients):

    for ingredient in ingredients:
        print("Adding: " + ingredient.title())

sandwich('mayo', 'tomato')
sandwich('ham', 'cheese', 'bacon', 'dick', 'balls')
sandwich('fettucini')

print()

print(buildProfile('eric', 'xie', age = '19', university = 'duke', location = 'home'))

print()

def carProfile(manufacturer, model_name, **car_info):
    
    profile = {}
    profile['manufacturer'] = manufacturer
    profile['model_name'] = model_name
    
    for key, value in car_info.items():
        profile[key] = value
    
    return profile

print(carProfile('honda', 'toyota s4 rc', color = 'red', wheels = 4, convertible = True))

