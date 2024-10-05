from astroquery.ipac.nexsci.nasa_exoplanet_archive import NasaExoplanetArchive
import astropy
import numpy as np


def get_random_exoplanets(quantity=1) -> astropy.table.QTable:
    random_pl_names = _get_random_exoplanet_names(quantity)
    name_conditions = [f"pl_name='{
        row["pl_name"]}'" for row in random_pl_names]
    results = NasaExoplanetArchive.query_criteria(
        table="ps",
        select="distinct pl_name, ra, dec, sy_dist",
        cache=True,
        where=" OR ".join(name_conditions)
    )
    return results


def _get_random_exoplanet_names(quantity=1):
    results = NasaExoplanetArchive.query_criteria(
        table="ps",
        cache=True,
        select="distinct pl_name",
    )
    random_indices = np.random.choice(len(results), quantity, replace=False)
    return results[random_indices]
