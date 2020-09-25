class GameStats:
    """ Track statistics for Alien Invasion. """

    def __init__(self, ai_games):
        """ Initialize statistics. """
        self.setting = ai_games.setting
        self.reset_stats()
        # high score should never be reset
        with open('highscore.txt') as f:
            self.high_score = int(f.read())

        # start Alien Invasion in inactive state.
        self.game_active = False

    def reset_stats(self):
        """ Initialize statistics that can change during the game. """
        self.ship_left = self.setting.ship_limit
        self.score = 0
        self.level = 1

