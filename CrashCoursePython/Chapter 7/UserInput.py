## In order to solve many users' problems, we need to take input from them and transform it into something with our code.
## We can prompt the user for their input by using the input() function, and in conjunction with while loops, we can give users
## the ability to decide when they want the program to end

## The input() function takes one argument, the message that should be displayed, and waits for the user to press ENTER:

message = input("Type what you want to see printed: ")
print(message)

## When you write input programs, make sure to be clear on what should be inputted with the displayed message.

name = input("Please print your full name: ")
print(name)

## You can simplify code by storing the prompt into a variable rather than directly typing it into the input argument:

prompt = "For us to understand you better, please follow the instructions below: "
prompt += "\nHi, please enter your name!"

## If we want an integer to be inputted, use int() rather than input() as input() converts the input into a string
## Now, we don't have to convert the input into an integer when we get it from the user:

print("Check if you're legally allowed to drink: ")
age = input("What is your age? ")
age = int(age)

if age >= 21:
    print("You're allowed to purchase and consume alcohol")
else:
    print("You are not legally allowed to purchase and consume alcohol")


## The MOD operator (%) works by getting the remainder after dividing both the numbers:

print(5 % 2)
print(10 % 2)

## This operator is very useful for determining whether a number is odd (x % y == 1) or even (x % y == 0)

## Exercises

carPrompt = "What kind of car would you like? "
car = input(carPrompt)

print("I'll see if I can find a " + car + " for you.")

num = input("How many people are in your dinner group? ")
num = int(num)

if num >= 8:
    print("You're gonna have to wait awhile")
else:
    print("Your table is ready.")

num10 = input("Input a number and we'll tell you if it's a multiple of 10 or not: ")
num10 = int(num10)

if num10 % 10 == 0:
    print("This number is a multiple of 10")
else:
    print("This number is not a multiple of 10")

