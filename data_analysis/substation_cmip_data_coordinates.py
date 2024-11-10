# Substation CMIP Data Coordinates Class
class SubstationCMIPDataCoordinates:
    # Constructor
    def __init__(self, substation_latitude, substation_longitude, substation_state, cmip_data_latitude, cmip_data_longitude):
        self.substation_latitude = substation_latitude
        self.substation_longitude = substation_longitude
        self.substation_state = substation_state
        self.cmip_data_latitude = cmip_data_latitude
        self.cmip_data_longitude = cmip_data_longitude
