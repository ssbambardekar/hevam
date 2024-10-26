# Imports
import sys
import os
from sys import argv

root_path = os.path.dirname(argv[0])
sys.path.insert(0, root_path)

from substation_cmip_data_coordinates_map import SubstationCMIPDataCoordinatesMap
from da_substation_exposure_processor import DASubstationExposureProcessor
from constants import Constants


# DA Manager Class
class DAManager:
    # Constructor
    def __init__(self):
        # Load the substations cmip data coordinates map
        source_file = Constants.SUBSTATION_CMIP_DATA_COORDINATES_PROCESSED_FILE
        self.substation_cmip_data_coordinates_map = SubstationCMIPDataCoordinatesMap(source_file)

        self.da_substation_exposure_processor = DASubstationExposureProcessor(self.substation_cmip_data_coordinates_map)
        
    # DA substation exposure
    def da_substations_exposure(self, threshold_temperature, exposure_operation):
        # Get all the cmip data daily max temperature related files from the requisite source folder   
        cmip_data_daily_max_temperature_source_folder_absolute_path = root_path + "/" + Constants.CMIP_DATA_DAILY_MAX_TEMPERATURE_PROCESSED_FOLDER
        cmip_data_daily_max_temperature_source_files = []
        for file_name in os.listdir(cmip_data_daily_max_temperature_source_folder_absolute_path):
            if (file_name.startswith(Constants.FILE_NAME_PREFIX_CMIP_DATA_DAILY_MAX_TEMPERATURE)):
                source_file = Constants.CMIP_DATA_DAILY_MAX_TEMPERATURE_PROCESSED_FOLDER + "/" + file_name
                cmip_data_daily_max_temperature_source_files.append(source_file)

        # Process the cmip data daily max temperatue files
        analyzed_file = Constants.CMIP_DATA_DAILY_MAX_TEMPERATURE_ANALYZED_FOLDER + "/" + Constants.FILE_NAME_PREFIX_SUBSTATION_EXPOSURE_THRESHOLD_TEMPERATURE + exposure_operation + "_" + str(threshold_temperature) + ".csv"

        self.da_substation_exposure_processor.process_files(cmip_data_daily_max_temperature_source_files, analyzed_file, threshold_temperature, exposure_operation)
