import json

## Storing data exercises that retrieve the data


try:
    with open('favorite.json') as file_object:
        fave = json.load(file_object)
    print("Hey, " + str(fave) + " is my favorite number too!")
except FileNotFoundError:
    fave = input('Type in your favorite number: ')
    with open('favorite.json', 'w') as file_object:
        json.dump(fave, file_object)
else:
    print(str(fave) + " is my favorite number too!")

