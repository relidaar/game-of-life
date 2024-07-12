import random
from typing import List

from cell import Cell
from generation import Generation


class GameState:
    def __init__(self, field_width: int = 10, field_height: int = 10, initial_count: int = 70):
        self.generation_count = 1
        self.current_generation = GameState.generate_initial_generation(field_width, field_height, initial_count)

    def cells_exist(self):
        return len(self.current_generation.get_living_cells()) > 0

    def calculate(self):
        self.generation_count += 1
        next_generation = self.current_generation.calculate_next_generation()
        self.current_generation = next_generation

    @staticmethod
    def generate_initial_generation(width: int, height: int, initial_count: int) -> Generation:
        assert 1 <= width <= 100, 'Initial field width must be in range [1, 100]'
        assert 1 <= height <= 100, 'Initial field height must be in range [1, 100]'
        field_square = width * height
        assert 1 <= initial_count <= field_square, f'Initial number of cells must be in range [1, {field_square}]'

        cols, rows = GameState.field_size_to_coordinates(width), GameState.field_size_to_coordinates(height)
        possible_cells = set()
        for row in rows:
            for col in cols:
                possible_cells.add(Cell(col, row))

        living_cells = random.sample(tuple(possible_cells), initial_count)
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
