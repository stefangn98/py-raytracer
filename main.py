"""
    =======================================================
    || Code Written By: Stefan Nikolov                   ||
    || Date: 10.04.2021                                  ||
    || A simple ray tracing simulation done in           ||
    || Python 3.9, done only with standard libraries.    ||
    || Inspiration by: Ray Tracer in Python by ArunRocks ||
    || And: Ray Tracing in One Weekend by Peter Shirley  ||
    =======================================================
"""

from src.colour import Colour
from src.point import Point
from src.vector3 import Vector3
from src.image import Image
from src.sphere import Sphere
from src.ray import Ray
from src.scene import Scene
from src.engine import Engine
from src.light import Light
from src.material import Material
import src.constants as constants

import argparse
from typing import NoReturn


def init_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(usage="%(prog)s -f [FILE]",
                                     description="Create a .ppm ray traced image and output it to [FILE].")
    parser.add_argument("-file", type=str, help="name of the output file.")
    return parser


def main() -> NoReturn:
    parser = init_parser()
    args = parser.parse_args()

    if not args.file:
        file_path = "image.ppm"
    elif args.file.endswith(".ppm"):
        file_path = args.file
    else:
        raise TypeError("Input file must have .ppm extension.")

    # img = Image(constants.WIDTH, constants.HEIGHT)
    camera = Vector3(0, 0, -1)
    objects = [Sphere(Point(0, 0, 1), 0.5, Material(
        0.05, 1.0, 1.0, Colour.from_hex("#FF0000")))]

    lights = [Light(Point(1.5, -0.5, -10.0), Colour.from_hex("#00FFFF"))]
    scene = Scene(constants.WIDTH, constants.HEIGHT, camera, objects, lights)
    engine = Engine()

    img = engine.render(scene)

    with open(file_path, "w") as my_file:
        img.write_to_file(my_file)

    print("Done")


if __name__ == "__main__":
    main()


# Traffic lights
# objects = [Sphere(Point(0, -0.5, 1), 0.2, Colour.from_hex("#FF0000")),
#                Sphere(Point(0, 0, 1), 0.2, Colour.from_hex("#FFFF00")),
#                Sphere(Point(0, 0.5, 1), 0.2, Colour.from_hex("#00FF00"))]

# Set each pixel to a random colour
    # for i in range(constants.WIDTH):
    #     for j in range(constants.HEIGHT):
    #         img.set_pixel(i, j, Colour(random.uniform(0.0, 1.0),
    #                       random.uniform(0.0, 1.0), random.uniform(0.0, 1.0)))
