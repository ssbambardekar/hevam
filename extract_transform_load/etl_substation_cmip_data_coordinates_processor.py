# Imports
import sys
import os
from sys import argv
import pandas as pd

if __name__ == "__main__":
    root_path = os.path.dirname(os.path.dirname(argv[0]))
else:
    root_path = os.path.dirname(argv[0])
sys.path.insert(0, root_path)

from constants import Constants
from etl_processor_base import ETLProcessorBase


# ETL Substation Cmip Data Coordinates Processor Class
# Extracts and maps substation to cmip data coordinates, to generate processed file `substations_cmip_data_coordinates.csv`
class ETLSubstationCmipDataCoordinatesProcessor(ETLProcessorBase):
    # Constructor
    def __init__(self):
        pass

    # Perform substations temperatures etl on the given file    
    def process_file(self, source_substation_state_file, source_cmip_data_file, processed_file):        
        try:
            # Set the paths            
            source_substation_state_file_absolute_path = root_path + "/" + source_substation_state_file
            source_cmip_data_file_absolute_path = root_path + "/" + source_cmip_data_file
            processed_file_absolute_path = root_path + "/" + processed_file 
            
            # Set the columns to be extracted from the source files
            source_substation_state_file_columns_to_be_extracted = ["Latitude", "Longitude", "State"]
            normalized_substation_state_file_columns_header_names = [Constants.SUBSTATION_LATITUDE_HEADER_NAME, Constants.SUBSTATION_LONGITUDE_HEADER_NAME, Constants.SUBSTATION_STATE_HEADER_NAME]
            source_cmip_data_file_columns_to_be_extracted = ["Latitude", "Longitude"]
            normalized_cmip_data_columns_header_names = [Constants.CMIP_DATA_LATITUDE_HEADER_NAME, Constants.CMIP_DATA_LONGITUDE_HEADER_NAME]

            # Print etl begin message
            print("Starting ETL Processing of combined substation file and cmip data coordinates file...")
            self._print_etl_begin(source_substation_state_file_absolute_path, processed_file_absolute_path, source_substation_state_file_columns_to_be_extracted, normalized_substation_state_file_columns_header_names)            
            self._print_etl_begin(source_cmip_data_file_absolute_path, processed_file_absolute_path, source_cmip_data_file_columns_to_be_extracted, normalized_cmip_data_columns_header_names)

            # Load the source substation file
            extracted_substation_state_data_frames = pd.read_csv(source_substation_state_file_absolute_path, usecols=source_substation_state_file_columns_to_be_extracted)
            
            # Normalize the source substation data frames
            extracted_substation_state_data_frames = self._normalize_data_frames(extracted_substation_state_data_frames, source_substation_state_file_columns_to_be_extracted, normalized_substation_state_file_columns_header_names)

            # Load the source cmip data frames
            extracted_cmip_data_frames = pd.read_csv(source_cmip_data_file_absolute_path, usecols=source_cmip_data_file_columns_to_be_extracted)

            # Normalize the source cmip data frames
            extracted_cmip_data_frames = self._normalize_data_frames(extracted_cmip_data_frames, source_cmip_data_file_columns_to_be_extracted, normalized_cmip_data_columns_header_names)

            # Add the cmip data coordinates columns to the substation coordinates
            extracted_substation_state_data_frames = extracted_substation_state_data_frames.apply(lambda df: self._map_coordinates(df, extracted_cmip_data_frames), axis=1)

            # Save the extracted data to processed file
            extracted_substation_state_data_frames.to_csv(processed_file_absolute_path, index=False)

            # Print etl end message
            self._print_etl_end()
        except Exception as error:
            self._print_etl_error(error)

    # Get state from coordinates
    def _map_coordinates(self, data_frame, extracted_cmip_data_frames):        
        cmip_data_latitude = 0
        cmip_data_longitude = 0
        nearest_distance_squared = sys.maxsize

        for index, extracted_cmip_data_frame_row in extracted_cmip_data_frames.iterrows():            
            # Use the distance formula: (x2-x1)^2 + (y2-y1)^2
            # We do not need to square root it to save some cpu cycles, we just care about the closest point            
            dx = extracted_cmip_data_frame_row[Constants.CMIP_DATA_LATITUDE_HEADER_NAME] - data_frame[Constants.SUBSTATION_LATITUDE_HEADER_NAME]
            dy = extracted_cmip_data_frame_row[Constants.CMIP_DATA_LONGITUDE_HEADER_NAME] - data_frame[Constants.SUBSTATION_LONGITUDE_HEADER_NAME]

            distanceSquared = dx*dx + dy*dy;        
            if distanceSquared < nearest_distance_squared:
                nearest_distance_squared = distanceSquared
                cmip_data_latitude = extracted_cmip_data_frame_row[Constants.CMIP_DATA_LATITUDE_HEADER_NAME]
                cmip_data_longitude = extracted_cmip_data_frame_row[Constants.CMIP_DATA_LONGITUDE_HEADER_NAME]

        data_frame[Constants.CMIP_DATA_LATITUDE_HEADER_NAME] = cmip_data_latitude
        data_frame[Constants.CMIP_DATA_LONGITUDE_HEADER_NAME] = cmip_data_longitude
        
        return data_frame


# Debug Code
if __name__ == "__main__":
    etl_substation_cmip_data_coordinates_processor = ETLSubstationCmipDataCoordinatesProcessor()
    source_substation_file = Constants.SUBSTATION_STATES_PROCESSED_FILE
    source_cmip_data_file = "data/processed/generated/cmip_data_daily_max_temperatures_2025.csv"                                            
    etl_substation_cmip_data_coordinates_processor.process_file(source_substation_file, source_cmip_data_file, "/data/processed/generated/test_substation_cmip_data_coordinates.csv")