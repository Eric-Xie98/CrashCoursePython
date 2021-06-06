## Because classes can closely model real life situations, we need to be able to access and modify attributes
## directly or in specific ways

# Let's create a car class with the attributes of make, model, and year:

class Car():

    """A simple attempt to represent a car"""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    
    def getDescriptiveName(self):
        return str(self.year) + " " + self.make.title() + " " + self.model.title()

    def readOdometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it")
        if self.odometer_reading == 69:
            print("Nice.")
            
    def changeOdometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't turn back on an odometer!")

    def incrementOdometer(self, mileage):
        self.odometer_reading += mileage
    

newCar = Car('audi', 'a4', 2016)
print(newCar.getDescriptiveName())
newCar.readOdometer()

## Every attribute in a class needs an initial value whether an empty string or just 0. For this car class,
## we'll be adding an odometer reader set to a default value of 0

## We can modify the odometer_reading using the dot notation:

newCar.odometer_reading = 23
newCar.readOdometer()

## The method above modifies it directly, but it's more helpful to use a setter method to modify for you

newCar.changeOdometer(46)
newCar.readOdometer()

## An example of this is when we want to check logic before changing a value, a setter method saves having to write
## the logic check every time you want to change the odometer; in this example, we're checking whether
## the odometer is trying to be set lower (which can't be done).

newCar.changeOdometer(23)       ## Should return the statement that the odometer can't be turned backwards

## We can increment the odometer mileage rather than changing it entirely each time too.

newCar.incrementOdometer(23)
newCar.readOdometer()

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
    

restaurant = Restaurant('panda express', 'chinese')
restaurant.customersServed()
restaurant.changeServed(100)
restaurant.customersServed()

print()

print("Today we served 20 new customers.")
restaurant.incrementServed(20)
restaurant.customersServed()

class User():

    def __init__(self, name):
        self.name = name
        self.login_attempts = 0

    def incrementAttempts(self):
        self.login_attempts += 1
        if(self.login_attempts == 3):
            print("You are temporarily locked out for 5 minutes!")

    def resetAttempts(self):
        self.login_attempts = 0

user1 = User('eric')
print(user1.login_attempts)

## Fails to login 3 times:

for i in range(3):
    print(user1.login_attempts)
    user1.incrementAttempts()

user1.resetAttempts()
print(user1.login_attempts)

    
