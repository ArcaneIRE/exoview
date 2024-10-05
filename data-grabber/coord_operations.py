from math import radians, cos, sin


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


def get_translation_diffs(x: float, y: float, z: float) -> dict[str, float]:
    return {
        'x_diff': -x,
        'y_diff': -y,
        'z_diff': -z
    }
