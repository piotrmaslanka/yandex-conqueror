def degrees_to_kilometres(degrees: int) -> float:
    """
    Convert degrees of longitude into kilometres
    :param degrees:
    :return:
    """

    return (63567523 * degrees / 90) / 1000


def kilometres_to_degrees(kilometres: float) -> float:
    """
    Convert kilometres of longitude into degrees
    :param degrees:
    :return:
    """

    return kilometres * 90 * 1000 / 63567523
