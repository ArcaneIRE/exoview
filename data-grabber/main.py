from get_random_exoplanets import get_random_exoplanets
from get_rand_stars import get_stars
from write_tables import write_tables

planets = get_random_exoplanets(5)
for planet in planets:
    stars = get_stars(planet)
    # add_cartesians(planet, stars)
    # add_XO_origin_cartesians(planet, stars)
    # add_XO_origin_galactics(planet, stars)
    # calculate_real_brightness(stars)
    # cull_dim_stars(stars)
    write_tables(planet, stars)
