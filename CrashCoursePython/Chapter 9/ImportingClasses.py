## To keep your code uncluttered, Python lets you import classes from other modules.

# Let's say we have a module of Car class stored in car.py that we want to import. We can import
# single modules:

from car import Car, ElectricCar

first_car = Car('audi', 'a4', 2016)
print(first_car.get_descriptive_name())

# Now that we've added the related Battery() and ElectricCar() classes to the car.py module, we can import them here:

electric_car = ElectricCar('tesla', 'model s', 2016)
electric_car.battery.getRange()

# We can import multiple classes as shown above using commas
# However, if we were to import the entire module without specifying which classes, we need to follow the format:
# module_name.function_name.parameters
# rather than calling the functions like they were in this file

# Let's say we store the electric car class and car class in separate modules, if we forget to from car import Car in the 
# electric_car.py module, we'll need to manually do it in our program.

# Python gives you multiple avenues for creating your own workflow, so keep your code structure simple starting out.
# Try making sure everything works first in one module before splitting everything up.

## Exercises 

print()

from Inheritance import Restaurant

food_stand = Restaurant('panda express', 'cuisine')
food_stand.customersServed()


## from InheritanceExercise import User, Admin, Privilege

## twitchMod = Admin('eric xie')
## print(twitchMod.login_attempts)
## twitchMod.priv.showPrivileges()

# Made sure to link the separate User, Admin, and Privileges files together using import statements:

print()

from user import User
from admin import Admin
from privilege import Privilege

twitchMod = Admin('eric xie')
twitchUser = User('alina zhang')

twitchUser.priv.showPrivileges()
twitchMod.priv.showPrivileges()
