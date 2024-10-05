def write_tables(planet, stars):
    pass
    # Make planet CSV
    # with open("planet.csv", "w") as f:
    #     fieldnames = planets.colnames
    #     d_writer = csv.DictWriter(f, fieldnames=fieldnames)
    #     d_writer.writeheader()
    #     tb = astropy.table.Table(planets)
    #     d_writer.writerow(tb[0])

    # # Make stars CSV for planet
    # r = get_stars(planets[0])
    # with open("star.csv", "w") as f:
    #     fieldnames = r.colnames
    #     d_writer = csv.DictWriter(f, fieldnames=fieldnames)
    #     d_writer.writeheader()
    #     tb = astropy.table.Table(r)
    #     d_writer.writerows(tb)
