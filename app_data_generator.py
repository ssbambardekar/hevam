# Imports
import sys
import os
from sys import argv

root_path = os.path.dirname(argv[0])
etl_module_path = root_path + '/extract_transform_load'
sys.path.insert(0, etl_module_path)

from etl_manager import ETLManager


# Create etl manager
etl_manager = ETLManager()

# Steps - NOTE: The order of steps matters, as processed files of some steps serve as inputs to the next steps
# ETL daily max temperatures
etl_manager.etl_daily_max_temperature()

# ETL power grids
etl_manager.etl_power_grids()

# ETL Substations
etl_manager.etl_substations()

# ETL Substations States
etl_manager.etl_substations_states()

# ETL substations cmip data coordinates
etl_manager.etl_substations_cmip_data_coordinates()