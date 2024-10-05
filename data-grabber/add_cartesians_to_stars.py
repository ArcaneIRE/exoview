import csv
from coord_operations import galactic_to_cartesian


def add_cartesians_to_stars_csv(input_path: str, output_path: str):
    with open(input_path, 'r') as file:
        reader = csv.DictReader(file)

        with open(output_path, 'w', newline='') as output_file:
            fieldnames = reader.fieldnames
            # Rename un-descriptive headers
            for i, field_name in enumerate(fieldnames):
                if field_name == 'l':
                    fieldnames[i] = 'galactic_longitude'
                if field_name == 'b':
                    fieldnames[i] = 'galactic_latitude'
                if field_name == 'distance_gspphot':
                    fieldnames[i] = 'distance_parsecs'
            # Add Cartesian coordinate headers
            fieldnames += ['cart_x', 'cart_y', 'cart_z']
            writer = csv.DictWriter(output_file, fieldnames=fieldnames)
            writer.writeheader()

            for star in reader:
                x, y, z = galactic_to_cartesian(
                    star['galactic_longitude'], star['galactic_latitude'], star['distance_parsecs'])
                star['cart_x'] = x
                star['cart_y'] = y
                star['cart_z'] = z
                writer.writerow(star)
