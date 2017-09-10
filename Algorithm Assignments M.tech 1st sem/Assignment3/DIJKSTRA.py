import queue
from collections import namedtuple

Edge = namedtuple('Edge', ['vertex', 'weight'])


class GraphUndirectedWeighted(object):
    def __init__(self, vertex_count):
        self.vertex_count = vertex_count
        # Contains the list of vertices in the graph
        self.adjacency_list = [[] for _ in range(vertex_count)]

    def add_edge(self, source, dest, weight):
        if source < self.vertex_count and dest < self.vertex_count:
            # Add an entry of edge between the source and destination vertex
            self.adjacency_list[source].append(Edge(dest, weight))
            self.adjacency_list[dest].append(Edge(source, weight))


    def get_edge(self, vertex):
        for e in self.adjacency_list[vertex]:
            yield e

    def get_vertex(self):
        for v in range(self.vertex_count):
            yield v



"""
Dijkstra Algorithm
This function takes the graph and find the minimum distance
between the source node and the destination node
"""
def dijkstra(graph, source, dest):
    q = queue.PriorityQueue()
    parents = []
    distances = []
    start_weight = float("inf")

    """
    Initialize the weight oof source vertex to 0 and all
    other vertex to a large value i.e infinity
    """
    for i in graph.get_vertex():
        weight = start_weight
        if source == i:
            weight = 0
        distances.append(weight)
        parents.append(None)

    q.put(([0, source]))

    """
    For each entry in the heap + map data structure pop the
    minimum element and find the adjacent vertex for the
    popped out element
    """
    while not q.empty():
        v_tuple = q.get()
        v = v_tuple[1]

        for e in graph.get_edge(v):
            candidate_distance = distances[v] + e.weight
            if distances[e.vertex] > candidate_distance:
                distances[e.vertex] = candidate_distance
                parents[e.vertex] = v
                # primitive but effective negative cycle detection
                if candidate_distance < -1000:
                    raise Exception("Negative cycle detected")
                q.put(([distances[e.vertex], e.vertex]))

    shortest_path = []
    end = dest
    while end is not None:
        shortest_path.append(end)
        end = parents[end]

    shortest_path.reverse()

    return shortest_path, distances[dest]



if __name__ == "__main__":
    g = GraphUndirectedWeighted(6)
    g.add_edge(0, 1, 2)
    g.add_edge(0, 5, 4)
    g.add_edge(0, 3, 5)
    g.add_edge(1, 2, 4)
    g.add_edge(2, 5, 3)
    g.add_edge(5, 3, 2)
    g.add_edge(3, 4, 1)

    # Print the graph
    print("Graph")
    for i in g.get_vertex():
        for j in g.get_edge(i):
            print(i,j)

    # Print the final Result
    print("Final Result")
    print("Source    Node    Distance    Path")
    for l in range(0,5):
        shortest_path, distance = dijkstra(g, 0, l)
        print("  {0}         {1}        {2}        {3}".format(0,l,distance,shortest_path))
