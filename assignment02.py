import sys

class Graph(object):
    def __init__(self, graph_dict=None):
        """ initializes a graph object 
            If no dictionary or None is given, 
            an empty dictionary will be used
        """
        if graph_dict == None:
            graph_dict = {}
        self.__graph_dict = graph_dict

    def vertices(self):
        """ returns the vertices of a graph """
        return list(self.__graph_dict.keys())

    
    def is_connected(self, 
                        vertices_encountered = None, 
                        start_vertex=None):
        """ determines if the graph is connected """
        if vertices_encountered is None:
            vertices_encountered = set()
        gdict = self.__graph_dict        
        vertices = list(gdict.keys()) # "list" necessary in Python 3 
        if not start_vertex:
            # chosse a vertex from graph as a starting point
            start_vertex = vertices[0]
        vertices_encountered.add(start_vertex)
        if len(vertices_encountered) != len(vertices):
            for vertex in gdict[start_vertex]:
                if vertex not in vertices_encountered:
                    if self.is_connected(vertices_encountered, vertex):
                        return True
        else:
            return True
        return False

if __name__ == "__main__":

 g = { "a" : ["b","e","f"],
      "b" : ["a","c","d","f"],
      "c" : ["b","d","e"],
      "d" : ["b","c","e"],
      "e" : ["a","c","d","f"],
      "f" : ["a","b","e"]
     }
 g1= { "a" : ["b","e","f"],
      "b" : ["a","c","e","f"],
      "c" : ["b","f","e"],
      "d" : [],
      "e" : ["a","b","c","f"],
      "f" : ["a","b","c","e"]
    }

  
 #graph = Graph(g)

 #print(graph)
 #print(graph.is_connected())

 graph = Graph(g)
 print("the graph with all vertices with degree either n/2 or greater than n/2")
 print("graph g :",g)
 print("for graph g")
 print("min degree criteria :",graph.is_connected())

 graph = Graph(g1)
 print("")
 print(" graph g1 :",g1)
 print("for graph g1")
 print("min degree criteria :",graph.is_connected())    
