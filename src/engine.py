from .sphere import Sphere
from .vector3 import Vector3
from . import constants
from .scene import Scene
from .image import Image
from .ray import Ray
from .point import Point
from .colour import Colour

from typing import Optional


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
        hit_normal = obj.normal(hit_pos)
        colour += self.colour_at(obj, hit_pos, hit_normal, scene)

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

    def colour_at(self, hit_object: Optional[Sphere], hit_position: Point, hit_normal: Vector3,  scene: Scene) -> Colour:
        """This function calculates the colour of an object at a position of a ray hit"""

        obj_material = hit_object.material
        obj_colour = obj_material.colour_at(hit_position)

        to_cam = scene.camera - hit_position
        colour = obj_material.ambient * Colour.from_hex("#000000")

        # Loop over every light in the scene and calculate the shading
        for light in scene.lights:
            to_light = Ray(hit_position, light.origin - hit_position)

            # Apply Lambert shading (diffuse)
            # Use max() to avoid getting a negative value as we do not want
            # to subtract from the colour
            # Check the wikipedia article to learn why we use the dot product
            colour += obj_colour * obj_material.diffuse * \
                max(hit_normal.dot(to_light.direction), 0)

            # Apply Blinn-Phong shading (specular)

            # H - a normalized vector halfway between
            # the viewer (to_cam) and the light source (to_light)
            H = (to_light.direction + to_cam).normalize()
            colour += light.colour * obj_material.specular * \
                max(hit_normal.dot(H), 0) ** 50

        return colour
