## In Python, square brackets [] indicate a list, and individual items are separated by commas

bicycles = ["wheels", "handle", "seat", "spokes"]
print(bicycles)

# Access individual elements in a list using index, keep in mind that the index starts at 0 for lists

print(bicycles[1])
print(bicycles[1].title())

## Change elements using the index and add elements using .append()

bicycles[0] = "ducati"
bicycles.append("joe mama")
print(bicycles)

## Insert elements into a list using the insert(index, element) method

bicycles.insert(0, "the new first element")
bicycles.insert(1, "the new second element")
print(bicycles)

## Removing elements can be done using the del statement

del bicycles[0]
del bicycles[0]
print(bicycles)

## the del statement is a void method, meaning it doesn't return a value. on the other hand, the pop() method removes the top element from the list
## and returns whatever value it has (this is the last element)
## this is analogous to the Java stack where pop takes the top element off the stack

ret = bicycles.pop()
print(ret)
print(bicycles)

## How do we pop an element at a specified index then? Put the index inside the pop() method.

balls = ["red", "blue", "yellow", "green"]
print(balls.pop(0))
print("As you can see, the balls list's first element has been popped: " + str(balls))

## The previous remove methods involved knowing the positions of the element and their indexes. So what if you only have the element itself and want to remove it?
## Let's say we want to remove "yellow" in balls but don't know the index; .remove() will only remove the first occurance of it in the list!

balls.remove("yellow")
print(balls)

repeat = ["repeated", "repeated"]
repeat.remove("repeated")
print(repeat)


## Exercises

guestList = ["Abraham Lincoln", "Theodore Roosevelt", "Dwight D. Eisenhower"]

for person in guestList:

    print("Hey " + person + ", wanna come over for dinner? Mom's making spaghetti.")

print("\n\n")

print("Oh no! Abraham Lincoln was brutally assassinated in a theater, so he can't make it!")
guestList[0] = "Mao Ze Dong"
print("The guest list has been updated: " + str(guestList))

print("\n\n")

print("Let's go, we found an even bigger dinner table!")
guestList.insert(0, "Pol Pot")
guestList.insert(int(len(guestList)/2), "Joseph Stalin")
guestList.append("Fidel Castro")

for guest in guestList:
    print("Hey " + guest + ", want to come over for spaghetti and meatballs?")

print("\n\n")

print("Yo, the table isn't coming in time, I can only let 2 people come")
print("\"That's fucked up\" - Mao Ze Dong")

for i in range(int(len(guestList) - 2)):
    print("Hey " + guestList.pop() + ", you're uninvited. Sucks to suck.")

for guest in guestList:
    print("You're still invited fatass: " + guest)

del guestList[:]
print(guestList)



