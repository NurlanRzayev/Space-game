import pygame

class Alien(pygame.sprite.Sprite):

    def __init__(self, screen):
        super(Alien, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('images\ino.png')
        self.rect = self.image.get_rect()
        self.y = float(self.rect.y) # т. к. объекты класса rect не могут хранить вещевственные числа, вводим эту переменную
    def update(self): # этот метод унаследован от Sprite
        self.y += 0.1 # чтобы движение было не таким быстрым увеличиваем не на целое число
        self.rect.y = self.y # передаем получившееся число в свойство класса rect, где оно будет переведено в целое число, таким образом координата self.rect.y будет смещатся на целую часть прибаляемого числа, после нескольких итераций (в данном случае 10) дробная часть self.y составит также 1 целую, которая прибавится к целой части self.y и таким образом self.rect.y сместится на 1 больше относительно последней итерации