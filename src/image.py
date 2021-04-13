from io import TextIOWrapper
from .colour import Colour
from typing import NoReturn


class Image:
    def __init__(self, width: int, height: int) -> NoReturn:
        self.width = width
        self.height = height
        self.pixels = [[None for _ in range(width)] for _ in range(height)]

    def set_pixel(self, row: int, col: int, colour: Colour) -> NoReturn:
        """Set the pixel of an image"""
        self.pixels[col][row] = colour

    def write_to_file(self, file: TextIOWrapper) -> NoReturn:
        """Write the contents of the Image to a file"""

        file.write(f"P3 {self.width} {self.height}\n255\n")
        whole = self.width * self.height
        for row in self.pixels:
            for col in row:
                curr = self.pixels.index(row) * len(row) + row.index(col)
                file.write(
                    f"{convert_to_byte(col.x())} {convert_to_byte(col.y())} {convert_to_byte(col.z())} ")
            file.write("\n")


def convert_to_byte(val: float) -> int:
    """Convert a floating point number in [0, 1] to a byte [0, 255]"""
    return round(max(min(val*255, 255), 0))
