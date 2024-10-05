from astroquery.ipac.nexsci.nasa_exoplanet_archive import NasaExoplanetArchive
from astropy.table import QTable
import numpy as np
import math


def get_random_exoplanets(quantity: int = 1) -> QTable:
    """Gets the pl_name, ra, dec, sy_dist of a given number of exoplanets"""
    name_conditions: list = []
    for row in _get_random_exoplanet_names(quantity):
        name_conditions.append(f"pl_name='{row["pl_name"]}'")
    results = NasaExoplanetArchive.query_criteria(
        table="ps",
        select="distinct pl_name, ra, dec, sy_dist, glat, glon",
        cache=True,
        where=" OR ".join(name_conditions)
    )

    results.add_index('pl_name')
    
    # Check for null rows and remove them
    for pl in results:
        if math.isnan(float(pl['sy_dist'].value)):
            print(f"pl {pl['pl_name']} sy_dist was Nan")
            results.remove_row(results.loc[pl['pl_name']].index)

    print("===")
    return results


def _get_random_exoplanet_names(quantity: int = 1) -> QTable:
    """Gets the pl_names of a given number of random exoplanets"""
    results = NasaExoplanetArchive.query_criteria(
        table="ps",
        cache=True,
        select="distinct pl_name",
    )
    random_indices = np.random.choice(len(results), quantity, replace=False)
    return results[random_indices]
