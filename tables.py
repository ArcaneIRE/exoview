import csv
import convert

# Open the CSV file
with open('a.csv', 'r') as file:
    # Create a CSV reader object
    reader = csv.DictReader(file)

    # Open a new file for writing
    with open('a_new.csv', 'w', newline='') as output_file:
        # Create a CSV writer object
        fieldnames = reader.fieldnames + ['cart_x', 'cart_y', 'cart_z']
        writer = csv.DictWriter(output_file, fieldnames=fieldnames)
        writer.writeheader()

        # Iterate over the rows in the CSV file
        for row in reader:

            # Write the row to the new CSV file
            x, y, z = convert.galacticToCartesian(row['l'], row['b'], row['distance_gspphot'])
            row['cart_x'] = x
            row['cart_y'] = y
            row['cart_z'] = z

            writer.writerow(row)

