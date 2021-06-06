## Functions usually return a value, and in Java, this would make the function not void: 

def getFormalName(first, last):
    formal = first.title() + " " + last.title()
    return formal

print(getFormalName('eric', 'xie'))     ## Because the function only returns a value, we need to manually print it

## Even though this looks far more complicated than just writing a singular print statement, the function is more for
## large - scale use such as with a user database and all we need is just a function call to print a formal name

## We can make arguments optional depending on whether they're necessary or not:

def getFullName(first, last, middle = ''):      ## Setting middle to a default value of empty string when no argument is given to it

    if middle:                  
        return first.title() + " " + middle.title() + " " + last.title()
    else:
        return first.title() + " " + last.title()

print(getFullName('eric', 'xie'))

## As you can see, if a middle argument is given, the if statement triggers the code that preps for middle names
## Otherwise, only the first and last name are used.

## We can actually convert getFormalName into getFullName for less functions and a cleaner coding interface

## Let's say we want to use a function to build and return a dictionary:

def buildPerson(first, last, middle = '', age = ''):        ## Optional values middle and last
    
    person = {'first': first, 'last': last}
    if age:
        person['age'] = age
    if middle:
        person['middle'] = middle
    
    return person

print(buildPerson('eric', 'xie', 'liran'))
print(buildPerson('alina', 'zhang', age = '17'))

## We can use functions inside a while loop:

while True:
    print('Please enter your full name!')
    print("Enter 'q' anytime to quit.")

    first = input("Enter your first name:\n")
    if first == 'q':
        break
    last = input("Enter your last name\n")
    if last == 'q':
        break
    
    print(getFormalName(first, last))

## Exercises

def cityCountry(city_name, country_name):
    return city_name.title() + ", " + country_name.title()

print(cityCountry("Atlanta", "US"))
print(cityCountry("Beijing", "China"))
print(cityCountry(country_name = 'Your', city_name = 'mom'))

print()

def makeAlbum(artistName, albumTitle):

    album = {'artist': artistName.title(), 'album': albumTitle.title()}
    return album

print(makeAlbum('post malone', "hollywood's bleeding"))
print(makeAlbum("blackbear", "everything means nothing"))
print(makeAlbum('logic', 'bobby tarantino II'))

while True:

    print("Type 'q' anytime to quit program")

    artist = input("What is the name of the artist? ")
    if artist == 'q':
        break
    
    album = input("What is the name of the album? ")
    if album == 'q':
        break

    print(makeAlbum(artist, album))


