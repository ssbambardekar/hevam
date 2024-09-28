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


# ETL Surface Temperature Processor Class
class ETLSurfacetemperatureProcessor(ETLProcessorBase):
    # Constructor
    def __init__(self) -> None:
        pass

    # Perform generic etl on the given file    
    def process_file(self, source_file, processed_file):        
        try:
            # Set the paths            
            source_file_absolute_path = root_path + "/" + source_file
            processed_file_absolute_path = root_path + "/" + processed_file 
            
            # Set the columns to be extracted and normalized
            columns_to_be_extracted = ["lat", "lon", "ts"]
            normalized_columns_header_names = [Constants.LATITUDE_HEADER_NAME, Constants.LONGITUDE_HEADER_NAME, Constants.SURFACE_TEMPERATURE_HEADER_NAME]

            # Print etl begin message
            self._print_etl_begin(source_file_absolute_path, processed_file_absolute_path, columns_to_be_extracted, normalized_columns_header_names)

            # Load the source file. Note that the source file has spaces as separators instead of comma
            # So specify the separator when reading the file, else the selective columns will not be extracted
            extracted_data_frames = pd.read_csv(source_file_absolute_path, sep="\s+", usecols=columns_to_be_extracted)

            # Normalize the data frames
            extracted_data_frames = self._normalize_data_frames(extracted_data_frames, columns_to_be_extracted, normalized_columns_header_names)

            # The longitude column is in degree_east unit. Normalize it by converting it 
            # into degrees_west unit, to match the grid coordinates
            extracted_data_frames[Constants.LONGITUDE_HEADER_NAME] = extracted_data_frames[Constants.LONGITUDE_HEADER_NAME].apply(lambda x: (x - 360))

            # The surface temperature is in kelvin unit. Normalize it by converting it 
            # into faranheit unit
            extracted_data_frames[Constants.SURFACE_TEMPERATURE_HEADER_NAME] = extracted_data_frames[Constants.SURFACE_TEMPERATURE_HEADER_NAME].apply(lambda x: ((x - 273.15) * 9/5) + 32)

            # Save the extracted data to processed file
            extracted_data_frames.to_csv(processed_file_absolute_path, index=False)

            # Print etl end message
            self._print_etl_end()
        except Exception as error:
            self._print_etl_error(error)


# Debug Code
if __name__ == "__main__":
    etl_surface_temperature_processor = ETLSurfacetemperatureProcessor()
    source_file = Constants.CMIP_DATA_SURFACE_TEMPERATURE_SOURCE_FOLDER + "/surface_temperature_july_2030.csv"
    etl_surface_temperature_processor.process_file(source_file, "/data/processed/test_surface_temperatures.csv")