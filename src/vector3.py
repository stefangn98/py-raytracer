from typing import Optional
from math import sqrt


class Vector3(object):
    """A multipurpose thee component vector class"""

    def __init__(self, x: float = 0.0, y: float = 0.0, z: float = 0.0) -> None:
        self.__x = float(x)
        self.__y = float(y)
        self.__z = float(z)

    def x(self) -> float:
        """The x component of the vector"""
        return self.__x

    def y(self) -> float:
        """The y component of the vector"""
        return self.__y

    def z(self) -> float:
        """The z component of the vector"""
        return self.__z

    def __str__(self) -> str:
        """Print the vector"""
        return(f"({self.x()}, {self.y()}, {self.z()})")

    def dot(self, other: 'Optional[Vector3]') -> float:
        """The dot product of two vectors"""
        assert isinstance(other, Vector3)
        return self.x() * other.x() + self.y() * other.y() + self.z() * other.z()

    def magnitude(self) -> float:
        """The magnitude of a vector"""
        return sqrt(self.dot(self))

    def cross(self, other: 'Optional[Vector3]') -> 'Optional[Vector3]':
        """The cross product of two vectors"""
        assert isinstance(other, Vector3)
        return Vector3(self.y() * other.z() - self.z() * other.y(),
                       self.z() * other.x() - self.x() * other.z(),
                       self.x() * other.y() - self.y() * other.x())

    def normalize(self) -> 'Optional[Vector3]':
        return self / self.magnitude()

    # The following functions are required for operator overloading
    def __add__(self, other: 'Optional[Vector3]') -> 'Optional[Vector3]':
        return Vector3(self.x() + other.x(),
                       self.y() + other.y(),
                       self.z() + other.z())

    def __sub__(self, other: 'Optional[Vector3]') -> 'Optional[Vector3]':
        return Vector3(self.x() - other.x(),
                       self.y() - other.y(),
                       self.z() - other.z())

    def __mul__(self, other) -> 'Optional[Vector3]':
        assert not isinstance(other, Vector3)
        return Vector3(self.x() * other, self.y() * other, self.z() * other)

    def __rmul__(self, other) -> 'Optional[Vector3]':
        return self.__mul__(other)

    # This is only supported in Python 3 (with special imports in Python 2)
    def __truediv__(self, other) -> 'Optional[Vector3]':
        assert not isinstance(other, Vector3)
        return Vector3(self.x() / other, self.y() / other, self.z() / other)
