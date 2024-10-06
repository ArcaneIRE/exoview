import magnitude
from astropy.table import Table

def calculate_real_brightness(stars:Table):
    """
    Add the absolute brightness of the star to the stars table

    :param stars: table of nearby stars
    :type star: Table
    """
    stars.add_column(0.0, name='absolute_magnitude')

    for star in stars:
        # get abs mag
        # get app mag from star
        abs = magnitude.app_to_abs(star['phot_g_mean_mag'], star['distance_parsecs'])
        star['absolute_magnitude'] = abs
