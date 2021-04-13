from .vector3 import Vector3

"""
    These utility functions can be used in cases
    where operator overloading is not implemented
    in the Vector3 class. They do the same as
    __add__, __sub__, __mul__ and __truediv__
"""


def AddVectors(v1: Vector3, v2: Vector3) -> Vector3:
    return Vector3(v1.x() + v2.x(), v1.y() + v2.y(), v1.z() + v2.z())


def SubVectors(v1: Vector3, v2: Vector3) -> Vector3:
    return Vector3(v1.x() - v2.x(), v1.y() - v2.y(), v1.z() - v2.z())


def MulVectors(v1: Vector3, v2: Vector3) -> Vector3:
    return Vector3(v1.x() * v2.x(), v1.y() * v2.y(), v1.z() * v2.z())


def MulVectorByNum(v1: Vector3, num: float) -> Vector3:
    return Vector3(v1.x() * num, v1.y() * num, v1.z() * num)


def DotProduct(v1: Vector3, v2: Vector3) -> float:
    return v1.x() * v2.x() + v1.y() * v2.y() + v1.z() * v2.z()


def CrossProduct(v1: Vector3, v2: Vector3) -> Vector3:
    return Vector3(v1.y() * v2.z() - v1.z() * v2.y(),
                   v1.z() * v2.x() - v1.x() * v2.z(),
                   v1.x() * v2.y() - v1.y() * v2.x())


def NormalizeVector(v1: Vector3) -> Vector3:
    return v1.div(v1.magnitude())
