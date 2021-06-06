## Usually your lists will be given in unpredictable order, so how would you sort them?

## Permanent sort using the sort() method, which sorts them alphabeticaly (takes into account capitalization)

people = ["Mao Ze Dong", "Pol Pot", "Adolf Hitler", "Gandhi"]
people.sort()   ## You can't undo this sort
print(people)
people.sort(reverse=True) # You can even the reverse the sort
print(people)

## You can temporarily sort the list using the sorted() method with the argument as the list

colors = ["red", "blue", "yellow", "green"]
print(sorted(colors))
print(colors)

## I can print a list in reverse order by using a .reverse() method

colors.reverse()
print(colors) # Permanent reverse sort
colors.reverse()
print(colors) # We can reverse the reverse by calling it again on the list

print("\n")

## Count the number of elements in a String and a list using len() method

print("The number of elements inside colors is " + str(len(colors)))
strName = "Joe mama"
print(len(strName))
print("The length of the variable str is " + str(len(strName)))
print("\n")

## Exercises

places = ["Japan", "South Korea", "France", "Germany", "Italy"]
print("Here's a list of the places I want to go to: " + str(places))
print("The sorted list: " + str(sorted(places)))
print("The original list: " + str(places))
print("The sorted reverse list: " + str(sorted(places, reverse=True)))
print("Back to the original: " + str(places))
print("\n")

places.reverse()
print(places)
places.reverse()
print(places)
print("\n")

places.sort()
print(places)
places.sort(reverse=True)
print(places)

print("I am planning to go to " + str(len(places)) + " places in the future")


