from astroquery.gaia import Gaia
from astroquery.ipac.nexsci.nasa_exoplanet_archive import NasaExoplanetArchive as nea

def get_stars(planet):
    """Get a volume of stars around a planet"""
    ## print(planet['pl_name'])
    ## print(planet['ra'])
    ## print(planet['dec'])
    ## print(planet['sy_dist'])

    ra = float(planet['ra'].value)
    dec = float(planet['dec'].value)
    pc = float(planet['sy_dist'].value)

    query = f"""
    SELECT 
        distance_gspphot,
        ra,
        dec,
        l,
        b,
        pseudocolour
    FROM 
        "gaiadr3"."gaia_source"
    WHERE 
        distance_gspphot BETWEEN {pc-40} AND {pc+40}
        AND ra BETWEEN {ra-2} AND {ra+2}
        AND dec BETWEEN {dec-2} AND {dec+2}
    """
    print(query)
    j = Gaia.launch_job(query)
    r = j.get_results()
    # print(r)
    return r
