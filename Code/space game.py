import pygame, controls
from gun import Gun
from stats import Stats

def run():
    pygame.init()
    screen = pygame.display.set_mode((600, 700))
    pygame.display.set_caption('Космические защитники')
    bg_color = (0, 0, 0)
    gun = Gun(screen)
    bullets = pygame.sprite.Group()
    aliens = pygame.sprite.Group()
    controls.create_army(screen, aliens)
    stats = Stats()

    while True:
        controls.events(gun, screen, bullets)
        gun.move()
        controls.remove_bullet(bullets, aliens, screen) 
        controls.remove_aliens(stats, screen, aliens, gun, bullets)
        controls.update_screen(screen, bg_color, gun, bullets, aliens)
    
run()