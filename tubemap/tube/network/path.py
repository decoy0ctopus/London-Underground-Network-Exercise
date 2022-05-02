from numpy import Infinity
from network.graph import NeighbourGraphBuilder

class PathFinder:
    """
    Task 3: Complete the definition of the PathFinder class by:
    - completing the definition of the __init__ method (if needed)
    - completing the "get_shortest_path" method (don't hesitate to divide your code into several sub-methods)
    """

    def __init__(self, tubemap):
        """
        Args:
            tubemap (TubeMap) : The TubeMap to use.
        """
        self.tubemap = tubemap
        graph_builder = NeighbourGraphBuilder()
        self.graph = graph_builder.build(self.tubemap)
        
        # Feel free to add anything else needed here.

    def get_shortest_path(self, start_station_name, end_station_name):

        """ Find ONE shortest path (in terms of duration) from start_station_name to end_station_name.

        For instance, get_shortest_path('Stockwell', 'South Kensington') should return the list:
        [Station(245, Stockwell, {2}), 
         Station(272, Vauxhall, {1, 2}), 
         Station(198, Pimlico, {1}), 
         Station(273, Victoria, {1}), 
         Station(229, Sloane Square, {1}), 
         Station(236, South Kensington, {1})
        ]

        If start_station_name or end_station_name does not exist, return None.

        Args:
            start_station_name (str): name of the starting station
            end_station_name (str): name of the ending station

        Returns:
            list[Station] : list of Station objects corresponding to ONE 
                shortest path from start_station_name to end_station_name.
                Returns None if start_station_name or end_station_name does not exist.
        """

        station_name_list = self.tubemap.stations # Get list of stations
        visited = set() #Empty set to put in stations already visited

        for station_id in self.graph:

            if station_name_list[station_id].name == start_station_name:
                #If station name matches start station name add to shortest paths
                shortest_paths = {station_id: (None, 0)}
                current_stn = station_id

        while station_name_list[current_stn].name != end_station_name:

            visited.add(current_stn)
            destinations = self.graph[current_stn].items()
            weight_to_current_station = shortest_paths[current_stn][1]

            for neighbour_stn, connections in destinations:

                weight = int(connections[0].time) + weight_to_current_station

                if neighbour_stn not in shortest_paths:

                    shortest_paths[neighbour_stn] = (current_stn, weight)

                else:

                    current_shortest_weight = shortest_paths[neighbour_stn][1]

                    if current_shortest_weight > shortest_paths[neighbour_stn][1]:

                        shortest_paths[neighbour_stn] = (current_stn, weight)

            next_destinations = {node: shortest_paths[node] for node in shortest_paths if node not in visited}

            if not next_destinations:
                return None

            current_stn = min(next_destinations, key=lambda k: next_destinations[k][1])

        path = []
        while current_stn is not None:
            path.append(station_name_list[current_stn])
            next_node = shortest_paths[current_stn][0]
            current_stn = next_node
        # Reverse path
        path = path[::-1]
        return path



def test_shortest_path():
    from tube.map import TubeMap
    tubemap = TubeMap()
    tubemap.import_from_json("data/london.json")
    
    path_finder = PathFinder(tubemap)
    stations = path_finder.get_shortest_path("Covent Garden", "Green Park")
    print(stations)
    
    station_names = [station.name for station in stations]
    expected = ["Covent Garden", "Leicester Square", "Piccadilly Circus", 
                "Green Park"]
    assert station_names == expected


if __name__ == "__main__":
    test_shortest_path()
