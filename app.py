# Imports
import sys
import os
from sys import argv

root_path = os.path.dirname(argv[0])
etl_module_path = root_path + '/extract_transform_load'
sys.path.insert(0, etl_module_path)

from etl_manager import ETLManager


# Create Etl manager
etl_manager = ETLManager()

# Steps
# ETL coordinates
etl_manager.etl_grid_coordinates()

# ETL components by coordinates
etl_manager.etl_grid_components_by_coordinates()

# ETL surface temperatures by coordinates and decades
etl_manager.etl_surface_temperature_by_coordinates_and_decades()
    