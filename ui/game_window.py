from typing import Tuple

import pygame

from cell import Cell
from game_state import GameState
from ui import color


class GameWindow:
    def __init__(self, width: int = 800, height: int = 600, cell_size: int = 3, title: str = 'The Game of LIFE'):
        self.width, self.height = width, height
        self.center_x, self.center_y = self.width // 2, self.height // 2
        self.cell_size = cell_size
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(title)

    def cell_to_screen_coordinates(self, cell: Cell) -> Tuple[float, float]:
        return self.center_x + (cell.get_x() * self.cell_size), self.center_y + (cell.get_y() * self.cell_size)

    def draw(self, game_state: GameState):
        self.screen.fill((0, 0, 0))

        living_cells = game_state.get_current_generation().get_living_cells()
        for cell in living_cells:
            coordinates = self.cell_to_screen_coordinates(cell)
            pygame.draw.circle(self.screen, color.WHITE.get_value(), coordinates, self.cell_size)

        pygame.display.flip()
        pygame.time.Clock().tick(60)
