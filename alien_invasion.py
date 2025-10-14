import sys
import pygame 
from settings import *
from ship import *
from bullet import *

class AlienInvasion:
    """Overall class to manage game assests and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_width = self.screen.get_rect().height
        # self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height
        # self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion")
        # Set the background color.
        # self.bg_color = (230, 230, 230)
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self.__check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self.__check_keyup_events(event)
    
    def __check_keydown_events(self, event):
        """Respond to keypresses."""
        if event.key == pygame.K_RIGHT:
            # Move the ship to the right.
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
                # Move the ship to the left.
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
    
    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group."""
        if len(self.bullets) < 3:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def __check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def __update_bullets(self):
        """Update position of bullets and get rid of old bullets."""
        # Update bullet positions.
        self.bullets.update()
        # Get rid of bullets that have disappeared.
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
    
    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.blitme()
        pygame.display.flip()
        self.clock.tick(60)

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self.ship.update()
            self.__update_bullets()
            self._update_screen()

if __name__ == '__main__':
    #make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()
