import sys
import pygame
from time import sleep

from settings import Settings
from ship import Ship
from bullet import Bullet
from ufo import Ufo
from game_statistics import GameStatistics
from start_button import Start_Button, Score_Button, Config


class Game:
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        # self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        # self.settings.screen_width = self.screen.get_rect().width
        # self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Shooting UFO")

        self.runing = False
        self.pause = False
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.ufo_fleet = pygame.sprite.Group()
        self.statistics = GameStatistics(self)

        self._create_ufo_fleet()

        # (self, text, width, height, bg_color, text_color, font)
        self.config_start = Config("Start", 200, 50,  (0, 255, 0), (255, 255, 255), 48, -1, -1)
        self.start_button = Start_Button(self, self.config_start)

        self.config_score = Config("0", 150, 50,  (255, 255, 0), (255, 0, 255), 48, 1040, 10)
        self.score_button = Score_Button(self, self.config_score)

    def run(self):
        while True:
            self._check_event()
            self._update_screen()

    def _check_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                self._check_mouse_to_start(pos)
                # sleep(0.5)
            elif event.type == pygame.KEYDOWN:
                self._check_event_keydown(event)
            elif event.type == pygame.KEYUP:
                self._check_event_keyup(event)

    def _check_event_keydown(self, event):
        if event.key == pygame.K_LEFT or event.key == pygame.K_a:
            self.ship.moving_left = True
        elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
            self.ship.moving_right = True
        elif event.key == pygame.K_UP or event.key == pygame.K_w:
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
            self.ship.moving_down = True
        elif event.key == pygame.K_SPACE or event.key == pygame.K_j:
            self.ship.firing = True
        elif event.key == pygame.K_RETURN:
            # self._restart()
            self.runing = False
            self.pause = True
            pygame.mouse.set_visible(True)
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_event_keyup(self, event):
        if event.key == pygame.K_LEFT or event.key == pygame.K_a:
            self.ship.moving_left = False
        elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
            self.ship.moving_right = False
        elif event.key == pygame.K_UP or event.key == pygame.K_w:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
            self.ship.moving_down = False
        elif event.key == pygame.K_SPACE or event.key == pygame.K_k:
            self.ship.firing = False

    def _update_screen(self):
        self.settings.set_bg(self)
        self._check_start_button()
        self._draw()
        if self.runing:
            self._update_ship(len(self.bullets))
            self._update_bullet()
            self._check_collisions()
            self._update_ufo_fleet()
            self._new_wave()
            self._check_ship_collision()

        pygame.display.flip()

    def _draw(self):
        if self.runing or self.pause:
            self.ship.blit_me()
            self.ufo_fleet.draw(self.screen)
            self.score_button.draw()
            # for ufo in self.ufo_fleet:
            #     ufo.blit_me()

    def _update_ship(self, curent_bullet_number):
        self.ship.update()
        self.ship.counter_plus_one()

        if self.ship.can_fire(curent_bullet_number):
            self._fire()
            self.ship.counter_reset()

    def _update_bullet(self):
        self.bullets.update()
        for bullet in self.bullets:
            bullet.draw_bullet()

        for b in self.bullets.copy():
            if b.rect.bottom < b.rect.height+1:  # 避免消灭窗口外的敌人
                self.bullets.remove(b)
        # print("Nuber of bullets: " + str(len(self.bullets)))

    def _check_collisions(self):
        conllisions = pygame.sprite.groupcollide(self.bullets, self.ufo_fleet, True, True)
        if conllisions:
            for ufo in conllisions.values():
                self.score_button.score += len(ufo)

        score_str = "{:,}".format(self.score_button.score*550)
        self.score_button.crate_text_image(score_str)

    def _new_wave(self):
        if not self.ufo_fleet:
            self.bullets.empty()
            self._create_ufo_fleet()

    def _update_ufo_fleet(self):
        self.ufo_fleet.update()

    def _fire(self):
        bullet = Bullet(self)
        self.bullets.add(bullet)

    def _create_ufo_fleet(self):
        ufo_sample = Ufo(self, 0, 0)
        for n in range(10):
            ufo_line1 = Ufo(self, n*ufo_sample.rect.width*1.5+10, 0)
            ufo_line2 = Ufo(self, n*ufo_sample.rect.width*1.5+10, ufo_sample.rect.height)
            # ufo_line1 = Ufo(self, n*ufo_sample.rect.width*1.5+10, 0-ufo_sample.rect.height*2)
            # ufo_line2 = Ufo(self, n*ufo_sample.rect.width*1.5+10, 0-ufo_sample.rect.height
            self.ufo_fleet.add(ufo_line1)
            self.ufo_fleet.add(ufo_line2)

    def _check_ship_collision(self):
        if pygame.sprite.spritecollideany(self.ship, self.ufo_fleet):
            print("collision:", self.statistics.ships_left)
            self.statistics.ships_left -= 1
            if self.statistics.ships_left == 0:
                self.runing = False
                self.pause = False
                self.statistics.reset()
                pygame.mouse.set_visible(True)
            else:
                sleep(1)
            self._restart()

    def _restart(self):
        self.bullets.empty()
        self.ufo_fleet.empty()
        self._create_ufo_fleet()

        self.ship.rect.x = 600
        self.ship.rect.y = 800 - self.ship.rect.height
        self.ship.x = float(self.ship.rect.x)
        self.ship.y = float(self.ship.rect.y)

    def _check_start_button(self):
        if not self.runing:
            self.start_button.draw()

    def _check_mouse_to_start(self, pos):
        if self.start_button.rect.collidepoint(pos) and not self.runing:
            self.runing = True
            self.pause = False
            pygame.mouse.set_visible(False)


if __name__ == '__main__':
    game = Game()
    game.run()
