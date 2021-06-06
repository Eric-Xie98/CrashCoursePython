## We'll see that arguments for a function can take a variety of different forms, where in some cases we might need multiple arguments.

## We can use positional arguments, ones that must be in the same order as the function definition.
##  When we call a fuunction, Python must match each argument up to its corresponding parameter:

def describePet(breed, name, age):
    print('\tAnimal Info:')
    print("Breed: " + str(breed))
    print("Name: " + name)
    print("Age: " + str(age))

describePet('Labrador', 'Maxie', 12)

## We can do multiple function calls of the same kind with the same or different parameters. Each function call
## its "own parameters" that are different from another call of the same function

describePet('Poodle', 'Shitass', 100)

## If we mess up the position of our arguments, they will pass to the function incorrectly:

describePet(100, 'Poodle', 'Shitass')

## A keyword argument is a name-value pair that prevents problems from happening like in the previous statement. Keyword arguments
## allow programmers from worrying about the correct order of the arguments, and instead focus on the code itself:

describePet(name = 'harry', age = 100, breed = 'hamster')   ## Even though the order of the arguments doesn't line up with the function def,

## it still correctly feeds the arguments to the parameters in the function

## While writing function defintions, you can set default values for the parameters:

def seasonsGreetings(name, holiday = 'Christmas'):      ## Setting the holiday paramter already in the definition ensures that its default value is Christmas
    print('Merry ' + holiday + ", " + name.title())

seasonsGreetings(name = 'eric')     ## We can now not have to put in a specific value for the holiday parameter.
seasonsGreetings('eric')            ## also works only because the default is after the one that's not

## default values must be after any parameters that don't automatically have a default value otherwise postional errors will kick in

## Because positional, keyword arguments, and default values can be used, there are multiple equivalent ways a function with the same output can be called.
## Avoiding argument errors can range from as simple as not inputting all the parameters required to giving the wrong arguments based on postional reasons

## Python reads the function code for us and tells us the name of the arguments that are missing. Therefore providing more descriptive code not only helps
## you, but it helps future readers of your code as well.

## Exercises

print()

def makeShirt(size, message):
    print("This T-Shirt is an " + size.title() + " and it says \"" + message.title() + "\"")

makeShirt('large', 'skip class eat ass')
makeShirt(message = 'skip class eat ass', size = 'extra large')

def newShirt(size, message = 'I Love Python'):
    print("This T-Shirt is an " + size.title() + " and it says \"" + message.title() + "\"")    

newShirt('large')
newShirt('medium')
newShirt('large', 'joe mama')

print()

def describeCity(city, country = 'iceland'):
    print(city.title() + " is in " + country.title())

describeCity('beijing')
describeCity('atlanta')
describeCity('rejiskvac')
describeCity('my dick', 'your mom')

