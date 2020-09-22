import sys
# we will use tools in the sys module to exit the game when the player quits.
import pygame
# we use pygame module to make the game.
from setting import Setting
from ship import Ship
from bullets import Bullet
from aliens import Alien


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
        self.bullet = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

    def run_game(self):
        """ Start the main loop of the game. """
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullet()
            self._update_screen()

    def _check_events(self):
        """Respond to key presses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """ Responding to key presses. """
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        """ Responding to key releases. """
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        elif event.key == pygame.K_q:
            sys.exit()

    def _fire_bullet(self):
        """ Create a new bullet and add it to the bullets group. """
        if len(self.bullet) < self.setting.bullet_number:
            new_bullet = Bullet(self)
            self.bullet.add(new_bullet)

    def _update_bullet(self):
        """ Updates the bullet position and get rid of old bullets. """
        # updates the bullet
        self.bullet.update()
        # removes the bullet out of screen
        for bullet in self.bullet.copy():
            if bullet.rect.bottom <= 0:
                self.bullet.remove(bullet)

    def _create_fleet(self):
        """ Create the flit of aliens. """
        # Make a alien and find the number of aliens in the row
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        available_space_x = self.setting.screen_width - (2 * alien_width)
        number_alien_x = available_space_x // (2 * alien_width)

        # determine the number of row of alien that can fit on the screen
        ship_height = self.ship.rect.height
        available_space_y = (self.setting.screen_height -
                             (3 * alien_height) - ship_height)
        number_rows = available_space_y // (2 * alien_height)

        # create the all rows of aliens.
        for row_number in range(number_rows):
            for alien_number in range(number_alien_x):
                self._create_alien(alien_number, row_number)

    def _create_alien(self, alien_number, row_number):
        """ Create a alien and place it in the row. """
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien_x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien_x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)

    def _update_screen(self):
        """ Updates images in the screen, and flip to new screen. """
        self.screen.fill(self.setting.bg_color)
        self.ship.blitme()
        for bullet in self.bullet.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)
        pygame.display.flip()


if __name__ == '__main__':
    # make the game instance and run the game.
    ai = AlienInvasion()
    ai.run_game()