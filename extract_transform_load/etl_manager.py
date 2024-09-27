# Imports
import sys
import os
from sys import argv

root_path = os.path.dirname(argv[0])
sys.path.insert(0, root_path)

from etl_generic_processor import ETLGenericProcessor
from etl_surface_temperature_processor import ETLSurfacetemperatureProcessor
from constants import Constants


# ETL Manager Class
class ETLManager:
    # Constructor
    def __init__(self) -> None:
        self.etl_generic_processor = ETLGenericProcessor()
        self.etl_surface_temperature_processor = ETLSurfacetemperatureProcessor()

    # ETL grid coordinates
    def etl_grid_coordinates(self):        
        columns_to_be_extracted = ["Latitude", "Longitude"]
        normalized_columns_header_names = [Constants.LATITUDE_HEADER_NAME, Constants.LONGITUDE_HEADER_NAME]
        source_file = Constants.GRID_MAPPING_SOURCE_FILE
        processed_file = Constants.GRID_COORDINATES_PROCESSED_FILE
        self.etl_generic_processor.process_file(source_file, processed_file, columns_to_be_extracted, normalized_columns_header_names)

    # ETL grid components by coordinates
    def etl_grid_components_by_coordinates(self):        
        columns_to_be_extracted = ["Latitude", "Longitude", "Marker Label"]
        normalized_columns_header_names = [Constants.LATITUDE_HEADER_NAME, Constants.LONGITUDE_HEADER_NAME, Constants.POWER_GRID_COMPONENT_HEADER_NAME]
        source_file = Constants.GRID_MAPPING_SOURCE_FILE
        processed_file = Constants.GRID_COMPONENTS_BY_COORDINATES_PROCESSED_FILE
        self.etl_generic_processor.process_file(source_file, processed_file, columns_to_be_extracted, normalized_columns_header_names)

    # ETL surface temperature by coordinates
    def etl_surface_temperature_by_coordinates(self):        
        cmip_data_surface_temperature_source_folder_absolute_path = root_path + "/" + Constants.CMIP_DATA_SURFACE_TEMPERATURE_SOURCE_FOLDER
        cmip_data_surface_temperature_source_files = os.listdir(cmip_data_surface_temperature_source_folder_absolute_path)

        for cmip_data_surface_temperature_source_file in cmip_data_surface_temperature_source_files:
            source_file = Constants.CMIP_DATA_SURFACE_TEMPERATURE_SOURCE_FOLDER + "/" + cmip_data_surface_temperature_source_file
            processed_file = Constants.SURFACE_TEMPERATURES_BY_COORDINATES_PROCESSED_FOLDER + "/" + cmip_data_surface_temperature_source_file.replace("surface_temperatures", "surface_temperatures_by_coordinates")
            self.etl_surface_temperature_processor.process_file(source_file, processed_file)