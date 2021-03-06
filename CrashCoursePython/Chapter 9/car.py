class Car():

    """ A simple attempt to represent a car """

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        """ Set the odometer reading to the given value. 
        Reject the change if it attempts to roll the odometer back."""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles

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