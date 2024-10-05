import csv
from math import *


def galacticToCartesian(gLat, gLong, dist):
    """
    Convert Galactic coordinates to Cartesian coordinates.    
    gLat: Galactic latitude in degrees
    gLong: Galactic longitude in degrees
    dist: Distance
    """
    
    gLat = float(gLat)
    gLong = float(gLong)
    dist = float(dist)
    
    # Convert angles from degrees to radians
    gLongRad = radians(gLong) 
    gLatRad = radians(gLat)

    # Cartesian coordinates conversion
    x = dist * cos(gLatRad) * cos(gLongRad)
    y = dist * cos(gLatRad) * sin(gLongRad)
    z = dist * sin(gLatRad)
    
    return (x, y, z)

# Open the CSV file
with open('a.csv', 'r') as file:
    # Create a CSV reader object
    reader = csv.DictReader(file)

    # Open a new file for writing
    with open('a_new.csv', 'w', newline='') as output_file:
        # Create a CSV writer object
        writer = csv.writer(output_file)

        # Iterate over the rows in the CSV file
        for row in reader:

            # Write the row to the new CSV file
            x, y, dist = galacticToCartesian(row['l'], row['b'], row['distance_gspphot'])
            row['cart_x'] = x
            row['cart_y'] = y
            row['dist'] = dist

            writer.writerow(row)

