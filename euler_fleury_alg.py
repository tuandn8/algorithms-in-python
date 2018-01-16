# Find euler cycle/path in undirected graph by Fleury algorithm
# Make sure the graph has 0 or 2 odd vertices
# If there 0 odd vertices, start anywhere. If there 2 odd vertices, start at one of them
# Follow the edges one at a time. If you have a choice between a bridge and 
# non-bridge, always choose non-bridge
# Stop when you run out of edges.
# Remember that the complexity of this Algorithm is O((V+E)^2)

from collections import defaultdict


class Graph:

    def __init__(self, vertices):
        self.V = vertices  # No. of vertices
        self.graph = defaultdict(list)  # default dictionary to store graph
        self.time = 0

    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def rmvEdge(self, u, v):
        for index, key in enumerate(self.graph[u]):
            if key == v:
                self.graph[u].pop(index)

        for index, key in enumerate(self.graph[v]):
            if key == u:
                self.graph[v].pop(index)

    def DFSCount(self, v, visited):
        count = 1
        visited[v] = True
        for i in self.graph[v]:
            if visited[i] == False:
                count = count + self.DFSCount(i, visited)
        
        return count

    def isValidNextEdge(self, u, v):
        # the edge u-v is valid in one of the two case

        # 1. if v only adjacent vertex of u
        if len(self.graph[u]) == 1:
            return True
        else:
            # 2. If there are multiple adjacent 

            # Count number of vertices reachable from u
            visited = [False] * self.V
            count1 = self.DFSCount(u, visited)

            # Remove edge (u,v) and after remove count number of vertices reachable
            # from u
            self.rmvEdge(u, v)
            count2 = self.DFSCount(u, visited)

            # Re-add edge (u, v)
            self.addEdge(u, v)

            return False if count1 > count2 else True

    def printEulerUtil(self, u):
        for v in self.graph[u]:
            if self.isValidNextEdge(u, v):
                print("%d-%d " % (u, v))
                self.rmvEdge(u, v)
                self.printEulerUtil(v)

    def printEulerTour(self):
        u = 0
        for i in range(self.V):
            if len(self.graph[i]) % 2 != 0:
                u = i
                break
        
        print ("\n")
        self.printEulerUtil(u)

g1 = Graph(4)
g1.addEdge(0, 1)
g1.addEdge(0, 2)
g1.addEdge(1, 2)
g1.addEdge(2, 3)
g1.printEulerTour()


g2 = Graph(3)
g2.addEdge(0, 1)
g2.addEdge(1, 2)
g2.addEdge(2, 0)
g2.printEulerTour()

g3 = Graph(5)
g3.addEdge(1, 0)
g3.addEdge(0, 2)
g3.addEdge(2, 1)
g3.addEdge(0, 3)
g3.addEdge(3, 4)
g3.addEdge(3, 2)
g3.addEdge(3, 1)
g3.addEdge(2, 4)
g3.printEulerTour()
