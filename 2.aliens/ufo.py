import pygame
from pygame.sprite import Sprite


class Ufo(Sprite):
    def __init__(self, game, x, y) -> None:
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings
        self.ufo_direction = 1

        self.image = pygame.image.load('D:/1_Michael/python/vscode/2.aliens/images/ufo.bmp')
        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def blit_me(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        self.x += self.settings.ufo_speed * self.ufo_direction
        if self.x > self.screen.get_rect().right - self.rect.width or self.x < 0:
            self.ufo_direction *= -1
            self.y += self.rect.height
            self.rect.y = self.y
        self.rect.x = self.x
