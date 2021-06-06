# Basic math operations in Python

print(3 + 1)
print(3 - 1)
print(3 * 1)
print(3 / 2)

# Use two ** to denote power expressions

print(3 ** 3)

# A float is a any number with a decimal; for the most part, decimals behave normally, but sometimes can become wonky

print(0.2 + 0.1)
print(0.2 + 0.2)

# Use the wrapper str() to convert ints to strings

age = 23
## the line print("Happy " + age + "rd birthday!") will return with an error because of the fact that the variable age is an int
## however, if we use the str() wrapper, we can convert age into a string temporarily

print("Happy " + str(age) + "rd birthday!")
print(type(age))    # the variable age remains an int

# Exercises

print(type(1 + 2 + 3 + 2))  # the results for both addition and subtraction stayed an integer
print(200 - 100 - 92)
print(200 * (1 / 25))   # however, the multiplication / division results became a float
print(200 / 25) 

print(type(200 / 8))
print(type(1.0 + 2))    # the "higher" class or whatever becomes the end result

favoriteNum = 98
print("My favorite number is " + str(favoriteNum) + " because it's a well-rounded integer")
favoriteNumStr = "98"
print("my fave num is " + favoriteNumStr)

import this
