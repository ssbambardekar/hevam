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


# ETL Substation Processor Class
# Extracts and normalizes substation data to generate processed file `substations.csv`
class ETLSubstationProcessor(ETLProcessorBase):
    # Constructor
    def __init__(self) -> None:
        pass

    # Perform substation etl on the given file    
    def process_file(self, source_file, processed_file):        
        try:
            # Set the paths            
            source_file_absolute_path = root_path + "/" + source_file
            processed_file_absolute_path = root_path + "/" + processed_file 
            
            # Set the columns to be extracted and normalized            
            columns_to_be_extracted = ["lat", "lon", "SS_NAME", "SS_TYPE", "SS_VOLTAGE"]
            normalized_columns_header_names = [Constants.LATITUDE_HEADER_NAME, Constants.LONGITUDE_HEADER_NAME, Constants.SUBSTATION_NAME, Constants.SUBSTATION_TYPE, Constants.SUBSTATION_VOLTAGE, ]

            # Print etl begin message
            self._print_etl_begin(source_file_absolute_path, processed_file_absolute_path, columns_to_be_extracted, normalized_columns_header_names)

            # Load the source file
            extracted_data_frames = pd.read_json(source_file_absolute_path, orient="record")

            # Normalize the data frames
            extracted_data_frames = self._normalize_data_frames(extracted_data_frames, columns_to_be_extracted, normalized_columns_header_names)

            # Filter the substation voltage to have only highest voltage value, which is the first value in the string
            extracted_data_frames = extracted_data_frames.apply(self._set_substation_voltage, axis=1)

            # Save the extracted data to processed file
            extracted_data_frames.to_csv(processed_file_absolute_path, index=False)

            # Print etl end message
            self._print_etl_end()
        except Exception as error:
            self._print_etl_error(error)

    # Filter the substation voltage to have only highest voltage value
    def _set_substation_voltage(self, data_frame):        
        # Voltage values in the record are split by semi-colon (E.g. 230000;115000;35000)
        # These are sorted in the descending order, so get the first voltage value in the record
        substation_voltages_list = data_frame[Constants.SUBSTATION_VOLTAGE].split(";")
        data_frame[Constants.SUBSTATION_VOLTAGE] = substation_voltages_list[0]
        return data_frame


# Debug Code
if __name__ == "__main__":
    etl_substation_processor = ETLSubstationProcessor()
    source_substation_mapping_file = Constants.SUBSTATIONS_SOURCE_FILE    
    etl_substation_processor.process_file(source_substation_mapping_file, "/data/processed/test_substation_coordinates.csv")