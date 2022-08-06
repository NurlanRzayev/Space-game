import pygame

class Alien(pygame.sprite.Sprite):

    def __init__(self, screen):
        super(Alien, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('images\ino.png')