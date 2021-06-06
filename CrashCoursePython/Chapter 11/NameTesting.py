## Testing for the get_formatted_name function using unittests module:

# To check that this function works, we made a program that uses this function:

from TestingFunction import get_formatted_name

""" while True:

    print("Type 'q' to end the program.")
    first = input("Type in your first name: ")
    if first == 'q':
        break
    last = input("Type in your last name: ")
    if last == 'q':
        break

    print(get_formatted_name(first, last))

print("Program ending...") """

# Here's the syntax for using unittest:

import unittest     # We first import unit test and create a class with unittest.TestCase

class getNameTesting(unittest.TestCase):

    """Tests for 'TestingFunction.py' get_formatted_name"""

    def test_first_last(self):                                                        # Made a mistake, MUST start with test to be run automatically by testcase
        """Do normal first and last names work? (e: Janis Joplin)"""
        self.assertEqual(get_formatted_name('janis', 'joplin'), 'Janis Joplin')     # The assert method is used, more info below

    def test_first_middle_last(self):
        """Do normal first, middle, and last names work? (ex: Wolfgang Amadeus Mozart)"""
        self.assertEqual(get_formatted_name('wolfgang', 'mozart', 'amadeus'), 'Wolfgang Amadeus Mozart')

        

## unittest.main()             # Tells Python to run all tests in this file


# One of the most useful unittest's features check whether the thing returned by the function matches the second parameter.
# Because we know that our function is supposed to return 'Janis Joplin', we compare the function's return to it.

# If the assertion is false, the test will indicate that the function doesn't work correctly.

# So what happens when we have a failed test? We'll be changing our function and then changing it back (adding a middle parameter).
# After we run unittest, we get FAILED (errors=1) for tests and the traceback shows that the function is missing a positional argument.

# Let's break down the error shown below:

""" E
======================================================================
ERROR: test_first_last (__main__.getNameTesting)
Do normal first and last names work? (e: Janis Joplin)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/ericx/Downloads/ThinkPython/CrashCoursePython/Chapter 11/NameTesting.py", line 31, in test_first_last
    self.assertEqual(get_formatted_name('janis', 'joplin'), 'Janis Joplin')     # The assert method is used, more info below
TypeError: get_formatted_name() missing 1 required positional argument: 'last'

----------------------------------------------------------------------
Ran 1 test in 0.000s

FAILED (errors=1) """

# The E immediately indicates a test failure and then a more specific traceback shows where. The bottom section gives a summary of the tests ran and etc.
# See how the comments show up in the testing function to describe what it's testing? Very helpful.

# Now we fix the middle parameter value by making it a default to "" and etc., but most importantly, Janis Joplin should now still work.
# Running the code once more, we get no errors. Success!

# Now that we got that working again, let's add a test for first, middle, and last! It works too! Awesome!


## Exercises

from TestingFunction import cityCountry

class getCityCountryTesting(unittest.TestCase):
    """Testing getCityCountry function"""

    def test_city_country(self):
        """Tests the City, Country format (ex: Rio de Janiero, Brazil)"""
        self.assertEqual(cityCountry('beijing', 'china'), "Beijing, China")

    def test_city_country_pop(self):
        """Tests the City, Country, and Population format (ex: Rio de Janiero, Brazil - Population: 500000)"""
        self.assertEqual(cityCountry('beijing', 'china', 5000000), "Beijing, China - Population: 5000000")

unittest.main()