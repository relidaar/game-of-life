from typing import Set

from core.cell import Cell


class Generation:
    def __init__(self, living_cells: Set[Cell] = None):
        self.living_cells = living_cells if living_cells else set()
        self.checked_free_cells = set()

    def get_living_cells(self, cells: Set[Cell] = None) -> Set[Cell]:
        return self.living_cells if not cells \
            else {cell for cell in cells if cell in self.living_cells}

    def add_cell(self, new_cell: Cell):
        self.living_cells.add(new_cell)

    def calculate_next_generation(self) -> 'Generation':
        next_generation = Generation()
        for living_cell in self.living_cells:
            self.enforce_life_rules(next_generation, living_cell)
        return next_generation

    def enforce_life_rules(self, next_generation: 'Generation', living_cell: Cell):
        neighbors = living_cell.get_neighbors()
        living_neighbors = self.get_living_cells(neighbors)

        if self.living_cell_will_survive(living_cell):
            next_generation.add_cell(living_cell)

        free_cells = neighbors.difference(living_neighbors).difference(self.checked_free_cells)
        for free_cell in free_cells:
            if self.new_cell_will_be_born(free_cell):
                next_generation.add_cell(free_cell)
                self.checked_free_cells.add(free_cell)

    def living_cell_will_survive(self, cell: Cell) -> bool:
        neighbors = cell.get_neighbors()
        alive_neighbors = self.get_living_cells(neighbors)
        return 2 <= len(alive_neighbors) <= 3

    def new_cell_will_be_born(self, cell: Cell) -> bool:
        neighbors = cell.get_neighbors()
        alive_neighbors = self.get_living_cells(neighbors)
        return len(alive_neighbors) == 3

    def __eq__(self, other):
        if not isinstance(other, Generation):
            return False
        difference = self.living_cells.difference(other.get_living_cells())
        return len(difference) == 0

    def __hash__(self):
        return hash(self.living_cells)

    def __repr__(self):
        return ' ;'.join([f'({cell.get_y()},{cell.get_x()})'
                          for cell in self.living_cells])
