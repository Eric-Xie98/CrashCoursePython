## Python uses special objects called exceptions that manage errors that arise during a program's runtime.
## When these exception objects aren't handled by the code, the program stops and shows a traceback where the 
## exception occured. Otherwise, the program continues running.

## We can handle execeptions with try-except blocks that tell Python to do something when an exception is raised.
## So for users, rather than see a complex traceback call, they could be shown an user friendly error message.

# Let's try working with try-except blocks with the divide by zero exception (ZeroDivisionError):

# print(5/0)      # This line here results in a traceback of ZDE

# When you think something will raise an exception, a try-except block comes in handy.

try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")

# If the code in the try block works, Python skips over it and finds a corresponding except block and runs its code.
# The code inside is ran instead of a traceback being shown.

## Handling errors is especially important when we want the program to keep running even after an error happens.      
## This can especially happen in user input programs, where if the user inputs something incorrectly, a traceback would return.
## By handling errors correctly, we can allow users to retry and keep it nontechnical and prevent hackers from gaining info.

print("Give me two numbers. I'll divide them.")
print('Enter q to quit.')

while True:
    num1 = input("Enter the first number: ")
    if num1 == 'q':
        break
    else:
        num1 = int(num1)
    num2 = input("Enter the second number: ")
    if num2 == 'q':
        break
    else:
        num2 = int(num2)

    try:
        answer = num1 / num2        ## Note how it doesn't try to print it initally but tests if the variable can store it
    except ZeroDivisionError:
        print("You can't divide by zero. Please try again.")
    except ValueError:
        print("Let the program run wtf")
    else:
        print(answer)               ## Then after it'll print if none of the except statements run through

# An example of the try except block catching if the second number is 0. Honestly, you could just write an if statement to check whether the
# second number is a 0 or not.

## We can also add an else block the the try-except statement above to make it more error resistant, the last case scenario if none of the
## other excepts are ticked off.
    
# By anticipating these errors, we can write robust programs that can handle innocent users' mistakes as well as malcious hackers' attempts to get in.

# Another error that's common is the FileNotFoundError exception, which can be easily handled by the try-except block mentioned above:

filename = 'alice.txt'

try:                                            ## we add a try-except statement to try and see if we can open this file
    with open(filename) as file_object:         ## 'alice.txt' doesn't exist resulting in a traceback 
        contents = file_object.read()
except FileNotFoundError:
    print("This file doesn't exist.")
else:
    print(contents)

# The code checks whether the try statement works, which it doesn't, and matches up the error the except FileNotFoundError to print the error message.

rightFileName = 'pi_digits.txt'

try:
    with open(rightFileName) as file_object:
        contents = file_object.read()
except FileNotFoundError:
    print("This file couldn't be found.")
else:
    print(contents)


print()

# Quick test of an input program that handles traceback exception of file not being found:

while True:

    print("Enter 'quit' whenever you want to exit the program.")
    fileName = input("Please input a file name you want the contents to be printed: ")

    if fileName == 'quit':
        break

    try:
        with open(fileName) as file_object:
            contents = file_object.read()
    except FileNotFoundError:
        print("We couldn't find the file (" + fileName + ") you wanted.")
        print("Please try again.")
    else:
        print(contents)
        print()

        words = contents.split()
        wordCount = len(words)
        print("This file has a total of " + str(wordCount) + " words.")
    
print("Program ending...")

## When we end up using this to work with multiple files (and want to be able to print each's contents and number length),
## it's far better to turn the middle portion of the code above into a function called countWords() to be called for later use

def countWords(fileName):
    try:
        with open(fileName) as file_object:
            contents = file_object.read()
    except FileNotFoundError:
        print("We couldn't find the file (" + fileName + ") you wanted.")
    else:
        words = contents.split()
        wordCount = len(words)
        print("This file has a total of " + str(wordCount) + " words.")

files = ['guest.txt', 'learning_python.txt', 'valorant.txt', 'alice.txt', 'pi_digits.txt']
for file in files:
    countWords(file)

## The missing 'alice.txt' file has no effect on the rest of the program, and it continues running.

# If we want the program to pass any errors with any error message or warning, we can use the 'pass' keyword
# to signal for Python to do nothing and just keep schmoving.

# It can also act as a placeholder for you to know that you'll be adding code there later.

# It's up to you to on how to handle errors and how you'll present them to users. A good program is able to handle
# all different kinds of inputs and ensure that the experience is smooth.

## Exercises

print()

while True:

    print("We're gonna add two numbers together for you, you troglodyte.:")
    first = input("Enter the first number: ")
    second = input("Enter the second number: ")

    if first == 'quit' or second == 'quit':
        break

    try:
        first = int(first)
        second = int(second)
    except ValueError:
        print("Please enter a number, not text you retard.")
    else:
        print(first + second)


print()

firstFile = 'dogs.txt'
secondFile = 'cats.txt'

with open(firstFile, 'w') as file_obj:
    file_obj.write("spots\nrover\nmaxwell")

with open(secondFile, 'w') as file_obj:
    file_obj.write("mochi\nmittens\nlily")


def readFile(filename):
    try:
        with open(filename) as file_obj:
            contents = file_obj.read()
    except FileNotFoundError:
        print("We couldn't find this file: " + filename) 
    else:
        print(contents)


lst = ['dogs.txt', 'alice.txt', 'cats.txt']

for text in lst:
    readFile(text)

## We can use .count() to find the number of appearances of the argument in a string:

line = "Row, row, row your boat, gently down the stream. Merrily, merrily, merrily, merrily, life is like a dream."
print(line.count('row'))

# if we wanted to find ALL the instances, we would first .lower() everything in the line:

print(line.lower().count('row'))


