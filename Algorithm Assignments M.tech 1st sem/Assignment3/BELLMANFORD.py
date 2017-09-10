class Vertex:
    def __init__(self, node):
        self.id = node
        self.adjacent = {}
        # Set distance to infinity for all nodes
        self.distance = 10000
        #Parent
        self.parent = None

    def add_neighbor(self, neighbor, weight=0):
        self.adjacent[neighbor] = weight

    def get_connections(self):
        return self.adjacent.keys()

    def get_id(self):
        return self.id

    def get_weight(self, neighbor):
        return self.adjacent[neighbor]

    def set_distance(self, dist):
        self.distance = dist

    def get_distance(self):
        return self.distance

    def set_parent(self,node):
        self.parent = node

    def get_parent(self):
        return self.parent

    def __str__(self):
        return str(self.id) + ' adjacent: ' + str([x.id for x in self.adjacent])




class Graph:
    def __init__(self):
        self.vert_dict = {}
        self.num_vertices = 0

    def __iter__(self):
        return iter(self.vert_dict.values())

    def add_vertex(self, node):
        self.num_vertices = self.num_vertices + 1
        new_vertex = Vertex(node)
        self.vert_dict[node] = new_vertex
        return new_vertex

    def get_vertex(self, n):
        if n in self.vert_dict:
            return self.vert_dict[n]
        else:
            return None

    def add_edge(self, frm, to, cost=0):
        if frm not in self.vert_dict:
            self.add_vertex(frm)
        if to not in self.vert_dict:
            self.add_vertex(to)

        self.vert_dict[frm].add_neighbor(self.vert_dict[to], cost)

    def get_vertices(self):
        return self.vert_dict.keys()




# Bellman Ford Algorithm
def bellmanFord(aGraph,sequence):
    #print(aGraph)
    output = []

    aGraph.get_vertex('a').set_distance(0)

    for i in range(0,4):
        print("Iteration ",i+1)
        for pair in sequence:
            u = pair[0]
            v = pair[1]
            print("Sequence {0}->{1}".format(u,v))
            for ver in aGraph:
                for w in ver.get_connections():
                    a1 = ver.get_id()
                    a2 = w.get_id()
                    if a1 == u and a2 == v:
                        disV = int(aGraph.get_vertex(v).get_distance())
                        disU = int(aGraph.get_vertex(u).get_distance())
                        weight = int(ver.get_weight(w))
                        #print(disV,disU,weight)
                        if disV > disU + weight:
                            aGraph.get_vertex(v).set_distance(disU+weight)
                            aGraph.get_vertex(v).set_parent(u)

        print('Vertex', 'Distance', 'Parent')
        for ver in aGraph:
            print("  {0},    {1},       {2}".format(ver.get_id(), ver.get_distance(), ver.get_parent()))
        print("\n")


    print("=====Final Result=====")
    print('Vertex', 'Distance', 'Parent')
    for ver in aGraph:
        print("  {0}    {1}       {2}".format(ver.get_id(), ver.get_distance(), ver.get_parent()))





# Driver Function
if __name__ == "__main__":
    g = Graph()

    g.add_vertex('a')
    g.add_vertex('b')
    g.add_vertex('c')
    g.add_vertex('d')
    g.add_vertex('e')
    #g.add_vertex('f')


    g.add_edge('a','b',-1)
    g.add_edge('a', 'c', 4)
    g.add_edge('b', 'c', 3)
    g.add_edge('b', 'd', 2)
    g.add_edge('b', 'e', 2)
    g.add_edge('d','b',1)
    g.add_edge('e', 'd', -3)
    #g.add_edge('f', 'e', 1)

    print('Graph data:')
    for v in g:
        for w in v.get_connections():
            vid = v.get_id()
            wid = w.get_id()
            print('( %s , %s, %3d)' % (vid, wid, v.get_weight(w)))


    # define a random sequence
    sequence = [['b','e'],['d','b'],['b','d'],['a','b'],['a','c'],['d','c'],['b','c'],['e','d']]
    bellmanFord(g, sequence)