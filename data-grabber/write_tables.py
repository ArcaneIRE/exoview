from astropy.table import Table
import os


def write_tables(planet: Table, stars: Table):
    planets_folder_path = os.getcwd() + '/data/'
    planet_index = get_highest_numbered_folder(planets_folder_path) + 1
    planet_folder_path = f"{planets_folder_path}exoplanet_{planet_index}"
    os.makedirs(planet_folder_path)
    planet_df = planet.to_pandas()
    planet_df.to_json(f"{planet_folder_path}/planet.json", orient="records")
    stars_df = stars.to_pandas()
    stars_df.to_json(f"{planet_folder_path}/stars.json", orient="records")


def get_highest_numbered_folder(data_folder_path: str):
    """Gets the highest numbered exoplanet folder in the given path.

    Args:
      folder_path: The path to the folder containing the exoplanet folders.

    Returns:
      The highest numbered exoplanet folder, or None if no such folder exists.
    """
    exoplanet_folders = [folder for folder in os.listdir(
        data_folder_path) if folder.startswith('exoplanet_')]
    if not exoplanet_folders:
        return 0

    existing_indexes = [int(folder.split('_')[1])
                        for folder in exoplanet_folders]
    return max(existing_indexes)
