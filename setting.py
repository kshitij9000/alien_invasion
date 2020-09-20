class Setting:
    """ A class to store all the settings for Alien Invasion. """

    def __init__(self):
        """ Initialize the game setting. """
        # screen setting
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        # ship setting
        self.ship_speed = 1.5