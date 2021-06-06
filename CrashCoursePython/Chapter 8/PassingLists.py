## Passing lists to functions can be useful in making working with lists efficient. Furthermore, functions
## get direct access to the list that is passed to them:

def greetUsers(guests):
    
    for guest in guests:
        print("Hi, " + guest.title() + "!")
    
lst = ['eric', 'alina', 'max']
greetUsers(lst)

uncompleted = ['apple', 'windows', 'samsung', 'android']
completed = []

def showModels(uncompleted, completed):

    while uncompleted:                  ## Notice how I used a while loop, otherwise a for loop would only go to the 2nd element because pop changes the list size
        current = uncompleted.pop()
        print("Printing: " + current.title() + " model")
        completed.append(current)
    
def printModels(completed):

    print("Completed Models:")
    for model in completed:             ## Because the list size doesn't change here, I can use a for loop
        print(model.title())
    

showModels(uncompleted, completed)
printModels(completed)


## In the upper example, we modified a list after passing it through a function. We took the uncompleted models and
## popped them out one by one and appended them to the completed models list.

## When we don't want the function to alter the list argument passed to it, we can use list slices mentioned before to create a copy of that list
## Therefore, if we didn't want the original uncompleted list to be altered, we could write the function call like so:

uncompleted2 = ['apple', 'windows', 'samsung', 'android']
completed2 = []

showModels(uncompleted2[:], completed2)
print(uncompleted2)         ## uncompleted2 list remains unchanged because we used list slices in the call AKA sent a copy of it instead

## However, it's more efficient to pass the original list to the function rather than create a new one

## Exercises

print()

magicians = ['lee harvey oswald', 'houdini', 'your mom']

def showMagicians(magicians):

    for magician in magicians:
        print(magician.title())

def makeGreat(magicians):

    for i in range(len(magicians)):
        magicians[i] = "The Great " + magicians[i].title()

    return magicians


showMagicians(magicians)
makeGreat(magicians)
print(magicians)

magicians2 = ['lee harvey oswald', 'houdini', 'your mom']

changed = makeGreat(magicians2[:])
showMagicians(magicians2)
showMagicians(changed)
