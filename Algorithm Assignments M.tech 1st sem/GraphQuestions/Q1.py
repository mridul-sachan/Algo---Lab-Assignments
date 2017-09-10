
def bfs(graph, start):
    vis = []
    visited, queue = set(), [start]
    while queue:
        vertex = queue.pop(0)
        print(vertex)
        if vertex not in visited:
            vis.append(vertex)
            visited.add(vertex)
            print("Visited", visited)
            queue.extend(graph[vertex] - visited)
            print(queue)
    return vis



def bfs_paths(graph, start, goal):
    queue = [(start, [start])]
    res_path = []
    prev_child = 0
    level = 0
    visited = []
    level_desc = []
    c = 0


    while queue:
        (vertex, path) = queue.pop(0)
        #print((vertex, path))
        childs = graph[vertex] - set(path)
        child_len = len(childs)

        for next in graph[vertex] - set(path):
            if next not in visited and prev_child == 0:
                c += 1
                prev_child = child_len
                level += 1
                level_desc.append((level, graph[vertex] - set(path),child_len))
                visited.append(next)

            if next == goal:
                res_path.append(path + [next])
            else:
                queue.append((next, path + [next]))
                prev_child -=1

    return res_path,level_desc





if __name__ == "__main__":
    graph = {'S': {'B', 'C'},
             'B': {'S', 'D'},
             'C': {'S', 'D'},
             'D': {'B', 'C', 'T'},
             'T': {'D'}}

    g2 = {"a": set(["b","c"]),
          "b": set(["c","f","a"]),
          "c": set(["d","b","a"]),
          "d": set(["e"]),
          "e": set([]),
          "f": set(["a"])
          }

    paths,level_desc = bfs_paths(graph,'S','T')


    con = 0

    for level in level_desc:
        if level[2] == 1:
            node = level[1].pop()
            for path in paths:
                if node in path:
                    #print('Yes')
                    print("The node that can be removed is: ",node)
                    con = 0
                    break

        else:
            con = -1

    if con == -1:
        print("No node can be removed")