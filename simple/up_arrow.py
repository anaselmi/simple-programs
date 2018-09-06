def parser(xpr: str):
    """ Parses an up-arrow expression into a tuple containing the parsed expression.
    Notes:
        ↑ is used to denote the up-arrow.

    :param str xpr: Expression. Must be an int, n amount of arrows, and an int, separated by spaces.
    :return tuple: Parsed expression, represented by three numbers.
                   0) int a.
                   1) int arrow. The amount of arrows.
                   2) int b. The amount of iterations.
    """
    xpr = xpr.split(" ")
    return int(xpr[0]), len(xpr[1]), int(xpr[2])


def calc(a, arrow, b):
    assert(arrow >= 0 and b >= 0)
    if arrow == 0:
        return a*b
    if b == 0:
        return 1
    return calc(a, arrow-1, calc(a, arrow, b-1))


def up_arrow(xpr: str):
    a, arrow, b = parser(xpr)
    return calc(a, arrow, b)
