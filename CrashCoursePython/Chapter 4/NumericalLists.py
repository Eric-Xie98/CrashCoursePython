## Numerical lists allow you to more precisely move through elements in a list and keep track of their positions:

## One function tha comes in handy is the range() function, which can generate a series of number from the start index to to the end index (not inclusive)

for i in range(1, 4):
    print(i)

print("This should print the numbers from 1 to 3")

## Create lists using the range method as shown below using the list() function

lst = list(range(1, 4))
print(lst)

## We can even make the range() function skip numbers:

lst2 = list(range(0, 11, 2))
print(lst2)

skip3 = list(range(0, 11, 3))
print(skip3)

squares = []
for i in range(0, 11):
    squares.append(i**2)
print(squares)

## Python lists also come with a few functions that allow for easier developments such as min(), max(), and sum():

integers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print("Max integer in list: " + str(max(integers)))
print("Min integer in list: " + str(min(integers)))
print("Sum of the integers in list: " + str(sum(integers)))

## List Comphrehension can be used to shorten lines into a singular, compact line of code
## Using our squares list from previous as an example:

squares2 = [values ** 2 for values in range(0, 11)]
print(squares2)


## Exercises
print("")

## for i in range(1, 21):
    ## print(i)

bigList = list(range(1, 1000001))
## print(bigList)

print("Max: " + str(max(bigList)))
print("Min: " + str(min(bigList)))
print("Sum: " + str(sum(bigList)))

print("")

for i in range(1, 21, 2):
    print(i)


print("")

for i in range(3, 31, 3):
    print(i)


print('')

## cubes = []
## for i in range (1, 11):
##    cubes.append(i**3)
## print(cubes)

cubes = [i ** 3 for i in range(1, 11)]
print(cubes)

