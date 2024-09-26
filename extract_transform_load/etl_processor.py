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


# Generic ETL Processor Class
class ETLProcessor:
    # Constructor
    def __init__(self) -> None:
        pass

    def process_file(self, source_file, processed_file, columns_to_be_extracted):        
        try:
            # Set the paths
            source_file_absolute_path = root_path + "/" + source_file
            processed_file_absolute_path = root_path + "/" + processed_file 

            # Print info
            print("Starting ETL Processing")
            print("Source File: ", source_file_absolute_path)
            print("Processed File: ", processed_file_absolute_path)
            print("Columns For Extraction: ", columns_to_be_extracted)

            # Load the source file
            extracted_data_frames = pd.read_csv(source_file_absolute_path, usecols=columns_to_be_extracted)

            # Reorder the columns as specified
            extracted_data_frames = extracted_data_frames[columns_to_be_extracted]
            
            # Drop nulls
            extracted_data_frames.dropna(inplace = True)

            # De-dup
            extracted_data_frames.drop_duplicates(inplace = True) 

            # Save the extracted data to processed file
            extracted_data_frames.to_csv(processed_file_absolute_path, index=False)

            print("ETL Processing Completed")            
        except Exception as error:
            print("ETL Processing Error: ", error)


# Debug Code
if __name__ == "__main__":
    etl_processor = ETLProcessor()
    columns_to_be_extracted = ["Latitude", "Longitude"]
    etl_processor.process_file(Constants.GRID_MAPPING_SOURCE_FILE, "/data/processed/test_coordinates.csv", columns_to_be_extracted)