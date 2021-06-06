# The Settings class will be where we store new code for when we add new functionality to the game.
# With all the settings in one class, it makes it easier to modify certain aspects rather than looking 
# all over the file for the correct path

class Settings():

    """A class that stores all the settings for Alien Invasion"""

    def __init__(self):
        
        """Initialize game settings"""

        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Ship settings
        self.ship_speed_factor = 1.5

# This was the code that we initally had manually written in alien_invasion, but then put it
# all here for ease of access 