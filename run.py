import search

mi_problema = search.GPSProblem('A', 'B', search.romania)
print search.breadth_first_graph_search(mi_problema)
print search.depth_first_graph_search(mi_problema)

