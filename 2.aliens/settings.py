class Settings:
    def __init__(self) -> None:
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.color_base = 50

        self.ship_speed = 0.3
        self.fire_intervel = 100
        self.max_bullet_number = 6
        self.ship_limit = 3

        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)

        self.ufo_speed = 0.2

    def set_bg(self, win):
        # self.color_base = (self.color_base + 1) % 255
        # self.bg_color = (self.color_base,
        #                  (self.color_base + 100) % 255,
        #                  (self.color_base + 200) % 255)
        win.screen.fill(self.bg_color)
