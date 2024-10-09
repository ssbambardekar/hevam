# Imports
import sys
import os
from sys import argv

root_path = os.path.dirname(argv[0])
sys.path.insert(0, root_path)

from etl_daily_max_temperature_processor import ETLDailyMaxTemperatureProcessor
from etl_power_grid_processor import ETLPowerGridProcessor
from etl_substation_processor import ETLSubstationProcessor
from etl_state_processor import ETLStateProcessor
from etl_substation_cmip_data_coordinates_processor import ETLSubstationCmipDataCoordinatesProcessor
from constants import Constants


# ETL Manager Class
class ETLManager:
    # Constructor
    def __init__(self):
        self.etl_daily_max_temperature_processor = ETLDailyMaxTemperatureProcessor()
        self.etl_power_grid_processor = ETLPowerGridProcessor()
        self.etl_substation_processor = ETLSubstationProcessor()       
        self.etl_state_processor = ETLStateProcessor()
        self.etl_substation_cmip_data_coordinates_processor = ETLSubstationCmipDataCoordinatesProcessor()

    # ETL daily max temperature
    def etl_daily_max_temperature(self):     
        # Get all the daily max temperature related files from the requisite source folder   
        cmip_data_daily_max_temperature_source_folder_absolute_path = root_path + "/" + Constants.CMIP_DATA_DAILY_MAX_TEMPERATURE_SOURCE_FOLDER
        cmip_data_daily_max_temperature_source_files = os.listdir(cmip_data_daily_max_temperature_source_folder_absolute_path)

        for cmip_data_daily_max_temperature_source_file in cmip_data_daily_max_temperature_source_files:            
            source_file = Constants.CMIP_DATA_DAILY_MAX_TEMPERATURE_SOURCE_FOLDER + "/" + cmip_data_daily_max_temperature_source_file
            processed_file = Constants.CMIP_DATA_DAILY_MAX_TEMPERATURE_PROCESSED_FOLDER + "/" + cmip_data_daily_max_temperature_source_file.replace("daily_max_temperatures", "cmip_data_daily_max_temperatures")

            # Process the surface temperature file
            self.etl_daily_max_temperature_processor.process_file(source_file, processed_file)

    # ETL power grids
    def etl_power_grids(self):        
        source_file = Constants.POWER_GRIDS_SOURCE_FILE
        processed_file = Constants.POWER_GRIDS_PROCESSED_FILE
        
        # Process the power grids file
        self.etl_power_grid_processor.process_file(source_file, processed_file)

   # ETL substations
    def etl_substations(self):
        source_file = Constants.SUBSTATIONS_SOURCE_FILE
        processed_file = Constants.SUBSTATIONS_PROCESSED_FILE

        # Process the substations file
        self.etl_substation_processor.process_file(source_file, processed_file)

    # ETL substations states
    def etl_substations_states(self):
        source_file = Constants.SUBSTATIONS_PROCESSED_FILE
        processed_file = Constants.SUBSTATION_STATES_PROCESSED_FILE

        # Process the substations states file
        self.etl_state_processor.process_file(source_file, processed_file)

    # ETL substations cmip data coordinates
    def etl_substations_cmip_data_coordinates(self):
        source_substation_file = Constants.SUBSTATIONS_PROCESSED_FILE
        source_cmip_data_file = Constants.CMIP_DATA_DAILY_MAX_TEMPERATURE_2025_PROCESSED_FILE
        processed_file = Constants.SUBSTATION_CMIP_DATA_COORDINATES_PROCESSED_FILE

        # Process the substations cmip data coordinates file
        self.etl_substation_cmip_data_coordinates_processor.process_file(source_substation_file, source_cmip_data_file, processed_file)    