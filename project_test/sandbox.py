import sys

import pygame

from sandbox_settings import Settings
from soy import Soy

class Sandbox:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.settings = Settings()

        # These lines are for fullscreen.
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height

        # These lines are for windowed.
        # self.screen = pygame.display.set_mode(
        #     (self.settings.screen_width, self.settings.screen_height))

        pygame.display.set_caption("Sandbox")

        self.soy = Soy(self)

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self.soy.update()
            self._update_screen()

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Responds to keypresses."""
        if event.key == pygame.K_RIGHT:
            self.soy.moving_right = True
        if event.key == pygame.K_LEFT:
            self.soy.moving_left = True
        if event.key == pygame.K_DOWN:
            self.soy.moving_down = True
        if event.key == pygame.K_UP:
            self.soy.moving_up = True

    def _check_keyup_events(self, event):
        """Responds to key releases."""
        if event.key == pygame.K_RIGHT:
            self.soy.moving_right = False
        if event.key == pygame.K_LEFT:
            self.soy.moving_left = False
        if event.key == pygame.K_DOWN:
            self.soy.moving_down = False
        if event.key == pygame.K_UP:
            self.soy.moving_up = False
        if event.key == pygame.K_q:
            sys.exit()

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        self.soy.blitme()

        pygame.display.flip()

if __name__ == '__main__':
    # Make a game instance, and run the game.
    sb = Sandbox()
    sb.run_game()