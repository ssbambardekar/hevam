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
    def da_substations_exposure(self):
        source_file = Constants.CMIP_DATA_DAILY_MAX_TEMPERATURE_2025_PROCESSED_FILE
        analyzed_file = "/data/processed/analyzed/substations_exposure_2025.csv"
        threshold_temperature = 70

        # Process the cmip data daily max tempeatue file
        self.da_substation_exposure_processor.process_file(source_file, analyzed_file, threshold_temperature)

