# Constants
class Constants:
    # Version
    VERSION = "1.0.0"

    # CMIP data daily max temperature source folder name
    CMIP_DATA_DAILY_MAX_TEMPERATURE_SOURCE_FOLDER = "/data/source/cmip_data/daily_max_temperature"

    # CMIP data daily max temperature processed folder name, relative to the root data folder
    CMIP_DATA_DAILY_MAX_TEMPERATURE_PROCESSED_FOLDER = "/data/processed"

    # Substations source file, relative to the root data folder
    SUBSTATIONS_SOURCE_FILE = "/data/source/power grid data/substations.json"

    # Substations processed file name, relative to the root data folder
    SUBSTATIONS_PROCESSED_FILE = "/data/processed/substations.csv"

    # Power grids source file name, relative to the root data folder
    POWER_GRIDS_SOURCE_FILE = "/data/source/power grid data/grid_mapping.csv"

    # Power grid processed file name, relative to the root data folder
    POWER_GRIDS_PROCESSED_FILE = "/data/processed/power_grids.csv"
    
    # Substation state processed file name, relative to the root data folder 
    SUBSTATION_STATES_PROCESSED_FILE = "/data/processed/substations_states.csv"



    # Grid components by coordinates processed file name, relative to the root data folder
    GRID_COMPONENTS_BY_COORDINATES_PROCESSED_FILE = "/data/processed/grid_components_by_coordinates.csv"

   
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
    
