from typing import Tuple


class Color:
    def __init__(self, red, green, blue):
        self.red = red
        self.green = green
        self.blue = blue

    def get_value(self) -> Tuple[int, int, int]:
        return self.red, self.green, self.blue


WHITE = Color(255, 255, 255)
BLACK = Color(0, 0, 0)
GRAY = Color(200, 200, 200)
RED = Color(255, 0, 0)
GREEN = Color(0, 255, 0)
