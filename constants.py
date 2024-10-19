# Constants
class Constants:
    # Version
    VERSION = "1.0.0"

    # Exposure operation = greater than
    EXPOSURE_OPERATION_GREATER_THAN = "gt"

    # Exposure operation = less than
    EXPOSURE_OPERATION_LESS_THAN = "lt"

    # CMIP data daily max temperature source folder name
    CMIP_DATA_DAILY_MAX_TEMPERATURE_SOURCE_FOLDER = "/data/source/cmip_data/daily_max_temperature"

    # CMIP data daily max temperature processed folder name, relative to the root data folder
    CMIP_DATA_DAILY_MAX_TEMPERATURE_PROCESSED_FOLDER = "/data/processed/generated"

    # CMIP data daily max temperature analyzed folder name, relative to the root data folder
    CMIP_DATA_DAILY_MAX_TEMPERATURE_ANALYZED_FOLDER = "/data/processed/analyzed"

    # Substations source file, relative to the root data folder
    SUBSTATIONS_SOURCE_FILE = "/data/source/power grid data/substations.json"

    # Substations processed file name, relative to the root data folder
    SUBSTATIONS_PROCESSED_FILE = "/data/processed/generated/substations.csv"

    # Power grids source file name, relative to the root data folder
    POWER_GRIDS_SOURCE_FILE = "/data/source/power grid data/grid_mapping.csv"

    # Power grid processed file name, relative to the root data folder
    POWER_GRIDS_PROCESSED_FILE = "/data/processed/generated/power_grids.csv"
    
    # Substation state processed file name, relative to the root data folder 
    SUBSTATION_STATES_PROCESSED_FILE = "/data/processed/generated/substations_states.csv"

    # CMIP data daily max temperature 2025 processed file name, relative to the root data folder 
    CMIP_DATA_DAILY_MAX_TEMPERATURE_2025_PROCESSED_FILE = "/data/processed/generated/cmip_data_daily_max_temperatures_2025.csv"

    # Substations cmip data coordinates processed file name, relative to the root data folder 
    SUBSTATION_CMIP_DATA_COORDINATES_PROCESSED_FILE = "/data/processed/generated/substations_cmip_data_coordinates.csv"

    # File name prefix for daily max temperature
    FILE_NAME_PREFIX_DAILY_MAX_TEMPERATURE = "daily_max_temperatures_"

    # File name prefix for cmip data daily max temperature
    FILE_NAME_PREFIX_CMIP_DATA_DAILY_MAX_TEMPERATURE = "cmip_data_daily_max_temperatures_"

    # File name prefix for substation exposure threshold temperature
    FILE_NAME_PREFIX_SUBSTATION_EXPOSURE_THRESHOLD_TEMPERATURE = "substation_exposure_temperature_"

    # File name suffix for year
    FILE_NAME_PREFIX_THRESHOLD_TEMPERATURE = "year_"
   
    # Data points names
    LATITUDE_HEADER_NAME = "Latitude"
    LONGITUDE_HEADER_NAME = "Longitude"
    SUBSTATION_LATITUDE_HEADER_NAME = "Substation Latitude"
    SUBSTATION_LONGITUDE_HEADER_NAME = "Substation Longitude"
    CMIP_DATA_LATITUDE_HEADER_NAME = "CMIP Data Latitude"
    CMIP_DATA_LONGITUDE_HEADER_NAME = "CMIP Data Longitude"    
    POWER_GRID_COMPONENT_HEADER_NAME = "Power Grid Component"
    DAILY_MAX_TEMPERATURE_HEADER_NAME = "Daily Max Temperature"
    TIME_HEADER_NAME = "Time"
    STATE_HEADER_NAME = "State"
    SUBSTATION_NAME = "Substation Name"
    SUBSTATION_TYPE = "Substation Type"
    SUBSTATION_VOLTAGE = "Substation Voltage"
    
