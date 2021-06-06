## Rather than individually index each element in a list, we can utilize a for loop:

numbers = ["1", '2', '3', '4']

for number in numbers:
    print("I'm on number " + number)

print("\n")

names = ['Eric', 'Max', 'Bryan', 'Allinn', 'Nate', 'Edwin']

for i in range(0, 3):
    print("Wow, " + names[i] + " that was a great trick!")
    print("The index is: " + str(i))
print("Thanks for coming to our dogshit magic show!")

## Because Python uses indentation to determine whether something is part of a loop, it's imperative to write neatly formatted code
## that is easy to read An indentation error can occur when we don't indent after creating a for loop.

## Furthermore, forgetting to indent additional lines in a for loop can result in a logic error, where the code will compile and run,
## but it won't do what you wanted to. In this case, a line that should run each iteration of the loop will only run once after the loop finishes.

## It's also possible to add unnecessary indentations, which cause an unexpected indentation error. 

print("\n")

for i in range(0, 1):
    print("The colon after the for loop tells the compiler to read the next line as part of the loop.")

## Exercises
print("\n")

pizzas = ['cheese', 'bacon', 'extra cheesy']

for pizza in pizzas:
    print("I really like " + pizza + " pizza!")
print("Pizza is delicious!")

print("")

pets = ['dog', 'cat', 'hamster']

for pet in pets:
    print("A " + pet + " would make a great pet!")
print("All of these animals would make great pets.")


