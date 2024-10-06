from math import degrees, radians, cos, sin, sqrt, atan2, acos


def galactic_to_cartesian(galactic_lat: float, galactic_long: float, dist: float) -> tuple[float, float, float]:
    """
    Convert Galactic coordinates to Cartesian coordinates.    
    gLat: Galactic latitude in degrees
    gLong: Galactic longitude in degrees
    dist: Distance
    """
    # Convert angles from degrees to radians
    galactic_lat_rad = radians(galactic_lat)
    galactic_long_rad = radians(galactic_long)

    # Cartesian coordinates conversion
    x = dist * cos(galactic_lat_rad) * cos(galactic_long_rad)
    y = dist * cos(galactic_lat_rad) * sin(galactic_long_rad)
    z = dist * sin(galactic_lat_rad)

    return (x, y, z)


def cartesian_to_galactic(x: float, y: float, z: float) -> tuple[float, float, float]:
    """
    Convert Cartesian coordinates to Galactic coordinates    
    x: x cartesian coordinate (in parsecs?)
    y: x cartesian coordinate (in parsecs?)
    z: y cartesian coordinate (in parsecs?)

    Useful source: https://blog.demofox.org/2013/10/12/converting-to-and-from-polar-spherical-coordinates-made-easy/
    """
    x = float(x)
    y = float(y)
    z = float(z)
    x2 = x * x
    y2 = y * y
    z2 = z * z
    distance = sqrt(x2 + y2 + z2)  # radius
    longitude = atan2(y, x)  # theta
    latitude = acos(z / distance)  # phi
    return degrees(latitude), degrees(longitude), degrees(distance)


def get_translation_diffs(x: float, y: float, z: float) -> dict[str, float]:
    return {
        'x_diff': -x,
        'y_diff': -y,
        'z_diff': -z
    }
