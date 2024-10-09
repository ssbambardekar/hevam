# Imports
import sys
import os
from sys import argv

root_path = os.path.dirname(argv[0])
data_analysis_module_path = root_path + '/data_analysis'
sys.path.insert(0, data_analysis_module_path)

from da_manager import DAManager 


# Create da manager
da_manager = DAManager()

# Steps - NOTE: The order of steps matters, as processed files of some steps serve as inputs to the next steps
# DA substation exposure
da_manager.da_substations_exposure()
