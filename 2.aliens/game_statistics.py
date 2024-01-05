class GameStatistics:
    def __init__(self, game) -> None:
        self.settings = game.settings
        self.reset()

    def reset(self):
        self.ships_left = self.settings.ship_limit
        self.score = 0
