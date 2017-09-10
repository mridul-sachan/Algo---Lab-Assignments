def floydWarshall(graph,gSize):
    output = []
    for k in range(0,gSize):
        for i in range(0,gSize):
            for j in range(0,gSize):
                a1 = graph[i][j]
                b1 = graph[i][k]
                c1 = graph[k][j]

                if a1 > b1 + c1:
                    graph[i][j] = b1+c1

    for row in graph:
        print(row)





if __name__ == "__main__":
    graph = [[0,5,1000,10],[1000,0,3,1000],[1000,1000,0,1],[1000,1000,1000,0]]
    floydWarshall(graph,4)
