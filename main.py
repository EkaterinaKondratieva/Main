import os
import sys
import random

import pygame
from pygame.locals import *

pygame.init()

fps = 60
fpsClock = pygame.time.Clock()

width, height = 300, 300
screen = pygame.display.set_mode((width, height))


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname).convert_alpha()
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


class Hero(pygame.sprite.Sprite):
    hero_image = load_image('creature.png')

    def __init__(self, *groups):
        super().__init__(*groups)
        self.image = Hero.hero_image
        self.rect = self.image.get_rect()

    def move_right(self):
        self.rect.x += 10

    def move_left(self):
        self.rect.x -= 10

    def move_down(self):
        self.rect.y += 10

    def move_up(self):
        self.rect.y -= 10


all_sprites = pygame.sprite.Group()
hero = Hero(all_sprites)

while True:
    screen.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.scancode == 79:
                hero.move_right()
            elif event.scancode == 80:
                hero.move_left()
            elif event.scancode == 81:
                hero.move_down()
            elif event.scancode == 82:
                hero.move_up()

    all_sprites.draw(screen)
    pygame.display.flip()
    fpsClock.tick(fps)
