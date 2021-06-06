## In this chapter covering Files and Exceptions, we'll be learning how to handle errors and throw exceptions.
## We'll also learn about the json module that'll let us save data so it isn't lost when the program
## stops running. Throwing exceptions make programs for robust when they encounter bad data.

# When we want to work with information on a file, we need to read it into memory, whether one line at a time or the whole thing.

# We have a text file called pi_digits.txt that has the first 30 digits of pi with 10 decimals printed on each line.
# Here's code that opens the file, reads it, and prints the content to the screen.

with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents)

# The first line of this program uses the open() function, which takes one argument, the file name. Python looks
# for the file in the directory where the program being ran is stored. The open() returns a file object and we rename it
# as file_object.

# Normally, there's a close() function to close the file when we're done with it but improperly closing files can result 
# in data corruption, so it's better to let Python automatically close it.

# As you can see in the next line, the read() takes the file_object and stores it into one long string in the variable contents
# where we print it in the next line.

# Weirdly, in the textbook there's an extra whitespace, but for us it isn't there. If we wanted to remove this whitespace, use
# .rstrip() on contents during print to remove that extra white space from the right side of a string

## So what happens when you want to get a file from a different folder? For relative folders that are inside the same directory
## as the current program:

# with open('text_files/file_name.txt') as file_object:

## An absolute file path is where the file is stored in a completely other folder, so you'll have to write the absolute
## file path for Python to navigate there:

# filepath = '/Users/ericx/Downloads/ThinkPython/other_files/text_files/file_name.txt'
# with open(filepath) as file_object:

## This should now let you navigate to any folder in your system.

print("Now we're gonna talk about reading line by line.")
print()

filename = 'pi_digits.txt'
with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())

# The for loop that takes each line in the file_object prints its contents.
# We can get rid of the spaces in between by using .rstrip() as mentioned before

#v We can store all the file's liens in a variable:

print()

filename2 = "/Users/ericx/Downloads/ThinkPython/CrashCoursePython/Chapter 10/pi_digits.txt"

with open(filename2) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())

# Now that we have read the file, we can do stuff with the lines:

total = ''

for line in lines:
    total += line.strip()       ## .strip() removes all the whitespace on both sides

print(total)
print("Length: " + str(len(total)))

birthdayString = ''

bigfile = 'pi_million_digits.txt'
with open(bigfile) as file_object:
    for line in file_object.readlines():
        birthdayString += line.strip()

birthday = '092601'
if birthday in birthdayString:
    print("Your birthday number is in a million digits of pi!")
else:
    print("Your birthday digits are unfortunately not in a million digits of pi.")

## Exercises

print()

with open('learning_python.txt') as file_object:
    contents = file_object.read()

    for i in range(3):
        print(contents)

    print()

with open('learning_python.txt') as file_object2:
    for line in file_object2.readlines():
        print(line.strip())
    
    print()

with open('learning_python.txt') as file_object3:
    lines = file_object3.readlines()

    for line in lines:
        print(line.strip())

print()

with open('learning_python.txt') as file_object4:

    for line in file_object4.readlines():
        print(line.replace('Python', 'C').strip())