import sys

import pygame

from core.game_state import GameState
from ui.cell import CellSettings, CellStyle
from ui.common import Colors
from ui.game_window import GameWindow


class Game:
    def __init__(self):
        pygame.init()
        self.game_window = GameWindow(cell_settings=CellSettings(7, CellStyle.SQUARE, Colors.WHITE))
        self.running = True
        self.game_state = GameState()

    def run(self):
        while self.running:
            self.process_events()
            self.game_state.calculate()
            self.game_window.draw(self.game_state)
        pygame.quit()
        sys.exit()

    def process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
