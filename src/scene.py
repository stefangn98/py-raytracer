from typing import NoReturn
from .point import Point


class Scene:
    """A scene class that holds all objects and a camera"""

    def __init__(self,  width: int, height: int, camera: Point, objects: list, lights: list) -> NoReturn:
        self.width = width
        self.height = height
        self.camera = camera
        self.objects = objects
        self.lights = lights
