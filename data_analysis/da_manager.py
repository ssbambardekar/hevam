# Imports
import sys
import os
from sys import argv

root_path = os.path.dirname(argv[0])
sys.path.insert(0, root_path)

from substation_cmip_data_coordinates_map import SubstationCMIPDataCoordinatesMap
from constants import Constants


# DA Manager Class
class DAManager:
    # Constructor
    def __init__(self):
        source_file = Constants.SUBSTATION_CMIP_DATA_COORDINATES_PROCESSED_FILE
        self.substation_cmip_data_coordinates_map = SubstationCMIPDataCoordinatesMap(source_file)
