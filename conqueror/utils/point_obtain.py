import math
from random import random


def random_point(r: float) -> tuple[float, float]:
    """
    Pick a mathematically sane random circle around the point of (0, 0) with a radius of 1.

    :param r: radius
    :return: a tuple with either X and Y of the point
    """
    t = 2*math.pi*random()
    u = random()+random()
    v = 2-u if u > 1 else u

    return [v*math.cos(t)*r, v*math.sin(t)*r]




