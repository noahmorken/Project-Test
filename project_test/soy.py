import pygame

class Soy:
    """A class to manage the soyjak."""

    def __init__(self, sb_game):
        """Initialize the ship and set its starting position."""
        self.screen = sb_game.screen
        self.settings = sb_game.settings
        self.screen_rect = sb_game.screen.get_rect()

        # Load the image and get its rect.
        self.image = pygame.image.load('C:/Users/noahm/Documents/python/project_test/images/soyjak.bmp')
        self.rect = self.image.get_rect()

        # Start the soyjak at the center of the screen.
        self.rect.center = self.screen_rect.center

        # Store a decimal value for the ship's position.
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # Movement flag
        self.moving_right = False
        self.moving_left = False
        self.moving_down = False
        self.moving_up = False

    def update(self):
        """Update the soyjak's position based on movement flags."""
        # Update the soyjak's x value, not the rect.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.soy_speed
        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.x -= self.settings.soy_speed

        # Update the soyjak's y value, not the rect.
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.soy_speed
        if self.moving_up and self.rect.top > self.screen_rect.top:
            self.y -= self.settings.soy_speed

        # Update rect object from self.x and self.y.
        self.rect.x = self.x
        self.rect.y = self.y

    def blitme(self):
        """Draw the soyjak at its current location."""
        self.screen.blit(self.image, self.rect)