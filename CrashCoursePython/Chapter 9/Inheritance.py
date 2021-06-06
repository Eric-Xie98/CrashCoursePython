## Rather than rewriting a class from scratch, if the class is similar or a specialized version of another class, you can use inheritance
## to take on all the attributes and methods of the first class. The original class is known as the parent class
## while the class that inherits it is the child class. The child class is free to define its own methods and attributes.

## When Python is creating an instance or object of the child class, it needs to assign all values to attributes in the parent
## class. To do this, the __init__ method needs help from the parent class:

# Let's make an electric car class, similar to the car class we did previously.

class Car():

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        self.gas_tank = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles

    def fill_gas_tank(self, gallons):
        self.gas_tank += gallons


class Battery():

    """ A simple attempt to represent an electric car's battery """

    def __init__(self, battery_charge = 100, battery_size = 70):
        self.battery_charge = battery_charge
        self.battery_size = battery_size

    def checkBattery(self):
        print("The battery is currently " + str(self.battery_charge) + "%" + " charged.")

    def describeBattery(self):
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

    def getRange(self):
        miles = 0
        range = self.battery_charge * self.battery_size
        if range >= 6000:
            miles = 240
        elif range < 6000:
            miles = 200
        
        print("This car can go " + str(miles) + " more miles.")

class ElectricCar(Car):         ## shows inheritance of Car class

    def __init__(self, make, model, year):
        super().__init__(make, model, year)         ## Tells Python to call __init__ from the parent class of ElectricCar
        self.battery = Battery()

    def fill_gas_tank(self):
        print("This car doesn't have a gas tank!")

electric = ElectricCar('tesla', 'model s', 2016)
print(electric.get_descriptive_name())              ## The electric car object can uses methods/functions from the parent class


## When you create a child class, the parent class must be in the same file and before the child class

# We can add attributes to the child class now that separate it from the parent class

electric.battery.checkBattery()
electric.battery.describeBattery()

## You can override methods from the parent class by using the same name as the method in the parent class. Python 
## prioritizes the subclass/child class' method over the one in the parent.

car = Car('volvo', 's4', 2013)
car.fill_gas_tank(10)
electric.fill_gas_tank()

## YOu might notice that your attributes and methods start quickly becoming lengthy when modeling real life situations,
## so you can split up large classes into smaller classes 

# let's make a Battery() class for ElectricCar

## With the new Battery() class that doesn't inherit from anything, the initalization sets default values for the size and charge
## In ElectricCar() class, we create a new instance of Battery and store it in self.battery, and since it's in the __init__,
## everytime we create an electric car, a battery instance will be created automatically with it

my_tesla = ElectricCar('tesla', 'model v', 2020)
my_tesla.battery.checkBattery()
my_tesla.battery.battery_charge = 40
my_tesla.battery.checkBattery()

print()

my_tesla.battery.getRange()
my_tesla.battery.battery_charge = 100
my_tesla.battery.getRange()

## As we begin to model more complicated properties, we begin to question whether getRange() should be a part of the battery
## or a part of the ElectricCar class. Depending on the situation, it may be better to put it in the ElectricCar class when
## dealing with an entire line of cars

## Don't be afraid to tear up your classes in search of the most efficient method!

## Exercises

print()

class Restaurant():

    def __init__(self, name, cuisine):
        self.name = name
        self.cuisine = cuisine
        self.served = 0

    def customersServed(self):
        print(self.name.title() + " has served " + str(self.served) + " customers.")
    
    def changeServed(self, served):
        self.served = served

    def incrementServed(self, servedNum):
        self.served += servedNum


class IceCreamStand(Restaurant):

    """ Simple class of ice cream flavors that inherits from Restaurant"""

    def __init__(self, name, cuisine, *flavors):
        super().__init__(name, cuisine)
        self.flavors = flavors

    def displayFlavors(self):
        
        print("\tFlavors: ")
        
        for flavor in self.flavors:
            print(flavor.title())
    


iceCreamStand1 = IceCreamStand('ben and jerrys', 'desert', 'vanilla', 'chocolate', 'fudge', 'rocky road', 'sherbert')
iceCreamStand1.displayFlavors()

print()

class User():

    privileges = ['can create own post', 'can delete own post', 'can comment']

    def __init__(self, name):
        self.name = name
        self.login_attempts = 0

    def incrementAttempts(self):
        self.login_attempts += 1
        if(self.login_attempts == 3):
            print("You are temporarily locked out for 5 minutes!")

    def resetAttempts(self):
        self.login_attempts = 0

    def showPrivileges(self):
        print("These are " + self.name.title() + "'s privileges (user):")
        for item in self.privileges:
            print(item)


class Admin(User):

    """ Simple admin class with special privileges that extends User"""

    def __init__(self, name):
        super().__init__(name)
        self.adminPriv = ['can mute user', 'can delete others post', 'can ban user', 'can pin post']
    
    def showPrivileges(self):
        print("These are " + self.name.title() + "'s privileges (admin):")
        for item in self.adminPriv:
            print(item)
        for item in super().privileges:
            print(item)



twitchMod = Admin('eric xie')
twitchMod.showPrivileges()

twitchUser = User('max khan')
twitchUser.showPrivileges()

