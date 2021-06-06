## While the for loop should be used when we have an end in mind, the while loop allows us to create a loop that ends
## after a certain criterion is met:

count = 0

while count <= 5:
    print(count)
    count += 1

## We can give the user a way to end the program by setting up a while loop to check whether the input is a certain
## thing. For example, in this case, it can be "quit":

prompt = "Tell me something, and I'll repeat it right back to you: "
prompt += "\nWhat do you want repeated back? "
message = ''

#while message != 'quit':        ## This loop will continuously run and ask for user input until they type in "quit"
#    message = input(prompt)
#    if message != 'quit':
#        print(message)

## Using a flag allows us to make the conditions that stop the while loop more complex; rather than just have one condition
## that causes the loop to quit, we can now create a flag that can be triggered to stop the loop:

active = True   ## the flag

while active:
    
    message2 = input('Please put in what you want to be printed: ')
    
    if message2 == 'quit':
        active = False
    else:
        print(message2)

## After the while loop exits, this would where the game over statement is and potentially a prompt to play again

## Now it's easy for us to add more elif statements that trigger the end of the program
## We can also use a break statement to "break" out of a while loop
## Like the other while loops, put a "break" statement whne the condition is triggered

## The continue statement instead of breaking out of the entire loop, it ignores what's in the rest of the loop and goes
## back to the beginning:

num = 0
while num in range(0, 11):
    num += 1
    if num % 2 == 1:
        continue
    print(num)

## This code prints out all the even numbers from 1 to 10 inclusive

## Infinite loops occur when a while statement's condition variable doesn't change in the loop. The terminal continues without
## ending, so use CTRL + C to end terminal

## Exercises
print()

pizza = ''

while pizza != 'quit':
    pizza = input("What kind of topping do you want? ")
    if pizza != 'quit':
        print("Your topping, " + pizza + ", was added.")

movie = input("What is your age? ")
movie = int(movie)

if movie > 12:
    print("The price is $15")
elif movie >= 3 and movie <= 12:
    print("The movie is $10")
else:
    print("The movie is free")

