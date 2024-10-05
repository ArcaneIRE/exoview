from astroquery.gaia import Gaia
from astroquery.ipac.nexsci.nasa_exoplanet_archive import NasaExoplanetArchive as nea

Gaia.ROW_LIMIT = 1000

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

job = Gaia.launch_job(query, dump_to_file=True, output_format='csv')
stars = job.get_results()

pl_table = "ps"
pl_select = "DISTINCT pl_name, ra, dec, sy_dist"
pl_where = "pl_name = 'Kepler-22 b'"

planets = nea.query_criteria(table=pl_table, select=pl_select, where=pl_where)

# Write
stars.write("stars.csv", overwrite=True)
planets.write("planets.csv", overwrite=True)
