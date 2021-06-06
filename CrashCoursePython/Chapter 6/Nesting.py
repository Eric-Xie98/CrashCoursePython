## We can use nesting to store dictionaries or list inside dictionaries to create more complex and detailed data structures

alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'red', 'points': 10}
alien_2 = {'color': 'yellow', 'points': 15}

aliens = [alien_0, alien_1, alien_2]    ## This creates a list of dictionaries, in this case, a list of the aliens

## Normally, a screen would have far more aliens, and this list would contain many more alien dictionaries
## We can add more using a for loop but we start with an empty list first:

aliens2 = []

for i in range(10):
    new_alien = {'color': 'yellow', 'points': 15}
    aliens2.append(new_alien)

## print(aliens2)   ## These aliens are all separate, different objects, so if we need to change them later, we can use a list slice to change specific entries
print("Total number of aliens: " + str(len(aliens2)))

for alien in aliens[0:3]:
    if alien['color'] == 'green':       ## Makes sure that we're only changing aliens that were previously green
        alien['color'] = 'red'
        alien['points'] = 10
    elif alien['color'] == 'red':       ## This elif upgrades aliens if they were already red this time around
        alien['color'] = 'yellow'
        alien['points'] = 15
    
print(aliens)

## Dictionaries in a list work best when all the dictionaries have similar elements as we had in this one with all aliens
## A user database of a list could work like this

## So what about a list in a dictionary?
## This gives you the ability to be more in-depth on certain elements

pizza = {'crust': 'thin', 'toppings': ['extra cheese', 'pepperoni', 'bacon']}
print("You ordered a pizza with " + pizza['crust'] + " crust and these toppings:")
for topping in pizza['toppings']:
    print("\t" + topping)


favorite_languages = {
    'eric':  ['java', 'python', 'octave'],
    'allinn':  ['python', 'java'],
    'edwin': ['sql', 'python'],
    'max':  ['matlab'],
    'nate': ['matlab', 'python'],
    }

for name, languages in favorite_languages.items():
    if len(languages) == 1:
        print(name.title() + "'s favorite coding language is:")
    else:
        print(name.title() + "'s favorite coding languages are:")
    
    for language in languages:
        if(language == 'sql' or language == 'matlab'):
            print("\t" + language.upper())
        else:
            print("\t" + language.title())
    
    print()

## It's possible to nest dictionaries within dictionaries, but it can quickly become complicated.
## An example is if we had several users for a website, we can use their usernames as the key, and the value would be another dictionary detailing their personal info:

users = {
    'aeinstein': {'first_name': 'albert', 'last_name': 'einstein', 'location': 'princeton'},
    'emusk': {'first_name': 'elon', 'last_name': 'musk', 'location': 'mars'},
    'mcurie': {'first_name': 'marie', 'last_name': 'curie', 'location': 'paris'}
    }

for user, info in users.items():
    
    if(user == 'emusk'):
        print('Welcome back, ' + 
        info['first_name'].title() + " " + info['last_name'].title() + 
        " (Username: " + user + ") , how's the base expansion on " + 
        info['location'].title() + " doing?")
    else:
        print("Welcome back, " + 
        info['first_name'].title() + " " + info['last_name'].title() + 
        " (Username: " + user + ") , what's the weather like in " + 
        info['location'].title() + "?")

## As you can see above, dictionaries nested in other dictionaries can be done like this, but can become far more complicated if the structures of
## each element are different

print()

## Exercises

person1 = {'first_name': 'eric', 'last_name': 'xie', 'age': 19}
person2 = {'first_name': 'nate', 'last_name': 'kim', 'age': 19}
person3 = {'first_name': 'edwin', 'last_name': 'suh', 'age': 18}

people = [person1, person2, person3]

for person in people:
    print('First Name: ' + person['first_name'].title())
    print('Last Name: ' + person['last_name'].title())
    print('Age: ' + str(person['age']))
    print()

favorite_places = {
    'eric': ['tokyo', 'beijing', 'hell'],
    'edison': ['florida', 'april'],
    'chad': ['north carolina', 'duke'],
    }

for name, places in favorite_places.items():
    print(name.title() + "'s favorite places are: ")
    for place in places:
        print("\t" + place.title())

cities = {
    'atlanta': {'state': 'georgia', 'known for': 'tech', 'population': 2000000},
    'durham': {'state': 'north carolina', 'known for': 'duke', 'population': 10000},
    'new york': {'state': 'new york', 'known for': 'empire state building', 'population': 3000000},
    }

for city, city_info in cities.items():
    print(city.title() + ":")

    for category, value in city_info.items():
        if type(value) == int:
            print("\t" + category.title() + ": " + str(value))
        else:
            print("\t" + category.title() + ": " + value.title())

