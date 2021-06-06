## Exercises for if statements involving multiple lists

usernames = ['Eric', 'Max', 'Edwin', 'admin', 'Allinn']
usernames.clear() ## used to check whether or not the empty list conditon triggers

if usernames:
    for name in usernames:
        if name == 'admin':
            print("Hello administrator, what would you like to work on?")
        else:
            print("Hello " + name + ", how can I help you?")
else:
    print('We need to find more users!')

print()

currentUsers = ['pussyeater444', 'joemama23', 'assebeater', 'eric', 'fatherfinger3', 'whyme']
newUsers = ['ERIC', 'jOEMAMA23', 'whyMe', 'yesman', 'WOOOHOO']

for user in newUsers:
    if user.lower() in currentUsers:
        print("This username is taken. Enter a new one.")
    else:
        print("This username is open")

print()

nums = list(range(1, 10))

for num in nums:
    if num < 2:
        print(str(num) + "st", end = " ")
    elif num == 2:
        print(str(num) + "nd", end = " ")
    elif num == 3:
        print(str(num) + "rd", end = " ")
    else:
        print(str(num) + "th", end = " ")
    
