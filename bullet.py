import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """ A class to manage bullets fired from the ship. """

    def __init__(self, ai_games):
        """ Creates a bullet object at ship's current position. """
        super.__init__()
        self.screen = ai_games.screen
        self.setting = ai_games.setting
        self.color = self.setting.bullet_color

        # create a bullet rect at (0, 0) and then set correct position.
        self.rect = pygame.Rect(0, 0, self.setting.bullet_width, self.setting.bullet_height)
        self.rect.midbottom = ai_games.ship.rect.midbottom

        # store the bullet's position as a decimal value
        self.y = float(self.rect.y)

    def update(self):
        """ Move the bullet up the screen. """
        # update the decimal position of the bullet.
        self.y -= self.setting.bullet_speed
        # update the rect position.
        self.rect.y = self.y

    def draw_bullet(self):
        """ Draw the bullet to the screen. """
        pygame.draw(self.screen, self.color, self.rect)