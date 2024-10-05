import csv
import convert

with open('stars.csv', 'r') as file:
    reader = csv.DictReader(file)

    with open('stars_with_cartesian.csv', 'w', newline='') as output_file:
        fieldnames = reader.fieldnames
        for i, field_name in enumerate(fieldnames):
            if field_name == 'l':
                fieldnames[i] = 'galactic_longitude'
            if field_name == 'b':
                fieldnames[i] = 'galactic_latitude'
            if field_name == 'distance_gspphot':
                fieldnames[i] = 'distance_parsecs'
        fieldnames += ['cart_x', 'cart_y', 'cart_z']
        writer = csv.DictWriter(output_file, fieldnames=fieldnames)
        writer.writeheader()

        for row in reader:
            x, y, z = convert.galacticToCartesian(
                row['galactic_longitude'], row['galactic_latitude'], row['distance_parsecs'])
            row['cart_x'] = x
            row['cart_y'] = y
            row['cart_z'] = z
            writer.writerow(row)
