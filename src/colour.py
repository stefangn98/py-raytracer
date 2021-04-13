from .vector3 import Vector3
from typing import Optional


class Colour(Vector3):
    """An alias for Vector3 that holds an RGB colour"""

    @classmethod
    def from_hex(cls, code: str = "#FFFFFF") -> 'Optional[Colour]':
        """Convert a hexadecimal colour code to a colour object"""
        r = int(code[1:3], 16) / 255.0
        g = int(code[3:5], 16) / 255.0
        b = int(code[5:7], 16) / 255.0
        return cls(r, g, b)
