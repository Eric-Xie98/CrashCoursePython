## So, what is a tuple? A tuple is an immutable list, meaning that it's a list where its items cannot be changed.

## A tuple looks just like a list except you use parenthesis instead of square brackets; once the list is created, we can access
## the elements in the list like we would normally

dimensions = (200, 50)
print(dimensions[0])

## Trying to change the value of an item in a tuple will result in an item type error, saying you can't do item assignment on a tuple
## Just like lists, you can iterate through a tuple using a for loop:

integers = tuple(range(1, 4))
for integer in integers:
    print(integer)

## Even though we can't change individual elements, we can rewrite a tuple by reassigning the variable to a new one:

dimensions = (400, 100)
print(dimensions[0]) ## Now the dimensions of the tuple are changed but we had to create a new tuple

## Tuple Exercises

print("")

menu = ("cheesecake", "spaghetti", "ramen", "fried rice", "fried noodles")
for food in menu:
    print(food)

## menu[0] = "pussy" demonstrates that it's a tuple - item assignment error

print("")

menu = ("chocolate cake", "meatballs", "ramen", "fried rice", "fried noodles")
for food in menu:
    print(food)


