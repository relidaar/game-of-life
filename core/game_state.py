import random
from typing import List

from core.cell import Cell
from core.generation import Generation


class GameState:
    def __init__(self, field_width: int = 30, field_height: int = 30):
        self.generation_count = 1
        self.current_generation = GameState.generate_initial_generation(field_width, field_height)

    def cells_exist(self):
        return len(self.current_generation.get_living_cells()) > 0

    def calculate(self):
        self.generation_count += 1
        next_generation = self.current_generation.calculate_next_generation()
        self.current_generation = next_generation

    @staticmethod
    def generate_initial_generation(width: int, height: int) -> Generation:
        assert 1 <= width <= 100, 'Initial field width must be in range [1, 100]'
        assert 1 <= height <= 100, 'Initial field height must be in range [1, 100]'

        cols, rows = GameState.field_size_to_coordinates(width), GameState.field_size_to_coordinates(height)
        living_cells = set()
        for row in rows:
            for col in cols:
                if random.random() < 0.5:
                    living_cells.add(Cell(col, row))
        return Generation(living_cells)

    @staticmethod
    def field_size_to_coordinates(n: int) -> List[int]:
        assert n > 0
        if n == 1:
            return [0]
        center = n // 2
        return [i for i in range(-center, n - center)]

    def get_current_generation(self):
        return self.current_generation
