## Functions are blocks of code that can used to simplify the main code. Rather than repeatedly compute a value or 
## do a certain task, we can create a function that can be called and arguments can be passed to it.

## We create functions starting with the def() and the name of your function:

""" Prints out a simple greeting to user"""
def greet_user():
    print("Hello!")

greet_user()        ## The function definition parameters are empty, meaning it doesn't require any arguments to run

def greet_user2(username):
    print('Hi, my name is ' + username.title() + ", great to meet you")

greet_user2('eric')

## As you can see, in greet_user2 function, we passed an argument ('eric') to the parameter 'username' in the function definition.
## When we call a function, we place the value we want it to work with in the parentheses.

## Exercises

print()

def display_message():
    print('We learned about creating functions and giving them parameters and arguments.')

display_message()

def favorite_book(book):
    print("My favorite book is " + book.title())

favorite_book('alice in wonderland.')
