import sys
# we will use tools in the sys module to exit the game when the player quits.
import pygame
# we use pygame module to make the game.
from setting import Setting
from ship import Ship


class AlienInvasion:
    """ Overall class to manage game assets and behaviour. """

    def __init__(self):
        """ Initialize the game and create game resources. """
        # initializes the background settings that Pygame needs to work properly
        pygame.init()
        self.setting = Setting()

        # creates a display window assign this display
        self.screen = pygame.display.set_mode(
            (self.setting.screen_width, self.setting.screen_height))
        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self)

    def run_game(self):
        """ Start the main loop of the game. """
        while True:
            # watch for keyboard and mouse events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                # redraw the screen during each pass through loop
                self.screen.fill(self.setting.bg_color)
                self.ship.blitme()
                # makes the most recently drawn screen visible.
                pygame.display.flip()


if __name__ == '__main__':
    # make the game instance and run the game.
    ai = AlienInvasion()
    ai.run_game()