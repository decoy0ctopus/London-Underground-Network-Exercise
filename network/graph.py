class NeighbourGraphBuilder:
    """
    Task 2: Complete the definition of the NeighbourGraphBuilder class by:
    - completing the "build" method below (don't hesitate to divide your code into several sub-methods, if needed)
    """

    def __init__(self):
        pass

    def build(self, tubemap):
        """ Builds a graph encoding neighbouring connections between stations.

        ----------------------------------------------

        The returned graph should be a dictionary having the following form:
        {
            "station_A_id": {
                "neighbour_station_1_id": [
                                connection_1 (instance of Connection),
                                connection_2 (instance of Connection),
                                ...],

                "neighbour_station_2_id": [
                                connection_1 (instance of Connection),
                                connection_2 (instance of Connection),
                                ...],
                ...
            }

            "station_B_id": {
                ...
            }

            ...

        }

        ----------------------------------------------

        For instance, knowing that the id of "Hammersmith" station is "110",
        graph['110'] should be equal to:
        {
            '17': [
                Connection(Hammersmith<->Barons Court, District Line, 1),
                Connection(Hammersmith<->Barons Court, Piccadilly Line, 2)
                ],

            '209': [
                Connection(Hammersmith<->Ravenscourt Park, District Line, 2)
                ],

            '101': [
                Connection(Goldhawk Road<->Hammersmith, Hammersmith & City Line, 2)
                ],

            '265': [
                Connection(Hammersmith<->Turnham Green, Piccadilly Line, 2)
                ]
        }

        ----------------------------------------------

        Args:
            tubemap (TubeMap) : tube map serving as a reference for building the graph.

        Return:
            graph (dict) : as described above.

        Note:
            If the input data (tubemap) is invalid, the method should return an empty dict.
        """

        graph ={}

		#iterate through stations in the tubemap

        for station in tubemap.stations:

            graph_connections = {}

			#for each connection to each station, add the connection stations to a dict

            for connection in tubemap.connections:

                if tubemap.stations[station] in connection.stations:

                    for con_stn in connection.stations:

                        if tubemap.stations[station] != con_stn and con_stn in connection.stations:

                            if con_stn.id not in graph_connections:
                            
                                graph_connections[con_stn.id] = [connection]

                            else:

                                graph_connections[con_stn.id] += [connection]                  


            graph[station] = graph_connections
                        
        return graph 


def test_graph():
    from tube.map import TubeMap
    tubemap = TubeMap()
    tubemap.import_from_json("data/london.json")

    graph_builder = NeighbourGraphBuilder()
    graph = graph_builder.build(tubemap)

    print(graph['110'])
    print(graph["11"]["163"])
    print(graph["163"]["11"])


if __name__ == "__main__":
    test_graph()
