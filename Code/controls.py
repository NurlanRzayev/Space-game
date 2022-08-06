import pygame, sys
from bullets import Bullet

def events(gun, screen, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                gun.mright = True
            elif event.key == pygame.K_LEFT:
                gun.mleft = True
            elif event.key == pygame.K_SPACE:
                new_bullet = Bullet(screen, gun)
                bullets.add(new_bullet)
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                    gun.mright = False
            elif event.key == pygame.K_LEFT:
                    gun.mleft = False

def update_screen(screen, bg_color, gun, bullets):
    screen.fill(bg_color)
    for bullet in bullets: # по видимому объекты класса Group итерируемы
        bullet.draw_bullet()
    gun.output()
    pygame.display.flip()

def remove_bullet(bullets):
    bullets.update() # вызов update() всех объектов входящих в группу
    for bullet in bullets:
        if bullet.rect.bottom <= 0:
            bullet.remove(bullets) 
    print(len(bullets)) 
                              
