## Similar to previously mentioned lists, we can use del to remove key - value pairs in dictionaries

user_1 = {'name': 'Eric', 'resturaunt': 'five guys'}
print("This is the dictionary before an element is removed: " + str(user_1))

del user_1['resturaunt'] ## delete pairs by calling the pair using the key
print("Now, the dictionary looks like this: " + str(user_1))

## When you're making a dictioanry of similar objects, you can store one kind of information about many objects:

favorite_languages = {
    'eric': 'java',
    'allinn': 'python',
    'max': 'hates coding',
    'edwin': 'python',      ## Including a comma at the end of each pair even the last one is good practice
    }                       ## Also make sure the closing squiggly brace is lined up with the key - value pairs

for key in favorite_languages:
    print(key.title() + "'s favorite coding language is " + favorite_languages[key].title())

## Exercises

print()

person_1 = {'first_name': 'Eric', 'last_name': 'Xie', 'age': 19, 'city': 'suwanee',}
print(person_1)

print()

favorite_numbers = {
    'eric': 98,
    'allinn': 69,
    'edwin': 14,
    'josh': 100,
    'nate': 11,
    }

print(favorite_numbers)

print()

glossary = {'boolean': 'logical operator', 'iteration': 'to loop repeatedly', 'dictionary': 'store key-value pairs',
'balls': 'in your mouth',}

for key in glossary:
     print(key + ":\n\t" + glossary[key])
