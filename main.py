import json
import astropy.units as u
from astropy.coordinates import SkyCoord
from astroquery.gaia import Gaia
from astroquery.ipac.nexsci.nasa_exoplanet_archive import NasaExoplanetArchive as nea
import convert

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

