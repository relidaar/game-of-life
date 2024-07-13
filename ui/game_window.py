import pygame

from core.game_state import GameState
from ui.cell import create_drawable_cell, CellSettings, CellStyle
from ui.common import Colors


class GameWindow:
    def __init__(self, width: int = 800, height: int = 600,
                 cell_settings: CellSettings = CellSettings(5, CellStyle.SQUARE, Colors.WHITE),
                 title: str = 'The Game of LIFE'):
        self.width, self.height = width, height
        self.screen_center = self.width // 2, self.height // 2
        self.cell_settings = cell_settings
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(title)

    def draw(self, game_state: GameState):
        self.screen.fill((0, 0, 0))

        cells = [create_drawable_cell(cell, self.screen_center, self.cell_settings)
                 for cell in game_state.get_current_generation().get_living_cells()]
        for cell in cells:
            cell.draw(self.screen)

        pygame.display.flip()
        pygame.time.Clock().tick(60)
