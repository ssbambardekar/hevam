# Imports
import sys
import os
from sys import argv

root_path = os.path.dirname(os.path.dirname(argv[0]))
sys.path.insert(0, root_path)

from etl_processor import ETLProcessor
from constants import Constants


# ETL Manager Class
class ETLManager:
    # Constructor
    def __init__(self) -> None:
        self.etl_processor = ETLProcessor()

    # ETL grid coordinates
    def etl_grid_coordinates(self):        
        columns_to_be_extracted = ["Latitude", "Longitude"]
        source_file = Constants.GRID_MAPPING_SOURCE_FILE
        processed_file = Constants.GRID_COORDINATES_PROCESSED_FILE
        self.etl_processor.process_file(source_file, processed_file, columns_to_be_extracted)

    # ETL grid components by coordinates
    def etl_grid_components_by_coordinates(self):        
        columns_to_be_extracted = ["Latitude", "Longitude", "Marker Label"]
        source_file = Constants.GRID_MAPPING_SOURCE_FILE
        processed_file = Constants.GRID_COMPONENTS_BY_COORDINATES_PROCESSED_FILE
        self.etl_processor.process_file(source_file, processed_file, columns_to_be_extracted)

