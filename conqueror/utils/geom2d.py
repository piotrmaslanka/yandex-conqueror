import math


def degrees_to_kilometers_lat(degrees: int) -> float:
    """
    Convert degrees of longitude into kilometres
    :param degrees:
    :return:
    """

    return (63567523 * degrees / 90) / 1000


def degrees_to_kilometers_lon(degrees: float, degrees_lat: float) -> float:
    return degrees * 111.320 * math.cos(degrees_lat)


def kilometers_to_degrees_lon(kilometres: float, degrees_lat: float) -> float:
    return kilometres / 111.320 / math.cos(degrees_lat)


def kilometers_to_degrees_lat(kilometres: float) -> float:
    """
    Convert kilometres of longitude into degrees

    :param degrees:
    :return:
    """

    return kilometres * 90 * 1000 / 63567523
