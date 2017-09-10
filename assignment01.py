

def treePaths(graph, start, goal):
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)
        for next in graph[vertex] - set(path):
            if next == goal:
                yield path + [next]
            else:
                queue.append((next, path + [next]))

    
         
graph1 = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'G']),
         'D': set(['B']),
         'E': set(['B', 'G']),
         'G':set(['C','E','F']) ,       
         'F': set(['G'])}         

g={}
g=list(treePaths(graph1, 'A', 'F'))

s='A'
d='F'
print(list(treePaths(graph1, s, d))) # [['A', 'C', 'F'], ['A', 'B', 'E', 'F']]


paths = g

try:
  common = set(paths[0]).intersection(*paths)
except ValueError:
    
    common = set()

common.remove(s)
common.remove(d)    
print("crucial nodes :",common)
print()         