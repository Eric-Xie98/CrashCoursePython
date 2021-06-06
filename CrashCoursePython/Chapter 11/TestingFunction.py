## When we write code, it's imperative that we also know how to create tests for it and ensure
## that our code is correct. Using unit tests, we'll be able to catch errors before we even let
## users use the program.

## We'll learn how to use the unittest module in Python to check if our inputs match the outputs
## we want and learn how to read pass or fails.

# Let's start off with a simple get_formatted_name function to test:

def get_formatted_name(first, last, middle = ''):
    if middle:
        return first.title() + " " + middle.title() + " " + last.title()
    return first.title() + " " + last.title()

# From our short code in nametesting.py, we can see that our function using the inputs work.
# If we wanted to modify it to handle middle names, but we wanted to ensure
# that it still correctly handled first and last, we could do the nametesting.py each time,
# but that would be tedious.

# So let's do some unit testing and test cases:
# A unit test verifies a certain aspect of your function is working correctly and a test case
# is a group of unit tests that ensure your entire function works.

# When we make test cases, we want to make ones that are full coverage, they cover all possible
# inputs a function could receive and makes sure there are tests that cover them

# When we make large programs, this can become daunting, so it's better to write the barebones tests
# and then expand to full when more people start to use the program.

""" self.assertEqual(function tested result, expected result) """

# One of the most useful unittest's features check whether the thing returned by the function matches the second parameter.
# Because we know that our function is supposed to return 'Janis Joplin', we compare the function's return to it.

# If the assertion is false, the test will indicate that the function doesn't work correctly.

# Also make sure that the testing function name starts with test_ by convention and for it to be automatically run when testcase is ran

## Exercises

print()

def cityCountry(city_name, country_name, population = ''):
    if population:
        return city_name.title() + ", " + country_name.title() + " - Population: " + str(population)
    return city_name.title() + ", " + country_name.title()