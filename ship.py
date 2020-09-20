import pygame


class Ship:
    """ A class to manage the ship."""

    def __init__(self, ai_game):
        """ Initialize the ship and set its starting position. """
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        # needed only when the color of pygame windows is different than that of the image
        # since I am using grey theme I will not use self.bg_cp;pr and self.image.set_colorkey()
        # self.bg_color = (230, 230, 230)

        # load the ship image and get its rect.
        self.image = pygame.image.load('Images/ship.bmp')
        # self.image.set_colorkey(self.bg_color)
        self.rect = self.image.get_rect()

        # start new ship at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """ Draw the ship at its current location. """
        self.screen.blit(self.image, self.rect)
