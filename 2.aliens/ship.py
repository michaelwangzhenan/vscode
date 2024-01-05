import pygame


class Ship:
    def __init__(self, game) -> None:
        self.settings = game.settings
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()

        self.image = pygame.image.load('D:/1_Michael/python/vscode/2.aliens/images/ship.bmp')
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom
        # self.rect.left = 100
        # self.rect.center = self.screen_rect.center
        # self.rect.center = (1000, 100)
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

        self.x = self.rect.x
        self.y = self.rect.y

        self.firing = False
        self.fire_controller = 0

    def blit_me(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        elif self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.ship_speed
        elif self.moving_up and self.rect.top > 0:
            self.y -= self.settings.ship_speed
        self.rect.x = self.x
        self.rect.y = self.y

    def counter_plus_one(self):
        self.fire_controller += 1

    def counter_reset(self):
        self.fire_controller = 0

    def can_fire(self, curent_bullet_number) -> bool:
        return self.firing and (self.fire_controller > self.settings.fire_intervel) and (curent_bullet_number < self.settings.max_bullet_number)
