# get 100 random planets
# get a ton (1000) stars around each planet (+- 2 deg of ra and dec and 50 pc)
# transform and add planet and star data
# make a folder for each planet
# write a csv per planet to each folder

from astroquery.gaia import Gaia
from astroquery.ipac.nexsci.nasa_exoplanet_archive import NasaExoplanetArchive as nea
from get_random_exoplanets import *
from get_rand_stars import *
import astropy.table
from write_tables

# Get a bunch of planets
planets = get_random_exoplanets(5)
for planet in planets:
    stars = get_stars(planet)
    # add_cartesians(planet, stars)
    # add_XO_origin_cartesians(planet, stars)
    # add_XO_origin_galactics(planet, stars)
    # calculate_real_brightness(stars)
    # cull_dim_stars(stars)
    write_tables(planet, stars)
