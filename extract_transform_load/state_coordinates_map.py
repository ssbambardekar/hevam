# Imports
from state_coordinates import StateCoordinates


# State Coordinates Map Class
class StateCoordinatesMap:
    # Constructor
    def __init__(self) -> None:
        self.states_by_coordinates = []
        self._populate_states_by_coordinates_map()        

    # Populate states by coordinates map
    def _populate_states_by_coordinates_map(self):
        self.states_by_coordinates.append(StateCoordinates(latitude=44.500000, longitude=-89.500000, state="Wisconsin"))
        self.states_by_coordinates.append(StateCoordinates(latitude=39.000000, longitude=-80.500000, state="West Virginia"))
        self.states_by_coordinates.append(StateCoordinates(latitude=44.000000, longitude=-72.699997, state="Vermont"))
        self.states_by_coordinates.append(StateCoordinates(latitude=31.000000, longitude=-100.000000, state="Texas"))
        self.states_by_coordinates.append(StateCoordinates(latitude=44.500000, longitude=-100.000000, state="South Dakota"))

        self.states_by_coordinates.append(StateCoordinates(latitude=41.742325, longitude=-71.742332, state="Rhode Island"))
        self.states_by_coordinates.append(StateCoordinates(latitude=44.000000, longitude=-120.500000, state="Oregon"))
        self.states_by_coordinates.append(StateCoordinates(latitude=43.000000, longitude=-75.000000, state="New York"))
        self.states_by_coordinates.append(StateCoordinates(latitude=44.000000, longitude=-71.500000, state="New Hampshire"))
        self.states_by_coordinates.append(StateCoordinates(latitude=41.500000, longitude=-100.000000, state="Nebraska"))
            
        self.states_by_coordinates.append(StateCoordinates(latitude=38.500000, longitude=-98.000000, state="Kansas"))
        self.states_by_coordinates.append(StateCoordinates(latitude=33.000000, longitude=-90.000000, state="Mississippi"))
        self.states_by_coordinates.append(StateCoordinates(latitude=40.000000, longitude=-89.000000, state="Illinois"))
        self.states_by_coordinates.append(StateCoordinates(latitude=39.000000, longitude=-75.500000, state="Delaware"))
        self.states_by_coordinates.append(StateCoordinates(latitude=41.599998, longitude=-72.699997, state="Connecticut"))

        self.states_by_coordinates.append(StateCoordinates(latitude=34.799999, longitude=-92.199997, state="Arkansas"))
        self.states_by_coordinates.append(StateCoordinates(latitude=40.273502, longitude=-86.126976, state="Indiana"))
        self.states_by_coordinates.append(StateCoordinates(latitude=38.573936, longitude=-92.603760, state="Missouri"))
        self.states_by_coordinates.append(StateCoordinates(latitude=27.994402, longitude=-81.760254, state="Florida"))
        self.states_by_coordinates.append(StateCoordinates(latitude=39.876019, longitude=-117.224121, state="Nevada"))
                        
        self.states_by_coordinates.append(StateCoordinates(latitude=45.367584, longitude=-68.972168, state="Maine"))
        self.states_by_coordinates.append(StateCoordinates(latitude=44.182205, longitude=-84.506836, state="Michigan"))
        self.states_by_coordinates.append(StateCoordinates(latitude=33.247875, longitude=-83.441162, state="Georgia"))
        self.states_by_coordinates.append(StateCoordinates(latitude=19.741755, longitude=-155.844437, state="Hawaii"))
        self.states_by_coordinates.append(StateCoordinates(latitude=66.160507, longitude=-153.369141, state="Alaska"))

        self.states_by_coordinates.append(StateCoordinates(latitude=35.860119, longitude=-86.660156, state="Tennessee"))
        self.states_by_coordinates.append(StateCoordinates(latitude=37.926868, longitude=-78.024902, state="Virginia"))
        self.states_by_coordinates.append(StateCoordinates(latitude=39.833851, longitude=-74.871826, state="New Jersey"))
        self.states_by_coordinates.append(StateCoordinates(latitude=37.839333, longitude=-84.270020, state="Kentucky"))
        self.states_by_coordinates.append(StateCoordinates(latitude=47.650589, longitude=-100.437012, state="North Dakota"))
            
        self.states_by_coordinates.append(StateCoordinates(latitude=46.392410, longitude=-94.636230, state="Minnesota"))
        self.states_by_coordinates.append(StateCoordinates(latitude=36.084621, longitude=-96.921387, state="Oklahoma"))
        self.states_by_coordinates.append(StateCoordinates(latitude=46.965260, longitude=-109.533691, state="Montana"))
        self.states_by_coordinates.append(StateCoordinates(latitude=47.751076, longitude=-120.740135, state="Washington"))
        self.states_by_coordinates.append(StateCoordinates(latitude=39.419220, longitude=-111.950684, state="Utah"))

        self.states_by_coordinates.append(StateCoordinates(latitude=39.113014, longitude=-105.358887, state="Colorado"))
        self.states_by_coordinates.append(StateCoordinates(latitude=40.367474, longitude=-82.996216, state="Ohio"))
        self.states_by_coordinates.append(StateCoordinates(latitude=32.318230, longitude=-86.902298, state="Alabama"))
        self.states_by_coordinates.append(StateCoordinates(latitude=42.032974, longitude=-93.581543, state="Iowa"))
        self.states_by_coordinates.append(StateCoordinates(latitude=34.307144, longitude=-106.018066, state="New Mexico"))
            
        self.states_by_coordinates.append(StateCoordinates(latitude=33.836082, longitude=-81.163727, state="South Carolina"))
        self.states_by_coordinates.append(StateCoordinates(latitude=41.203323, longitude=-77.194527, state="Pennsylvania"))
        self.states_by_coordinates.append(StateCoordinates(latitude=34.048927, longitude=-111.093735, state="Arizona"))
        self.states_by_coordinates.append(StateCoordinates(latitude=39.045753, longitude=-76.641273, state="Maryland"))
        self.states_by_coordinates.append(StateCoordinates(latitude=42.407211, longitude=-71.382439, state="Massachusetts"))

        self.states_by_coordinates.append(StateCoordinates(latitude=36.778259, longitude=-119.417931, state="California"))
        self.states_by_coordinates.append(StateCoordinates(latitude=44.068203, longitude=-114.742043, state="Idaho"))
        self.states_by_coordinates.append(StateCoordinates(latitude=43.075970, longitude=-107.290283, state="Wyoming"))
        self.states_by_coordinates.append(StateCoordinates(latitude=35.782169, longitude=-80.793457, state="North Carolina"))
        self.states_by_coordinates.append(StateCoordinates(latitude=30.391830, longitude=-92.329102, state="Louisiana"))