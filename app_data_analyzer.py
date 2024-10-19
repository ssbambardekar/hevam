# Imports
import sys
import os
from sys import argv

root_path = os.path.dirname(argv[0])
data_analysis_module_path = root_path + '/data_analysis'
sys.path.insert(0, data_analysis_module_path)

from da_manager import DAManager 
from constants import Constants


# Get inputs
print("Welcome to Hevam Data Analyer!")

threshold_temperature = 0
while (True):
    threshold_temperature_string = input("Enter threshold temperature for calculations: ")
    try:
        threshold_temperature = int(threshold_temperature_string)
        break
    except Exception as error:
        continue

exposure_operation = Constants.EXPOSURE_OPERATION_GREATER_THAN
while (True):
    exposure_operation = input("Enter exposure operation for calculations (gt=greater than, lt=less than): ")
    if exposure_operation == "gt" or exposure_operation == "lt":
        break
    else:
        continue

print("Starting Data Analysis...")

# Create da manager
da_manager = DAManager()

# Steps - NOTE: The order of steps matters, as processed files of some steps serve as inputs to the next steps
# DA substation exposure
da_manager.da_substations_exposure(threshold_temperature, exposure_operation)
