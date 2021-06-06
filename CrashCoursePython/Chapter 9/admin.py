from user import User
from privilege import Privilege

class Admin(User):

    """ Simple admin class with special privileges that extends User"""

    def __init__(self, name):
        super().__init__(name)
        self.priv = Privilege('admin')