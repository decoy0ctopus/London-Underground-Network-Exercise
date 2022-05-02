import json

from tube.components import Station, Connection, Line

class TubeMap:
    """
    Task 1: Complete the definition of the TubeMap class by:
    - completing the "import_from_json" method (don't hesitate to divide your code into several sub-methods, if needed)

    As a minimum, the TubeMap class must contain these three member attributes:
    - stations: a dictionary that indexes Station instances by their id (key=id, value=Station)
    - lines: a dictionary that indexes Line instances by their id (key=id, value=Line)
    - connections: a list of Connection instances for the tube map (list of Connections)
    """

    def __init__(self):
        self.stations = {}  # key: id, value: Station
        self.lines = {}  # key: id, value: Line
        self.connections = []  # list of Connections

    def import_from_json(self, filepath):
        """ Import tube map information from a JSON file.
        
        During that import, the `stations`, `lines` and `connections` attributes should be updated.

        You can use the `json` python package to easily load the JSON file at `filepath`

        Note: when the indicated zone is not an integer (for instance: 2.5), 
            it means that the station is in two zones at the same time. 
            For example, if the zone of a station is "2.5", 
            it means that station is in zones 2 and 3.

        Args:
            filepath (str) : relative or absolute path to the JSON file 
                containing all the information about the tube map graph to import

        Returns:
            None

        Note:
            If the filepath is invalid, no attribute should be updated, and no error should be raised.
        """
        #Open the dataset from filepath and load into list of dictionaries 'data'
        file = open(filepath)
        data = json.load(file)

        #Iterate through each column creating a new item for each Station & Line using the classes defined in components
        for station in data['stations']:
            self.stations[station['id']] = Station(station['id'], station['name'], station['zone'])
        for line in data['lines']:
            self.lines[line['line']] = Line(line['line'], line['name'])
        
        #For connections we do the same but iterate through each item to add each station in the connection
        #to a set called stations before appending this to a list called connections.
        for connect in data['connections']:
            stations = set()
            for key, value in connect.items():
                if key.startswith('station'):   #find all keys that start with station and add these values to the set
                    stations.add(self.stations[f"{value}"])
            self.connections.append(Connection(stations, self.lines[f"{connect['line']}"], connect['time']))
        return


def test_import():
    tubemap = TubeMap()
    tubemap.import_from_json("data/london.json")

    # view one example Station
    print(tubemap.stations[list(tubemap.stations)[0]])
    
    # view one example Line
    print(tubemap.lines[list(tubemap.lines)[0]])
    
    # view the first Connection
    print(tubemap.connections[0])
    
    # view stations for the first Connection
    print([station for station in tubemap.connections[0].stations])


if __name__ == "__main__":
    test_import()
