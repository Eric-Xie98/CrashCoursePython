from privilege import Privilege

class User():

    def __init__(self, name):
        self.name = name
        self.login_attempts = 0
        self.priv = Privilege('user')

    def incrementAttempts(self):
        self.login_attempts += 1
        if(self.login_attempts == 3):
            print("You are temporarily locked out for 5 minutes!")

    def resetAttempts(self):
        self.login_attempts = 0
