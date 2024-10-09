#Imports
import pandas as pd
pd.options.mode.chained_assignment = None  # default='warn'; do not care about chained assignments warning "A value is trying to be set on a copy of a slice from a DataFrame"


# DA Processor Base Class
# Holds common methods for all processors
class DAProcessorBase:
    # Constructor
    def __init__(self):
        pass
        
    # Print da begin message
    def _print_da_begin(self, source_file_absolute_path, analyzed_file_absolute_path):
        print("Starting DA Processing...")
        print("Source File: ", source_file_absolute_path)
        print("Analyzed File: ", analyzed_file_absolute_path)
            
    # Print da end message
    def _print_da_end(self):
        print("DA Processing Completed")            

    # Print da error message
    def _print_da_error(self, error):
        print("DA Processing Error: ", error)
    