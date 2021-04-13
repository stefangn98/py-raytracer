from .colour import Colour
from .point import Point


class Material:
    """A class that describes a material"""

    def __init__(self, ambient_coef: float, diffuse_coef: float, specular_coef: float, colour: Colour = Colour.from_hex("#FFFFFF")) -> None:
        self.ambient = ambient_coef
        self.diffuse = diffuse_coef
        self.specular = specular_coef
        self.colour = colour

    def colour_at(self, hit_position: Point) -> Colour:
        return self.colour
