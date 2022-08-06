import pygame

class Bullet(pygame.sprite.Sprite):

    def __init__(self, screen, gun):
        super(Bullet, self).__init__()
        self.screen = screen
        self.rect = pygame.Rect(0, 0, 2, 12)
        self.rect.centerx = gun.rect.centerx
        self.rect.top = gun.rect.top
        self.color = 237, 236, 8
        self.speed = 1
    def update(self): # этот метод унаследован от Sprite
        self.rect.centery -= 1
    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
    
    