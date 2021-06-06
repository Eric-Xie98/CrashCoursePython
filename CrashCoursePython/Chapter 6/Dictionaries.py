## Python dictionaries allow users to connect information and almost limitlessly store them; In this chapter, we'll be 
## accessing and modifying information we store inside dictionaries and nest them inside lists, vice versa, and in themselves

## Here's an example of a simple dictionary:

alien_0 = {'color': 'red', 'points': 15} ## This dictioanry uses squiggly brackets and has two different values stored in color and points

print("Alien_0 has a color of " + alien_0['color'])
print("Alien_0 also is worth " + str(alien_0['points']) + ' points') ## The dictionary stores alien_0's color and point value

## A dictionary in Python is somewhat similar to a Hashmap in Java with it relying on key - value pairs, a set of values associated with each other.
## When a key is provided, Python returns the value associated. Every key - pair is connected by a colon, different pairs are separated by commas,
## and you can have a limitless amount of key - pairs in a dictionary

## When we want to access information in a dictionary, we do something similar to what we did above:
## Give the name of the dictionary and place the name of the key in square brackets.

alien_1 = {'color': 'green', 'points': 5}
print(alien_1['color'])
print(alien_1['points'])

## Because dictionaries are dynamic structures, we can add key - value pairs anytime:
## We create new pairs similar to how we access them:

alien_0['x_value'] = 25
alien_0['y_value'] = 0

print(alien_0) ## Even though it doesn't occur in this example, the dictionary doesn't care about the order of the pairs, only what's stored

## A dictionary can be initalized without having any key - value pairs inside, usually for later use

alien_3 = {}
alien_3['color'] = 'yellow'
alien_3['points'] = 10
print(alien_3)

## We can modify elements in a dictionary by using its key and modifying the value:

alien_3['color'] = 'pink'
alien_3['points'] = '35'
print(alien_3) ## Alien_3 now has a new color pink and point value 35

## Here's a more interesting example:

alien_5 = {'color': 'black', 'points': 44, 'x_position': 20, 'speed': 'fast'}

print('The original position of alien_5 is ' + str(alien_5['x_position']))
x_increment = 0

if alien_5['speed'] == 'slow':
    x_increment = 1
elif alien_5['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

alien_5['x_position'] += x_increment

print('Because the alien is traveling ' + alien_5['speed'] + ", the x-position of the alien is now " + str(alien_5['x_position']))







