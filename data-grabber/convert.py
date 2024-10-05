from math import radians, cos, sin

def galacticToCartesian(gLat, gLong, dist):
    """
    Convert Galactic coordinates to Cartesian coordinates.    
    gLat: Galactic latitude in degrees
    gLong: Galactic longitude in degrees
    dist: Distance
    """
    
    gLat = float(gLat)
    gLong = float(gLong)
    dist = float(dist)
    
    # Convert angles from degrees to radians
    gLongRad = radians(gLong) 
    gLatRad = radians(gLat)

    # Cartesian coordinates conversion
    x = dist * cos(gLatRad) * cos(gLongRad)
    y = dist * cos(gLatRad) * sin(gLongRad)
    z = dist * sin(gLatRad)
    
    return (x, y, z)

