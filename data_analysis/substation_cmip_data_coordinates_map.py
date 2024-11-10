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
from substation_cmip_data_coordinates import SubstationCMIPDataCoordinates

# Substation CMIP Data Coordinates MAP Class
class SubstationCMIPDataCoordinatesMap:
    # Constructor
    def __init__(self, source_file):
        self.substation_cmpi_data_coordinates = {} # Dictionary of { <substation_coordinates_key>, SubstationCMIPDataCoordinates }
        self._populate_substation_cmip_data_coordinates_map(source_file)

    # Populate substation cmip data coordinates map
    def _populate_substation_cmip_data_coordinates_map(self, source_file):
        # Set the paths            
        source_file_absolute_path = root_path + "/" + source_file        

        # Load the source file
        extracted_data_frames = pd.read_csv(source_file_absolute_path)

        for index, extracted_data_frames_row in extracted_data_frames.iterrows():
            # Build the key and the object
            substation_latitude = str(extracted_data_frames_row[Constants.SUBSTATION_LATITUDE_HEADER_NAME])
            substation_longitude = str(extracted_data_frames_row[Constants.SUBSTATION_LONGITUDE_HEADER_NAME])
            substation_cmpi_data_coordinates_key = substation_latitude + ":" + substation_longitude
            substation_cmip_data_coordinates = SubstationCMIPDataCoordinates(extracted_data_frames_row[Constants.SUBSTATION_LATITUDE_HEADER_NAME], 
                                                                             extracted_data_frames_row[Constants.SUBSTATION_LONGITUDE_HEADER_NAME],
                                                                             extracted_data_frames_row[Constants.SUBSTATION_STATE_HEADER_NAME],
                                                                             extracted_data_frames_row[Constants.CMIP_DATA_LATITUDE_HEADER_NAME],
                                                                             extracted_data_frames_row[Constants.CMIP_DATA_LONGITUDE_HEADER_NAME])
            
            # Set the substation cmip data coordinates in the map
            self.substation_cmpi_data_coordinates[substation_cmpi_data_coordinates_key] = substation_cmip_data_coordinates