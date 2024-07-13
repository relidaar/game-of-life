from typing import Set


class Cell:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def get_neighbors(self) -> Set['Cell']:
        result = set()
        # top left
        result.add(Cell(self.x - 1, self.y - 1))
        # top middle
        result.add(Cell(self.x, self.y - 1))
        # top right
        result.add(Cell(self.x + 1, self.y - 1))

        # left
        result.add(Cell(self.x - 1, self.y))
        # right
        result.add(Cell(self.x + 1, self.y))

        # bottom left
        result.add(Cell(self.x - 1, self.y + 1))
        # bottom middle
        result.add(Cell(self.x, self.y + 1))
        # bottom right
        result.add(Cell(self.x + 1, self.y + 1))
        return result

    def get_x(self) -> int:
        return self.x

    def get_y(self) -> int:
        return self.y

    def __eq__(self, other):
        return isinstance(other, Cell) \
            and other.get_x() == self.x \
            and other.get_y() == self.y

    def __hash__(self):
        return hash((self.x, self.y))

    def __repr__(self):
        return f'({self.x}, {self.y})'
