import math
import random


def random_point() -> tuple[float, float]:
    """
    Pick a mathematically sane random circle around the point of (0, 0) with a radius of 1.

    :return: a tuple with either X and Y of the point
    """
    t = 2*math.pi*random()
    u = random()+random()
    u = 2-u if u > 1 else u

    return [r*math.cos(t), r*math.sin(t)]



