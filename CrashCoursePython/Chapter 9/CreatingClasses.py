## Object-Oriented Programming (OOP) allows us to write classes that represent real world things
## and instantiate objects out of them that follow their behavior. When we write a class, we establish the general
## behavior of a category of objects.

## Making an object is called instantiation and you work with instances of a class. We'll furthermore be able to
## extend functionality of preexisting classes and make them easy for other programmers to use.

# We'll start by writing a simple class Dog() with 2 pieces of info (age and name) as well as
# 2 behaviors (sit and roll over):

class Dog():        ## This is the creation of Dog() class, capitalized by convention for classes

    """ A simple attempt to model a Dog """

    def __init__(self, name, age):
        """Initialize name and age attributes"""
        self.name = name            ## Both of these are attributes that take parameter and store in variable
        self.age = age

    def sit(self):
        """Simulate sitting because of a command"""
        print(self.name.title() + " is now sitting.")

    def rollOver(self):
        """Simulate rolling over because of a command"""
        print(self.name.title() + " rolled over.")
    

## A function that's part of a class is called a method. The __init__ method is a special method that Python
## runs automatically when we create a new instance of Dog(). It has 2 underscores before and after.

## This method automatically passes self with the argument, so we only need to provide the name and age arguments. The self
## argument allows for references to the instance itself.

## Right now, the two behavioral methods only print out statements, but they later can be written to do something realistic
## such as linked to an animation, etc.


# Think of a class as a set of instructions to make an instance. A cookie cutter of sorts. The Dog() class
# is a set of instructions that tells Python how to make individual instances represent specific dogs.

my_dog = Dog('willie', 6)        ## Python creates a Dog object/instance with a name 'willie' and age of 6 and stores it in my_dog variable

print("My dog, " + my_dog.name.title() + ", is " + str(my_dog.age) + " this year.")     ## Accessing attributes with the dot notation

## We call methods also using dot notation to call any method inside the object's class:

my_dog.sit()
my_dog.rollOver()

## We can create as many instances of a class as we need:

your_dog = Dog('lucy', 12)

print("Your dog, " + your_dog.name.title() + ", is " + str(your_dog.age) + " this year.")

your_dog.sit()


## Exercises 

print()

class Restaurant():

    """A class for a simple restaurant with name and cuisine type"""

    def __init__(self, name, cuisine):
        self.name = name
        self.cuisine = cuisine
    
    def describeRestaurant(self):
        print("This restaurant is named " + self.name.title() + " and is " + self.cuisine.title() + " styled cuisine.")

    def openRestaurant(self):
        print("The restaurant is now open.")


my_restaurant = Restaurant('panda express', 'chinese')
my_restaurant.describeRestaurant()
my_restaurant.openRestaurant()

rest1 = Restaurant('five guys and fries', 'american')
rest2 = Restaurant('taco mac', 'mexican')
rest3 = Restaurant('ginger and soy', 'asian')

print()

rest1.describeRestaurant()
rest2.describeRestaurant()
rest3.describeRestaurant()

print()

class User():

    """Class for a simple user's first and last name and some other attributes"""

    def __init__(self, first, last, age, gender):
        self.first = first
        self.last = last
        self.age = age
        self.gender = gender

    def describeUser(self):
        print("\tSummary:")
        print("Name: " + self.first.title() + " " + self.last.title())
        print("Info: " + str(self.age) + " year old " + self.gender)
    
    def greetUser(self):
        print("Welcome, " + self.first.title())


user1 = User('mark', 'swanson', 17, 'male')
user2 = User('alina', 'zhang', 17, 'female')
user3 = User('allinn', 'chen', 19, 'male')

user1.greetUser()
user2.describeUser()
user3.describeUser()


