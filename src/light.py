from .point import Point
from .colour import Colour


class Light:
    """A class that represents a light source"""

    def __init__(self, origin: Point, colour: Colour = Colour.from_hex("FFFFFF")) -> None:
        self.origin = origin
        self.colour = colour
