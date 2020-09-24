class GameStats:
    """ Track statistics for Alien Invasion. """

    def __init__(self, ai_games):
        """ Initialize statistics. """
        self.setting = ai_games.setting
        self.reset_stats()

        # start Alien Invasion in inactive state.
        self.game_active = False

    def reset_stats(self):
        """ Initialize statistics that can change during the game. """
        self.ship_left = self.setting.ship_limit

