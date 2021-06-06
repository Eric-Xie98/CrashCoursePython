## Because we take a lot input data from users, it's usual that we want to save what they input for things
## such as settings for later use. A simple way to do this is to use a json module:

## We dump simple Python data structures into a file and upload it whenever the program is run. We can use this JSON module
## to share this data between different program, programmers, and coding languages!

# JSON (JavaScript Object Notation) was originally developed for JavaScript but since then has become the main format for many languages.

# We're going to write a short program that takes a list of numbers and saves it then reloads them back in.

# The first program will use json.dump() to store the information and the second will instead use json.load() to retrieve it:

import json

numbers = [2, 3, 5, 17, 24, 33]

filename = 'numbers.json'       ## Notice how we're storing the file in a JSON format

with open(filename, 'w') as file_object:
    json.dump(numbers, file_object)     ## Using the json.dump() function to store the numbers list inside the numbers.json file

## Refer to numbersReading.py to see about json.load()

# Through this method, we can implement user input and store any data for later usage:

username = input("What do you want your username to be? ")

with open('username.json', 'w') as file_obj:
    json.dump(username, file_obj)
print("We'll remember you by your username, " + username + "!")

# Once we've stored the username in a json, we can pull it once he comes back.

with open('username.json') as file_obj:
    retrieval = json.load(file_obj)

print("Welcome back, " + retrieval + "!")

## The code below summarizes what we're doing:

def retrieveUsername():
    """Get username if its already stored"""
    filename = 'username2.json'
    try:
        
        with open(filename) as file_object:
            name = json.load(file_object)
    
    except FileNotFoundError:

        return None

    else:
        
        return name

def getNewUsername():

    user = input("What would you like your username to be? ")
    fileName = 'username2.json'
    
    with open(fileName, 'w') as file_object:
        json.dump(user, file_object)

    return user    

def rememberMe():

    username = retrieveUsername()

    if username:
        
        answer = input("Are you " + username + "? (Y / N): ")

        if answer == 'N':
            username = getNewUsername()

        print("Welcome back, " + username + "!")
    
    else:
        
        print("We don't seem to have you in our database yet...")
        username = getNewUsername()
        print("We'll remember you next time, " + username + "!")


rememberMe()

## What we essentially did here is refactor the code, or turn code that would be needed to use multiple times and repetitive into a function
## for later use. Furthermore, we can break down rememberMe() into smaller functions or refactor it. 

# Let's try refactoring rememberMe() and make a function that retrievesStoredUsernames:

## This can used to repalce the upper part of the rememberMe():

# Let's refactor getting a new username to for the hell of it:

## Now, our rememberMe() code has simplified into an if-else statement is much more clearer and easier to read!

## Exercises

print()

fave = input("Tell me your favorite number: ")
fave = int(fave)

with open('favorite.json', 'w') as file_object:
    json.dump(fave, file_object)

