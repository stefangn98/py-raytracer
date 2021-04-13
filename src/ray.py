from .point import Point
from .vector3 import Vector3
from typing import NoReturn


class Ray:
    """A ray that has an origin and direction"""

    def __init__(self, origin: Point, direction: Vector3) -> NoReturn:
        self.origin = origin
        self.direction = direction.normalize()
