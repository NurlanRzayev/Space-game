import pygame, controls
from gun import Gun

def run():
    pygame.init()
    screen = pygame.display.set_mode((600, 700))
    pygame.display.set_caption('Космические защитники')
    bg_color = (0, 0, 0)
    gun = Gun(screen)
    bullets = pygame.sprite.Group()

    while True:
        controls.events(gun, screen, bullets)
        gun.move()
        controls.remove_bullet(bullets) 
        controls.update_screen(screen, bg_color, gun, bullets)
        
run()