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

# Make planet CSV
with open("planet.csv", "w") as f:
    fieldnames = planets.colnames
    d_writer = csv.DictWriter(f, fieldnames=fieldnames)
    d_writer.writeheader()
    tb = astropy.table.Table(planets)
    d_writer.writerow(tb[0])

# make star CSV for planet
r = get_stars(planets[0])
with open("star.csv", "w") as f:
    fieldnames = r.colnames
    d_writer = csv.DictWriter(f, fieldnames=fieldnames)
    d_writer.writeheader()
    tb = astropy.table.Table(r)
    d_writer.writerows(tb)
