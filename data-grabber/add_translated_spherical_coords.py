from astropy.table import Table
from coord_operations import cartesian_to_galactic


def add_XO_origin_galactics(planet: Table, stars: Table):
    """
    Take the cartesian coords relative to the exoplanet and add 
    their spherical representations
    """
    planet.add_column(0.0, name='xo_as_origin_latitude')
    planet.add_column(0.0, name='xo_as_origin_longitude')
    planet.add_column(0.0, name='xo_as_origin_distance')

    stars.add_column(0.0, name='xo_as_origin_latitude')
    stars.add_column(0.0, name='xo_as_origin_longitude')
    stars.add_column(0.0, name='xo_as_origin_distance')
    for star in stars:
        x = star['xo_as_origin_x']
        y = star['xo_as_origin_y']
        z = star['xo_as_origin_z']
        lat, long, dist = cartesian_to_galactic(x, y, z)
        star['xo_as_origin_latitude'] = lat
        star['xo_as_origin_longitude'] = long
        star['xo_as_origin_distance'] = dist
