import pygame, sys
from bullets import Bullet
from aliens import Alien
import time

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
    aliens.draw(screen) # метод группы draw() выполняет метод blit() для объектов группы, если были объявлены свойства self.image и self.rect и переданы им объекты соотв. классов
    pygame.display.flip()

def remove_bullet(bullets, aliens, screen):
    bullets.update() # вызов update() всех объектов входящих в группу
    for bullet in bullets:
        if bullet.rect.bottom <= 0:
            bullet.remove(bullets) 
    print(len(bullets))
    pygame.sprite.groupcollide(bullets, aliens, True, True)
    if len(aliens) == 0:
        bullets.empty()
        create_army(screen, aliens)

def create_army(screen, aliens):
    alien = Alien(screen) # этот объект создается для того чтобы воспользоваться свойствами класса Rect, он не будет отображатся потому что он не добавлен в группу
    number_aliens = int((600 - 2 * alien.rect.width) / alien.rect.width)
    number_rows = int((700 - 100 - 6 * alien.rect.height) / alien.rect.height)
    for row_number in range(number_rows):
        for alien_number in range(number_aliens):
            alien = Alien(screen)
            alien.rect.x = alien.rect.width + alien.rect.width * alien_number
            alien.y = alien.rect.height + alien.rect.height * row_number # здесь важно менять alien.y, а не alien.rect.y, в противном случае alien.y неизменившись останется равным первому значению alien.rect.y присвоенному ей в конструкторе класса при создании объекта alien (это значение ноль). Это приведет к тому что после создания армии пришельцев, при вызове метода update() у всех объектов класса, свойству alien.rect.y каждого объекта присвоится значение alien.y, равное при первой итерации int(0 + 0.1), т. е. все объекты alien будут выводится на экран в одну строку и начинать движение с координаты ноль по вертикали
            alien.add(aliens)

def remove_aliens(stats, screen, aliens, gun, bullets):
    aliens.update() # вызов update() всех объектов входящих в группу
    if pygame.sprite.spritecollideany(gun, aliens):
        gun_kill(stats, screen, gun, aliens, bullets)
    aliens_check(stats, screen, gun, aliens, bullets)

def gun_kill(stats, screen, gun, aliens, bullets):
    stats.gun_health -= 1
    aliens.empty()
    bullets.empty()
    create_army(screen, aliens)
    gun.gun_new_start()
    time.sleep(1) # задержка time.sleep() принимает секунды, а не миллисекунды, в отличии от задержки pygame.time.delay(), т. е. такая задержка плохо подходит как постоянная (в основном цикле игры), по сравнению с delay() 

def aliens_check(stats, screen, gun, aliens, bullets):
    for alien in aliens.sprites():
        if alien.rect.bottom >= gun.screen_rect.bottom:
            gun_kill(stats, screen, gun, aliens, bullets)
            break 

                              
