from .point import Point
from .ray import Ray
from typing import Optional, NoReturn
from math import sqrt


class Sphere:
    """Simple 3D shape composed of center, radius and material"""

    def __init__(self, center: Point, radius: float, mat) -> NoReturn:
        self.center = center
        self.radius = radius
        self.material = mat

    def intersect(self, ray: Ray) -> Optional[float]:
        """Check if a ray intersects with a sphere and return the distance to the point if it does, otherwise return None"""

        sphere_to_ray = ray.origin - self.center
        a = ray.direction.dot(ray.direction)
        b = 2.0 * sphere_to_ray.dot(ray.direction)
        c = sphere_to_ray.dot(sphere_to_ray) - self.radius * self.radius
        discriminant = b * b - 4 * a * c

        if discriminant >= 0:
            t = (-b - sqrt(discriminant)) / 2
            if t > 0:
                return t
        return None

    def normal(self, point: Point):
        """Returns the surface normal to the point on the surface of a sphere"""

        return (point - self.center).normalize()
