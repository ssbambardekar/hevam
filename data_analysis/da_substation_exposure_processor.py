# Imports
import sys
import os
from sys import argv
import pandas as pd
import numpy as np

if __name__ == "__main__":
    root_path = os.path.dirname(os.path.dirname(argv[0]))
else:
    root_path = os.path.dirname(argv[0])
sys.path.insert(0, root_path)

from constants import Constants
from da_processor_base import DAProcessorBase
from substation_exposure import SubstationExposure


# DA Substation Exposure Processor Class
# Analyzes the substations exposure to temperatures beyond threshold temperature  
class DASubstationExposureProcessor(DAProcessorBase):
    # Constructor
    def __init__(self, substation_cmip_data_coordinates_map):
        self.substation_cmip_data_coordinates_map = substation_cmip_data_coordinates_map

    # Perform exposure analysis on the source file    
    def process_file(self, source_file, analyzed_file, threshold_temperature):        
        try:
            # Set the paths
            source_file_absolute_path = root_path + "/" + source_file
            analyzed_file_absolute_path = root_path + "/" + analyzed_file 
            
            # Print da begin message
            self._print_da_begin(source_file_absolute_path, analyzed_file_absolute_path)
            print("Threshold Temperature: ", threshold_temperature)
       
            # Load the source file that has the cmip data
            source_data_frames = pd.read_csv(source_file_absolute_path)
                        
            substation_exposure_columns_header_names = [Constants.LATITUDE_HEADER_NAME, Constants.LONGITUDE_HEADER_NAME, Constants.DAILY_MAX_TEMPERATURE_HEADER_NAME]
            substation_exposure_list = []
            for substation_cmip_data_coordinates in self.substation_cmip_data_coordinates_map.substation_cmpi_data_coordinates.values():
                # Get the number of days that the temperature is above the threshold temperature
                exposure_number_of_days = len(source_data_frames[
                                                (source_data_frames[Constants.LATITUDE_HEADER_NAME] == substation_cmip_data_coordinates.cmip_data_latitude) & 
                                                (source_data_frames[Constants.LONGITUDE_HEADER_NAME] == substation_cmip_data_coordinates.cmip_data_longitude) & 
                                                (source_data_frames[Constants.DAILY_MAX_TEMPERATURE_HEADER_NAME] >= threshold_temperature)])
                
                substation_exposure = [substation_cmip_data_coordinates.substation_latitude, substation_cmip_data_coordinates.substation_longitude, exposure_number_of_days]
                substation_exposure_list.append(substation_exposure)

            # Create data frames for the list
            substation_exposure_data_frames = pd.DataFrame(substation_exposure_list, columns=substation_exposure_columns_header_names)

            # Save the extracted data to processed file
            substation_exposure_data_frames.to_csv(analyzed_file_absolute_path, index=False)

            # Print etl end message
            self._print_da_end()
        except Exception as error:
            self._print_da_error(error)

