import math

def app_to_abs(app:float, dist:float) -> float:
    """
    Convert apparent mag to abs mag

    :param app: apparent magnitude
    :type app: float
    :param dist: distance in parsecs
    :type dist: float
    :return: absolute magnitude
    :rtype: float
    """
    return (app - (5*math.log10(dist/10)))

def abs_to_app(abs:float, dist:float) -> float:
    """
    Convert absolute mag to apparent mag

    :param abs: absolute magnitude
    :type abs: float
    :param dist: distance to star
    :type dist: float
    :return: apparent magnitude
    :rtype: float
    """
    return abs + (5*math.log10(dist/10))
