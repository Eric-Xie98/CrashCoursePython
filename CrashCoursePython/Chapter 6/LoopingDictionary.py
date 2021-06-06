## Since dictionaries can contain abundant amounts of data and pairs, Python lets you loop through dictionaries,
## through both the keys and values

## We can loop through a dictioanry with something slike below:

user_1 = {'username': 'elx', 'first_name': 'eric', 'last_name': 'xie'}

for k, v in user_1.items():     ## .items() returns a list of key - value pairs
    print(k + ": " + v)         ## rather than did what I did previously, I can just simply use k, v for both key and value

print()

favorite_foods = {
    'eric': 'pussy',
    'nate': 'dick',
    'edwin': 'beatrice',
    'allinn': 'rammus',
    }

for name, food in favorite_foods.items():
    print(name.title() + "'s favorite food is " + food + "\n")

## If we were to loop through all keys in the dictionary, two methods work:

for name in favorite_foods.keys():
    break

for name in favorite_foods:
    break

## Looping through keys is the default behavior when looping through a dictionary

## You can use the keys() method to check whether or not an element is in a dictionary or not

if 'eric' in favorite_foods:
    print('I love pussy too')

if 'max' not in favorite_foods:
    favorite_foods['max'] = 'annette'

print(favorite_foods)

print()

## I can even print out the names in a sorted order:

for key in sorted(favorite_foods.keys()):
    print(key.title() + "'s favorite food is " + favorite_foods[key])

## If you only want the values in the dictionary, you the values() method

print()

print("The following food have been mentioned:")
for food in favorite_foods.values():
    print(food)

## However, when we pull out the values, there's potential for duplicates to be reprinted again and again, which is
## bad especially when there are a lot of duplicate values in a dictionary
## To counter this, use the set() method to remove any duplicates:

print()

duplicate = {'first': 1, 'second': 2, 'third': 1, 'fourth': 1}
for num in set(duplicate.values()):
    print(num, end = " ")


## Exercises

print("\n")

rivers = {'nile': 'egypt', 'amazon': 'brazil', 'yellow river': 'china'}

for river, country in rivers.items():
    print("The " + river.title() + " runs through " + country.title())

for river in rivers:
    print(river)

for country in rivers.values():
    print(country)

print()

favorite_languages = {
    'eric': 'java',
    'allinn': 'python',
    'edwin': 'sql',
    'max': 'c++',
    'nate': 'python',
    }

poll_people = ['max', 'jeff', 'josh', 'eric']

for person in poll_people:
    if person in favorite_languages:
        print(person.title() + ", thank you for taking the poll!")
    else:
        print(person.title() + ", p[ease fill out the poll!")

