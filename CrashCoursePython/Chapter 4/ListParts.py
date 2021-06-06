## Rather than work with entire lists, we can use list slices to work with specified parts of lists.
## A list slice can be used with [start index : end index non inclusive]

colors = ['red', 'blue', 'green', 'yellow', 'white']
print(colors[0:len(colors)]) ## You can print the whole list by using the last index as the length of the list
print(colors[2:4])

## If you omit a space in the slice (ex: colors[1:]) then it will include everything in the list after or before

print(colors[1:])
print(colors[:3])

## Using negative integers in the start index takes the x element counuting from the end of the list and returns it to the end - 1 index
## The reverse is true when we put the negative integer in the end index space, it starts from the front of the loop

print('')
print(colors[-3:]) ## This should print out the 3rd to last index to the end
print(colors[:-3]) ## This should print out the first 2 values

## Similar to before, we can loop through a slice of a list rather than the whole thing

numbers = list(range(1, 10))
numString = ""

for number in numbers[0:4]:
    numString += str(number) + " "

print(numString)

## Copying lists with Python can be done in different ways but have different effects
## For example, if we copy lists over using slices:

myFoods = ['pizza', 'ice cream', 'chocolate chip cookie']
hisFoods = myFoods[:] ## this method creates an entirely new list copy

## If I were instead to use hisFoods = myFoods without the slices, this tells Python to point the object variable hisFoods to the where the list of myFoods is stored
## Therefore, any changes I make to hisFoods or myFoods will show up in both

hisFoods.append("pussy")
print(str(myFoods) + " " + str(hisFoods))

## Exercises
print("")

## This exercise will use the numbers list created above

middle = int(len(numbers)/2)
print("The first 3 items of the list are: " + str(numbers[0:3]))
print("The middle 3 items of the list are: " + str(numbers[middle - 1: middle + 2]))
print("The last 3 items of the list are: " + str(numbers[-3:]))

print("")

pizzas = ['cheese', 'pepperoni', 'extra cheese', 'bacon']
friends_pizza = pizzas[:]
pizzas.append('dog pizza')
friends_pizza.append('cat pizza')
print("My favorite pizzas are:")
for pizza in pizzas:
    print(pizza)
print("")

print("My friend's favorite pizzas are: ")
for pizza in friends_pizza:
    print(pizza)


## Extra Practice from online

print("")

integers = list(range(1, 101))
tens = [num for num in integers if num % 10 == 0]
sixs = [num for num in integers if num % 2 == 0 if num % 3 == 0]
print(tens)
print(sixs)

print("")

small = list(range(1, 11))
evenOdd = ["Even" if num % 2 == 0 else "Odd" for num in small]
print(evenOdd)
