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


# DA Exposure Processor Class
class DAExposureProcessor:
    # Constructor
    def __init__(self):
        pass

    # Perform power grid etl on the given file    
    def process_file(self, source_file, processed_file):        
        try:
            # Set the paths
            source_file_absolute_path = root_path + "/" + source_file
            processed_file_absolute_path = root_path + "/" + processed_file 

            # Set the columns to be extracted and normalized                        
            columns_to_be_extracted = ["Latitude", "Longitude", "Marker Label"]
            normalized_columns_header_names = [Constants.LATITUDE_HEADER_NAME, Constants.LONGITUDE_HEADER_NAME, Constants.POWER_GRID_COMPONENT_HEADER_NAME]

            # Print etl begin message
            self._print_etl_begin(source_file_absolute_path, processed_file_absolute_path, columns_to_be_extracted, normalized_columns_header_names)

            # Load the source file
            extracted_data_frames = pd.read_csv(source_file_absolute_path, usecols=columns_to_be_extracted)

            # Normalize the data frames
            extracted_data_frames = self._normalize_data_frames(extracted_data_frames, columns_to_be_extracted, normalized_columns_header_names)

            # Save the extracted data to processed file
            extracted_data_frames.to_csv(processed_file_absolute_path, index=False)

            # Print etl end message
            self._print_etl_end()
        except Exception as error:
            self._print_etl_error(error)


# Debug Code
if __name__ == "__main__":
    etl_generic_processor = ETLPowerGridProcessor()
    columns_to_be_extracted = ["Latitude", "Longitude"]
    normalized_columns_header_names = [Constants.LATITUDE_HEADER_NAME, Constants.LONGITUDE_HEADER_NAME]
    etl_generic_processor.process_file(Constants.POWER_GRIDS_SOURCE_FILE, "/data/processed/generated/test_coordinates.csv", columns_to_be_extracted, normalized_columns_header_names)