import pygame
from pygame.locals import *
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
COUNT = 50
score = 0

food_sprites_dict = {
    1: "assets/sprites/1apple.png",
    2: "assets/sprites/2avocado.png",
    3: "assets/sprites/3banana.png",
    4: "assets/sprites/4cherry.png",
    5: "assets/sprites/5coconut.png",
    6: "assets/sprites/6pineapple.png",
    7: "assets/sprites/7tomato.png",
    8: "assets/sprites/8eggplant.png",
    9: "assets/sprites/9chili.png"

}


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.image.load("assets/sprites/monkey.png").convert_alpha()
        self.surf = pygame.transform.scale(self.surf, (75, 90))
        self.rect = self.surf.get_rect()

    def update(self, k_pressed):
        self.rect.centery = SCREEN_HEIGHT - 118
        if k_pressed[K_LEFT]:
            self.rect.move_ip(-9, 0)
        if k_pressed[K_RIGHT]:
            self.rect.move_ip(9, 0)

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH


class Food(pygame.sprite.Sprite):
    def __init__(self, type):
        super().__init__()
        if type == "fruits":
            self.surf = pygame.image.load(food_sprites_dict[random.randint(1, 6)])
        elif type == "veggies":
            self.surf = pygame.image.load(food_sprites_dict[random.randint(7, 8)])
        elif type == "chili":
            self.surf = pygame.image.load(food_sprites_dict[9])
        self.type = type
        self.surf = pygame.transform.scale2x(self.surf)
        self.rect = self.surf.get_rect(
            center=(
                random.randint(0, SCREEN_WIDTH),
                -10
            )
        )
        self.speed = random.randint(6, 15)

    def update(self):
        self.rect.move_ip(0, self.speed)
        if self.rect.bottom < 0:
            self.kill()

