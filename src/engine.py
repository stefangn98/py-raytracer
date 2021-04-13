from . import constants
from .scene import Scene
from .image import Image
from .ray import Ray
from .point import Point
from .colour import Colour


class Engine:
    """Render objects in to a scene using ray tracing"""

    def render(self, scene: Scene) -> Image:
        aspect_ratio = constants.ASPECT_RATIO
        x0, x1, y0, y1 = -1.0, 1.0, -1.0 / aspect_ratio, 1.0 / aspect_ratio
        x_step = (x1 - x0) / (scene.width - 1)
        y_step = (y1 - y0) / (scene.height - 1)

        img = Image(scene.width, scene.height)

        for i in range(scene.height):
            y = y0 + i * y_step
            for j in range(scene.width):
                x = x0 + j * x_step
                ray = Ray(scene.camera, Point(x, y) - scene.camera)
                img.set_pixel(j, i, self.ray_trace(ray, scene))
        return img

    def ray_trace(self, ray: Ray, scene: Scene):
        """Perform the ray tracing operation"""
        dist, obj = self.hit(ray, scene)
        colour = Colour(0.0, 0.0, 0.0)

        if obj is None:
            return colour

        hit_pos = ray.origin + ray.direction * dist
        colour += self.colour_at(obj, hit_pos, scene)

        return colour

    # Technically "object_hit" can be anything so it's hard to type hint what it should be

    def hit(self, ray: Ray, scene: Scene):
        dist, obj = 0, None

        for item in scene.objects:
            temp_d = item.intersect(ray)
            if temp_d is not None and (obj is None or temp_d < dist):
                dist = temp_d
                obj = item
        return (dist, obj)

    def colour_at(self, hit_object, hit_position, scene: Scene):
        return hit_object.material
