import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """ A class to represent a single alien in a fleet. """

    def __init__(self, ai_game):
        """ Initialize the alien and set its starting position. """
        super().__init__()
        self.screen = ai_game.screen

        # load the alien image and set its rect attribute
        self.image = pygame.image.load('Images/alien.bmp')
        self.rect =  self.image.get_rect()

        # starting each new alien near the top left corner of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # store the alien's exact horizontal position.
        self.x = float(self.rect.x)
