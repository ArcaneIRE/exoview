from math import *
import json
import astropy.units as u
from astropy.coordinates import SkyCoord
from astroquery.gaia import Gaia
from astroquery.ipac.nexsci.nasa_exoplanet_archive import NasaExoplanetArchive as nea

def galacticToCartesian(gLat, gLong, dist):
    """
    Convert Galactic coordinates to Cartesian coordinates.    
    gLat: Galactic latitude in degrees
    gLong: Galactic longitude in degrees
    dist: Distance
    """
    
    # Convert angles from degrees to radians
    gLongRad = deg_to_rad(gLong) 
    gLatRad = deg_to_rad(gLat)

    # Cartesian coordinates conversion
    x = dist * cos(gLatRad) * cos(gLongRad)
    y = dist * cos(gLatRad) * sin(gLongRad)
    z = dist * sin(gLatRad)
    
    return (x, y, z)

Gaia.ROW_LIMIT = 1000
coord = SkyCoord(ra=280, dec=-60, unit=(u.degree, u.degree), frame='icrs')
# j = Gaia.cone_search_async(coord, radius=u.Quantity(1.0, u.deg),dump_to_file=True, output_format='csv')

query = """
SELECT 
    distance_gspphot,
    ra,
    dec,
    l,
    b
FROM 
    "gaiadr3"."gaia_source"
WHERE 
    distance_gspphot BETWEEN 580 AND 660
    AND ra BETWEEN 17.4955 AND 21.4955
    AND dec BETWEEN -47.7883 AND -43.7883
"""

j = Gaia.launch_job(query, dump_to_file=True, output_format='csv')
r = j.get_results()

pl_table = "ps"
pl_select = "DISTINCT pl_name, ra, dec, sy_dist"
pl_where = "pl_name = 'Kepler-22 b'"

j_pl = nea.query_criteria(table=pl_table, select=pl_select, where=pl_where)

## add cartiesian conv

print(r)
print(j_pl)

print(type(r))
print(type(j_pl))

r.write("a.csv", overwrite=True)
j_pl.write("b.csv", overwrite=True)

