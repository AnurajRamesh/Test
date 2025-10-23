import pygame

from pygame.sprite import Sprite

class Alien(Sprite):
    """ Create single alien to the game window!"""

    def __init__(self, ai_settings, screen):
        
        super().__init__()
        self.ai_settings = ai_settings
        self.screen = screen

        # Load the alien image and position it to the screen
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # Position alien to top left corner of window
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the x coordinate of alien as floating decimel value
        self.x = float(self.rect.x)

    def blitme(self):
        """ Show the alien to the screen"""
        self.screen.blit(self.image, self.rect)