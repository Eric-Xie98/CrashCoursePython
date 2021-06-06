## While loops can be used with lists and dictionaries and allows for modification while traversing them

## We can move items in one list to another using a while loop:

unconfirmed_users = ['eric', 'max', 'allinn']
confirmed_users = []

while unconfirmed_users:
    current = unconfirmed_users.pop()
    print("Verifying  unconfirmed user: " + current.title())
    confirmed_users.append(current)

print(confirmed_users)
print(unconfirmed_users)    ## should be empty now

## As you can see, the .pop() lets us remove elements from a list starting with the last item. As a result, the confirmed_users list
## is now the reverse of the original list and uncofirmed_users should be empty

## What do we do when we want to remove every instance of an element in a list?

shopping_list = ['milk', 'eggs', 'bacon', 'eggs', 'chips', 'water', 'eggs']

while 'eggs' in shopping_list:
    shopping_list.remove('eggs')

## The while loop checks whether or not 'eggs' is in the list, and if there is an instance, it removes it.
## Otherwise, the loop will stop when there are no more instances left

print(shopping_list) # should have no 'eggs' left

## We can also use input() to fill in a dictionary in conjunction with a flag and a while loop:

responses = {}

active = True   ## flag

while active:

    name = input('What is your name? ')
    place = input('Please input what your favorite place is: ')

    responses[name] = place
    
    rerun = input('Does anyone else want to take the poll? (Y/N) ')
    
    if rerun.lower() == 'n':
        active = False          ## set flag to false when no one else to take poll

## now that the poll is done, print results:

print("\n-- Poll Results -- ")

for name, place in responses.items():
    print(name.title() + "'s favorite place is " + place.title())


## Exercises

print()

request = ['pastrami', 'panini', 'ham and cheese', 'meatball sub']
finished = []

while request:
    done = request.pop()
    print("One " + done + " sandwich coming right up!")
    finished.append(done)

print(finished)

print()

sandwich_orders = ['pastrami', 'panini', 'ham and cheese', 'meatball sub']
sandwich_orders.append('pastrami')
sandwich_orders.append('velveeta')
sandwich_orders.append('pastrami')

print("The deli has run out of pastrami")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

print(sandwich_orders)

print()

polled = {}

pollingActive = True

while pollingActive:

    user = input("What's your name? ")
    food = input("What's your favorite food? ")

    polled[user] = food

    extra = input("Want to run the program again? (Y/N): ")
    if extra.lower() == 'n':
        print("Exiting program...")
        pollingActive = False
    
print("\n-- Poll Results -- ")

for user, food in polled.items():
    print(user.title() + "'s favorite food is " + food.title())
