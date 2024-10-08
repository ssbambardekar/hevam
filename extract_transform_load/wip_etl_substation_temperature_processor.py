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


# ETL Substation Temperature Processor Class
class ETLSubstationTemperatureProcessor(ETLProcessorBase):
    # Constructor
    def __init__(self) -> None:
        pass

    # Perform substations temperatures etl on the given file    
    def process_file(self, source_substations_file, source_temperatures_file, processed_file):        
        try:
            # Set the paths            
            source_substations_file_absolute_path = root_path + "/" + source_substations_file
            source_temperatures_file_absolute_path = root_path + "/" + source_temperatures_file
            processed_file_absolute_path = root_path + "/" + processed_file 
            
            # Set the columns to be extracted from the source grid coordinates file
            source_grid_coordinates_file_columns_to_be_extracted = ["Latitude", "Longitude"]
            normalized_grid_coordinates_columns_header_names = [Constants.LATITUDE_HEADER_NAME, Constants.LONGITUDE_HEADER_NAME]
            source_surface_temperature_file_columns_to_be_extracted = ["lat", "lon", "ts"]
            normalized_surface_temperature_columns_header_names = [Constants.LATITUDE_HEADER_NAME, Constants.LONGITUDE_HEADER_NAME, Constants.DAILY_MAX_TEMPERATURE_HEADER_NAME]

            # Print etl begin message
            print("Starting ETL Processing of combined grid coordinates file and surface temperatures file...")
            self._print_etl_begin(source_substations_file_absolute_path, processed_file_absolute_path, source_grid_coordinates_file_columns_to_be_extracted, normalized_grid_coordinates_columns_header_names)            
            self._print_etl_begin(source_temperatures_file_absolute_path, processed_file_absolute_path, source_surface_temperature_file_columns_to_be_extracted, normalized_surface_temperature_columns_header_names)

            # Load the source grid coordinates file
            extracted_grid_coordinates_data_frames = pd.read_csv(source_substations_file_absolute_path, usecols=source_grid_coordinates_file_columns_to_be_extracted)
            
            # Normalize the source grid coordinates data frames
            extracted_grid_coordinates_data_frames = self._normalize_data_frames(extracted_grid_coordinates_data_frames, source_grid_coordinates_file_columns_to_be_extracted, normalized_grid_coordinates_columns_header_names)

            # Load the source surface temperature data frames
            extracted_surface_temperatures_data_frames = pd.read_csv(source_temperatures_file_absolute_path, sep="\s+", usecols=source_surface_temperature_file_columns_to_be_extracted)

            # Normalize the source surface temperature data frames
            extracted_surface_temperatures_data_frames = self._normalize_data_frames(extracted_surface_temperatures_data_frames, source_surface_temperature_file_columns_to_be_extracted, normalized_surface_temperature_columns_header_names)

            # Add the surface temperature column to the grid coordinates, and set surface temperature values based on the grid coordinates
            extracted_grid_coordinates_data_frames = extracted_grid_coordinates_data_frames.apply(lambda df: self._get_surface_temperature_from_grid_coordinates(df, extracted_surface_temperatures_data_frames), axis=1)

            # Save the extracted data to processed file
            extracted_grid_coordinates_data_frames.to_csv(processed_file_absolute_path, index=False)

            # Print etl end message
            self._print_etl_end()
        except Exception as error:
            self._print_etl_error(error)

    # Get state from coordinates
    def _get_surface_temperature_from_grid_coordinates(self, data_frame, extracted_surface_temperatures_data_frames):        
        matching_surface_temperature = 0
        nearest_distance_squared = sys.maxsize

        for index, extracted_surface_temperatures_data_frame_row in extracted_surface_temperatures_data_frames.iterrows():            
            # Use the distance formula: (x2-x1)^2 + (y2-y1)^2
            # We do not need to square root it to save some cpu cycles, we just care about the closest point            
            dx = extracted_surface_temperatures_data_frame_row[Constants.LATITUDE_HEADER_NAME] - data_frame[Constants.LATITUDE_HEADER_NAME]
            dy = extracted_surface_temperatures_data_frame_row[Constants.LONGITUDE_HEADER_NAME] - data_frame[Constants.LONGITUDE_HEADER_NAME]

            distanceSquared = dx*dx + dy*dy;        
            if distanceSquared < nearest_distance_squared:
                nearest_distance_squared = distanceSquared
                matching_surface_temperature = extracted_surface_temperatures_data_frame_row[Constants.DAILY_MAX_TEMPERATURE_HEADER_NAME]

        data_frame[Constants.DAILY_MAX_TEMPERATURE_HEADER_NAME] = matching_surface_temperature
        print(data_frame)
        return data_frame


# Debug Code
if __name__ == "__main__":
    etl_grid_surface_temperature_processor = ETLSubstationTemperatureProcessor()
    source_grid_coordinates_file = Constants.GRID_MAPPING_SOURCE_FILE
    source_surface_temperature_file = "data/source/cmip_data/surface_temperature/surface_temperatures_july_2030.csv"
    etl_grid_surface_temperature_processor.process_file(source_grid_coordinates_file, source_surface_temperature_file, "/data/processed/test_surface_temperature_by_grid_coordinates.csv")