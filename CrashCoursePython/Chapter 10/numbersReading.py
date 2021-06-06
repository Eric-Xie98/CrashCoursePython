## Made as the second program to retrieve the information stored in the numbers.json module

import json

filename = 'numbers.json'

with open(filename) as file_object:
    numbers = json.load(file_object)        ## We use json.load(file_object) to retrieve whatever data is in the json

print(numbers)      ## Numbers are printed how they were stored in StoringData.py

# Retrieval method looks quite similar to the dump