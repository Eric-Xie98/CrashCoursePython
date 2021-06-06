class User():

    def __init__(self, name):
        self.name = name
        self.login_attempts = 0
        self.priv = Privilege('user')

    def incrementAttempts(self):
        self.login_attempts += 1
        if(self.login_attempts == 3):
            print("You are temporarily locked out for 5 minutes!")

    def resetAttempts(self):
        self.login_attempts = 0

class Privilege():

    def __init__(self, userType):
        if userType == 'admin':
            self.privileges = ['can mute user', 'can delete others post', 'can ban user', 'can pin post', 'can create own post', 'can delete own post', 'can comment']
        else:
            self.privileges = ['can create own post', 'can delete own post', 'can comment']
    
    def showPrivileges(self):
        print("This is your privileges:")
        for privilege in self.privileges:
            print(privilege)
        


class Admin(User):

    """ Simple admin class with special privileges that extends User"""

    def __init__(self, name):
        super().__init__(name)
        self.priv = Privilege('admin')
    

twitchMod = Admin('eric xie')
twitchMod.priv.showPrivileges()

print()

twitchUser = User('max khan')
twitchUser.priv.showPrivileges()

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

    def upgradeBattery(self):
        if self.battery_size != 85:
            self.battery_size = 85

class ElectricCar(Car):         ## shows inheritance of Car class

    def __init__(self, make, model, year):
        super().__init__(make, model, year)         ## Tells Python to call __init__ from the parent class of ElectricCar
        self.battery = Battery()

    def fill_gas_tank(self):
        print("This car doesn't have a gas tank!")


my_tesla = ElectricCar('tesla', 'model s', 2016)
my_tesla.battery.battery_charge = 75
print("Before:" )
my_tesla.battery.getRange()
print("After:")
my_tesla.battery.upgradeBattery()
my_tesla.battery.getRange()
