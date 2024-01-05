import pygame.font


class Config:
    def __init__(self, text, width, height, bg_color, text_color, font, x, y) -> None:
        self.text = text
        self.width = width
        self.height = height
        self.bg_color = bg_color
        self.text_color = text_color
        self.font = font
        self.x = x
        self.y = y


class Button:
    def __init__(self, game, config) -> None:
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()

        self.width, self.height = config.width, config.height
        self.bg_color = config.bg_color
        self.text_color = config.text_color
        self.font = pygame.font.SysFont(None, config.font)

        self.rect = pygame.Rect(0, 0, self.width, self.height)
        if config.x == -1:
            self.rect.center = self.screen_rect.center
        else:
            self.rect.x = config.x
            self.rect.y = config.y

        self.crate_text_image(config.text)

    def crate_text_image(self, text):
        self.text_image = self.font.render(text, True, self.text_color, self.bg_color)
        self.text_image_rect = self.text_image.get_rect()
        self.text_image_rect.center = self.rect.center

    def draw(self):
        self.screen.fill(self.bg_color, self.rect)
        self.screen.blit(self.text_image, self.text_image_rect)


class Start_Button(Button):
    def __init__(self, game, config) -> None:
        super().__init__(game, config)


class Score_Button(Button):
    def __init__(self, game, config) -> None:
        super().__init__(game, config)
        self.score = 0
