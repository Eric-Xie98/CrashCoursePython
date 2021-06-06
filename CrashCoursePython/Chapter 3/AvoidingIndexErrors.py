## When working with lists, always keep in mind that lists are indexed at 0, which means the first element has an index of 0, the next has 1, and so on
## This means the last element in the list has an index of len(list) - 1.

names = ["allinn", "nate", "edwin", "eric", "max"]
print("The name at index 3 of the names list is " + names[3])

## print(names[5]) would result in an index out of bounds error because there are only indexes 0 - 4 in the names list

## Using list[-1] prints the last element of the list, assuming that there are elements in the list; otherwise, it will return an error

print("This will always be the last element in the list: " + names[-1])
names.append("bryan")
print("The last element is now: " + names[-1])
