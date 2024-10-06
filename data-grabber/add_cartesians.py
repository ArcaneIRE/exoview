from coord_operations import galactic_to_cartesian
from astropy.table import Table


def add_cartesians(planet, stars):
    add_cartesians_to_planet(planet)
    add_cartesians_to_stars(stars)


def add_cartesians_to_planet(planet: Table):
    # planet.remove_column('sky_coord')
    planet.rename_column('sy_dist', 'distance_parsecs')
    planet.rename_column('glon', 'galactic_longitude')
    planet.rename_column('glat', 'galactic_latitude')
    planet.add_column(0.0, name='cart_x')
    planet.add_column(0.0, name='cart_y')
    planet.add_column(0.0, name='cart_z')

    x, y, z = galactic_to_cartesian(
        planet['galactic_longitude'], planet['galactic_latitude'], planet['distance_parsecs'])
    planet['cart_x'] = x
    planet['cart_y'] = y
    planet['cart_z'] = z


def add_cartesians_to_stars(stars: Table):
    stars.rename_column('l', 'galactic_longitude')
    stars.rename_column('b', 'galactic_latitude')
    stars.rename_column('distance_gspphot', 'distance_parsecs')
    stars.add_column(0.0, name='cart_x')
    stars.add_column(0.0, name='cart_y')
    stars.add_column(0.0, name='cart_z')

    for star in stars:
        x, y, z = galactic_to_cartesian(
            star['galactic_longitude'], star['galactic_latitude'], star['distance_parsecs'])
        star['cart_x'] = x
        star['cart_y'] = y
        star['cart_z'] = z
