# Imports
import sys
import os
from sys import argv
import pandas as pd

# Set imports path for data
root_path = os.path.dirname(os.path.dirname(argv[0]))
source_data_root_path = root_path + "/data/source"
sys.path.insert(0, source_data_root_path)
processed_data_root_path = root_path + "/data/processed"
sys.path.insert(0, processed_data_root_path)


# Generic ETL Manager Class
class ETLManager:
    # Constructor
    def __init__(self) -> None:
        pass

    def process_file(self, source_file_name, processed_file_name, columns_to_be_extracted):        
        try:
            # Set the paths
            source_file_path = source_data_root_path + "/" + source_file_name
            processed_file_path = processed_data_root_path + "/" + processed_file_name 

            # Print info
            print("Starting ETL Processing")
            print("Source File: ", source_file_path)
            print("Processed File: ", processed_file_path)
            print("Columns For Extraction: ", columns_to_be_extracted)
            
            # Load the source file
            extracted_data_frames = pd.read_csv(source_file_path, usecols=columns_to_be_extracted)

            # Save the extracted data to processed file
            extracted_data_frames.to_csv(processed_file_path)

            print("ETL Processing Completed")            
        except Exception as error:
            print("ETL Processing Error: ", error)


# Debug Code
if __name__ == "__main__":
    etl_manager = ETLManager()
    columns_to_be_extracted = ["Latitude", "Longitude"]
    etl_manager.process_file("power grid data/grid_mapping.csv", "test_coordinates.csv", columns_to_be_extracted)