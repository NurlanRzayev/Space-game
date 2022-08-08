import pygame, sys
from bullets import Bullet
from aliens import Alien

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

def update_screen(screen, bg_color, gun, bullets, aliens):
    screen.fill(bg_color)
    for bullet in bullets: # по видимому объекты класса Group итерируемы
        bullet.draw_bullet()
    gun.output()
    aliens.draw(screen)
    pygame.display.flip()

def remove_bullet(bullets):
    bullets.update() # вызов update() всех объектов входящих в группу
    for bullet in bullets:
        if bullet.rect.bottom <= 0:
            bullet.remove(bullets) 
    

def create_army(screen, aliens):
    alien = Alien(screen)
    number_aliens = int((600 - 2 * alien.rect.width) / alien.rect.width)
    number_rows = int((700 - 100 - 6 * alien.rect.height) / alien.rect.height)
    for row_number in range(number_rows):
        for alien_number in range(number_aliens):
            alien = Alien(screen)
            alien.rect.x = alien.rect.width + alien.rect.width * alien_number
            alien.rect.y = alien.rect.height + alien.rect.height * row_number
            alien.add(aliens)

                              
