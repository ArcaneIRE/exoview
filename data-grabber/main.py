# get 100 random planets
# get a ton (1000) stars around each planet (+- 2 deg of ra and dec and 50 pc)
# transform and add planet and star data
# make a folder for each planet
# write a csv per planet to each folder

from astroquery.gaia import Gaia
from astroquery.ipac.nexsci.nasa_exoplanet_archive import NasaExoplanetArchive as nea
from get_random_exoplanets import *
from get_rand_stars import *
import csv
import astropy.table

# Get a bunch of planets
planets = get_random_exoplanets(5)
points_of_view = []
# Pair up each planet with a table of stars
for planet in planets:
    pov = {
        'planet': planet,
        'stars': get_stars(planet),
    }

for pov in points_of_view:
    # add cartesians relative to earth
    # add translated cartesians with XO as origin
    # get galactic coords with XO as origin
    # calculate "real brightness"
    # remove stars with a brightness above 6.5
    pass

# Write Tables to CSV
for pov in points_of_view:
    # Make planet CSV
    with open("planet.csv", "w") as f:
        fieldnames = planets.colnames
        d_writer = csv.DictWriter(f, fieldnames=fieldnames)
        d_writer.writeheader()
        tb = astropy.table.Table(planets)
        d_writer.writerow(tb[0])

    # Make stars CSV for planet
    r = get_stars(planets[0])
    with open("star.csv", "w") as f:
        fieldnames = r.colnames
        d_writer = csv.DictWriter(f, fieldnames=fieldnames)
        d_writer.writeheader()
        tb = astropy.table.Table(r)
        d_writer.writerows(tb)
