from astropy.table import Table


def add_XO_as_origin_cartesians(planet: Table, stars: Table):
    diff_x = -1 * float(planet['cart_x'])
    diff_y = -1 * float(planet['cart_y'])
    diff_z = -1 * float(planet['cart_z'])

    planet.add_column(0.0, name='xo_as_origin_x')
    planet.add_column(0.0, name='xo_as_origin_y')
    planet.add_column(0.0, name='xo_as_origin_z')

    stars.add_column(0.0, name='xo_as_origin_x')
    stars.add_column(0.0, name='xo_as_origin_y')
    stars.add_column(0.0, name='xo_as_origin_z')

    for star in stars:
        star['xo_as_origin_x'] = float(star['cart_x']) + diff_x
        star['xo_as_origin_y'] = float(star['cart_y']) + diff_y
        star['xo_as_origin_z'] = float(star['cart_z']) + diff_z
