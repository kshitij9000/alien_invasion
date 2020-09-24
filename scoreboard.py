import pygame.font


class Scoreboard:
    """ A class to report scoring information. """

    def __init__(self, ai_game):
        """ Initialize score keeping attribute. """
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.setting = ai_game.setting
        self.stats = ai_game.stats

        # font information for scoreboard
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        # prepare the initial score image
        self.prep_score()

    def prep_score(self):
        """ Turn the score into rendered image. """
        score_str = str(self.stats.score)
        self.score_image = self.font.render(score_str, True,
                                            self.text_color, self.setting.bg_color)
        # display score at top right of the screen
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_score(self):
        """ Draw the score into the screen. """
        self.screen.blit(self.score_image, self.score_rect)