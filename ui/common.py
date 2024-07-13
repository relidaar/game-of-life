from abc import ABC, abstractmethod

from pygame import Surface, Color


class Colors:
    WHITE = Color(255, 255, 255)
    BLACK = Color(0, 0, 0)
    GRAY = Color(200, 200, 200)
    RED = Color(255, 0, 0)
    GREEN = Color(0, 255, 0)


class Drawable(ABC):
    @abstractmethod
    def draw(self, surface: Surface):
        pass
