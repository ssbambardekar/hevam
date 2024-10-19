# Imports
import sys
import os
from sys import argv
import pandas as pd
from pathlib import Path

if __name__ == "__main__":
    root_path = os.path.dirname(os.path.dirname(argv[0]))
else:
    root_path = os.path.dirname(argv[0])
sys.path.insert(0, root_path)

from constants import Constants
from da_processor_base import DAProcessorBase


# DA Substation Exposure Processor Class
# Analyzes the substations exposure to temperatures beyond threshold temperature  
class DASubstationExposureProcessor(DAProcessorBase):
    # Constructor
    def __init__(self, substation_cmip_data_coordinates_map):
        self.substation_cmip_data_coordinates_map = substation_cmip_data_coordinates_map

    # Perform exposure analysis on the source files    
    def process_files(self, source_files, analyzed_file, threshold_temperature, exposure_operation):        
        try:
            # Set the column headers
            substation_exposure_columns_header_names = [Constants.LATITUDE_HEADER_NAME, Constants.LONGITUDE_HEADER_NAME]
                        
            # Load the source files into data frames            
            cmip_data_frames_list = []
            for source_file in source_files:
                # Set the paths
                source_file_absolute_path = root_path + "/" + source_file

                # Load the source file that has the cmip data, and add to list
                cmip_data_frames = pd.read_csv(source_file_absolute_path)
                cmip_data_frames_list.append(cmip_data_frames)

                # Set the source file year name in the list
                cmip_file_year_name = Path(source_file).stem.replace(Constants.FILE_NAME_PREFIX_CMIP_DATA_DAILY_MAX_TEMPERATURE, "")
                substation_exposure_columns_header_names.append(cmip_file_year_name)
                        
            # Iterate through each substation
            substation_exposure_list = []
            for substation_cmip_data_coordinates in self.substation_cmip_data_coordinates_map.substation_cmpi_data_coordinates.values():
                # Create the substation exposure list that will represent a row in the data frame
                substation_exposure = [substation_cmip_data_coordinates.substation_latitude, substation_cmip_data_coordinates.substation_longitude]

                # Iterate through each source data frames
                for cmip_data_frames in cmip_data_frames_list:
                    if exposure_operation == Constants.EXPOSURE_OPERATION_GREATER_THAN:
                        # Get the number of days that the temperature is above the threshold temperature
                        exposure_number_of_days = len(cmip_data_frames[
                                                    (cmip_data_frames[Constants.LATITUDE_HEADER_NAME] == substation_cmip_data_coordinates.cmip_data_latitude) & 
                                                    (cmip_data_frames[Constants.LONGITUDE_HEADER_NAME] == substation_cmip_data_coordinates.cmip_data_longitude) & 
                                                    (cmip_data_frames[Constants.DAILY_MAX_TEMPERATURE_HEADER_NAME] >= threshold_temperature)])
                    else:
                        # Get the number of days that the temperature is below the threshold temperature
                        exposure_number_of_days = len(cmip_data_frames[
                                                    (cmip_data_frames[Constants.LATITUDE_HEADER_NAME] == substation_cmip_data_coordinates.cmip_data_latitude) & 
                                                    (cmip_data_frames[Constants.LONGITUDE_HEADER_NAME] == substation_cmip_data_coordinates.cmip_data_longitude) & 
                                                    (cmip_data_frames[Constants.DAILY_MAX_TEMPERATURE_HEADER_NAME] <= threshold_temperature)])
                        
                    substation_exposure.append(exposure_number_of_days)

                # Add the substation exposure data to the list
                substation_exposure_list.append(substation_exposure)
                
            # Create data frames for the list
            substation_exposure_data_frames = pd.DataFrame(substation_exposure_list, columns=substation_exposure_columns_header_names)

            # Save the extracted data to processed file
            analyzed_file_absolute_path = root_path + "/" + analyzed_file 
            
            substation_exposure_data_frames.to_csv(analyzed_file_absolute_path, index=False)

            # Print etl end message
            self._print_da_end()
        except Exception as error:
            self._print_da_error(error)

