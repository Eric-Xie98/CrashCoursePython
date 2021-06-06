class Privilege():

    def __init__(self, userType):
        if userType == 'admin':
            self.privileges = ['can mute user', 'can delete others post', 'can ban user', 'can pin post', 'can create own post', 'can delete own post', 'can comment']
        else:
            self.privileges = ['can create own post', 'can delete own post', 'can comment']
    
    def showPrivileges(self):
        print("This is your privileges:")
        for privilege in self.privileges:
            print(privilege)