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
from state_coordinates_map import StateCoordinatesMap

# ETL State Processor Class
class ETLStateProcessor(ETLProcessorBase):
    # Constructor
    def __init__(self) -> None:
        self.state_coordinates_map = StateCoordinatesMap()

    # Perform generic etl on the given file    
    def process_file(self, source_file, processed_file):        
        try:
            # Set the paths            
            source_file_absolute_path = root_path + "/" + source_file
            processed_file_absolute_path = root_path + "/" + processed_file 
            
            # Set the columns to be extracted and normalized
            columns_to_be_extracted = ["Latitude", "Longitude"]
            normalized_columns_header_names = [Constants.LATITUDE_HEADER_NAME, Constants.LONGITUDE_HEADER_NAME]

            # Print etl begin message
            self._print_etl_begin(source_file_absolute_path, processed_file_absolute_path, columns_to_be_extracted, normalized_columns_header_names)

            # Load the source file
            extracted_data_frames = pd.read_csv(source_file_absolute_path, usecols=columns_to_be_extracted)
            
            # Normalize the data frames
            extracted_data_frames = self._normalize_data_frames(extracted_data_frames, columns_to_be_extracted, normalized_columns_header_names)

            # Add the state column, and set state values based on the coordinates
            extracted_data_frames = extracted_data_frames.apply(self._get_state_from_coordinates, axis=1)

            # Save the extracted data to processed file
            extracted_data_frames.to_csv(processed_file_absolute_path, index=False)

            # Print etl end message
            self._print_etl_end()
        except Exception as error:
            self._print_etl_error(error)

    # Get state from coordinates
    def _get_state_from_coordinates(self, data_frame):        
        matching_state = ""
        nearest_distance_squared = sys.maxsize

        for state_coordinates in self.state_coordinates_map.states_by_coordinates:            
            # Use the distance formula: (x2-x1)^2 + (y2-y1)^2
            # We do not need to square root it to save some cpu cycles, we just care about the closest point            
            dx = state_coordinates.latitude - data_frame[Constants.LATITUDE_HEADER_NAME]
            dy = state_coordinates.longitude - data_frame[Constants.LONGITUDE_HEADER_NAME]

            distanceSquared = dx*dx + dy*dy;        
            if distanceSquared < nearest_distance_squared:
                nearest_distance_squared = distanceSquared
                matching_state = state_coordinates.state

        data_frame[Constants.STATE_HEADER_NAME] = matching_state
        return data_frame


# Debug Code
if __name__ == "__main__":
    etl_state_processor = ETLStateProcessor()
    source_file = Constants.GRID_MAPPING_SOURCE_FILE
    etl_state_processor.process_file(source_file, "/data/processed/test_state_by_coordinates.csv")