## One of the simplest ways to save data is to write to a file. Even after the program is closed, you can
## still look at the output file in its stored location as well as share it to others. You can also
## write programs that read it back into memory and work with it again later.

# To write in a file, we use the open() method and its two arguments:

filename = 'programming.txt'
with open(filename, 'w') as file_object:
    file_object.write("I love programming.\n")
    file_object.write("I love creating new games.\n")
    file_object.write("Graphic design is my passion.\n")

# The open method's first argument is the filename while the second argument is the mode we want to open the file in:
# There is ('r') read mode, ('w') write mode, ('a') append mode, and ('r+') read and write mode. 
# By default, the open method is in read mode.

# If the file we're opening doesn't exist, the open method will automatically create it for us. However, be careful when
# you open an existing file in write mode, it can erase the previous contents and return a new file_object.

# These lines should create a new file with the said line inside. If we want to put numerical numbers inside, we'll need to use str()

## With the 'a' append mode, we can add more lines to the file without erasing the pre-existing data:

with open(filename, 'a') as file_object:
    file_object.write("This shows that I can append to what was written before.")

gameName = 'valorant.txt'
with open(gameName, 'w') as file_object:
    file_object.write('Valorant is a shit game.')


## Exercises

print()

active = True

with open('guest.txt', 'a') as file_object:

    while active:
        print("Type in 'q' at anytime to quit the program")
        name = input("Please write your name into the guestbook: ")
        if name == 'q':
            active = False
        else:
            file_object.write(name.title() + "\n")


active2 = True

with open('reasons.txt', 'a') as file_object:
    
    while active2:

        reason = input("Write a favorite reason why you do programming: ")
        if reason == 'quit':
            active2 = False
        else:
            file_object.write(reason + '\n')
    
    

