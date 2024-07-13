import enum
from typing import Tuple

import pygame
from pygame import Surface, Color

from core.cell import Cell
from ui.common import Drawable, Colors


class CellStyle(enum.Enum):
    SQUARE = enum.auto()
    CIRCLE = enum.auto()
    TRIANGLE = enum.auto()


class DrawableCellSettings:
    def __init__(self, cell: Cell, screen_center: Tuple[int, int], size: int, color: Color = Colors.WHITE):
        self.cell = cell
        self.size = size
        self.color = color
        self.screen_center = screen_center


class SquareCell(Drawable):
    def __init__(self, settings: DrawableCellSettings):
        self.size, half_size = settings.size, settings.size // 2
        self.x = settings.screen_center[0] + (settings.cell.get_x() * self.size) - half_size
        self.y = settings.screen_center[1] + (settings.cell.get_y() * self.size) - half_size

    def draw(self, surface: Surface):
        pygame.draw.rect(surface, Colors.WHITE, (self.x, self.y, self.size, self.size))


class CircleCell(Drawable):
    def __init__(self, settings: DrawableCellSettings):
        self.size, self.half_size = settings.size, settings.size // 2
        self.x = settings.screen_center[0] + (settings.cell.get_x() * self.size)
        self.y = settings.screen_center[1] + (settings.cell.get_y() * self.size)

    def draw(self, surface: Surface):
        pygame.draw.circle(surface, Colors.WHITE, (self.x, self.y), self.half_size)


class TriangleCell(Drawable):
    def __init__(self, settings: DrawableCellSettings):
        x, y = settings.cell.get_x(), settings.cell.get_y()
        half_size = settings.size // 2
        self.points = [
            # top
            (x, y - half_size),
            # bottom left
            (x - half_size, y + half_size),
            # bottom right
            (x + half_size, y + half_size),
        ]
        self.points = [(settings.screen_center[0] + x, settings.screen_center[1] + y)
                       for x, y in self.points]

    def draw(self, surface: Surface):
        pygame.draw.polygon(surface, Colors.WHITE, self.points)


class CellSettings:
    def __init__(self, size: int, style: CellStyle = CellStyle.SQUARE, color: Color = Colors.WHITE):
        self.size = size
        self.style = style
        self.color = color


def create_drawable_cell(cell: Cell, screen_center: Tuple[int, int], settings: CellSettings):
    cell_style = settings.style
    drawable_settings = DrawableCellSettings(cell, screen_center, settings.size, settings.color)
    if cell_style == CellStyle.SQUARE:
        return SquareCell(drawable_settings)
    elif cell_style == CellStyle.CIRCLE:
        return CircleCell(drawable_settings)
    elif cell_style == CellStyle.TRIANGLE:
        return TriangleCell(drawable_settings)
    else:
        raise Exception('Invalid cell style')
