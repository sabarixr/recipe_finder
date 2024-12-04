import networkx as nx
def find_recipes_dijkstra(graph, start_ingredient):
    return nx.single_source_dijkstra_path(graph, start_ingredient, weight="dietary_weight")