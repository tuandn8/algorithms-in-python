# A directed graph has Euler cycle if
#   - All vertices with nonzero degree belong to a single strongly connected 
#       component
#   - In degree and out degree of every vertex is same

from collections import defaultdict


class Graph:

    def __init__(self, vertices):
        self.V = vertices  # No. of vertices
        self.graph = defaultdict(list)  # default dictionary to store graph
        self.IN  = [0] * self.V

    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.IN[v] += 1

    def DFSUtil(self, v, visited):
        visited[v] = True

        for i in self.graph[v]:
            if visited[i] == False:
                self.DFSUtil(i, visited)

    def getTranspose(self):
        gr = Graph(self.V)

        for node in range(self.V):
            for child in self.graph[node]:
                gr.addEdge(child, node)

        return gr

    def isSC(self):
        visited = [False] * self.V

        v = 0
        for v in range(self.V):
            if len(self.graph[v]) > 0: 
                break

        self.DFSUtil(v, visited)

        # If DFS not visit all node, return False
        for i in range(self.V):
            if visited[i] == False:
                return False 
        
        gr = self.getTranspose()

        visited = [False] * self.V
        gr.DFSUtil(v, visited)

        for i in range(self.V):
            if visited[i] == False:
                return False

        return True

    def isEulerCycle(self):
        # Check if all non-zero degree vertices are connected
        if self.isSC() == False:
            return False

        # Check if in degree and out degree of every vertex is same
        for v in range(self.V):
            if self.IN[v] != len(self.graph[v]):
                return False
        
        return True


g = Graph(5)
g.addEdge(1, 0)
g.addEdge(0, 2)
g.addEdge(2, 1)
g.addEdge(0, 3)
g.addEdge(3, 4)
g.addEdge(4, 0)
if g.isEulerCycle():
   print ("Given directed graph is eulerian")
else:
   print ("Given directed graph is NOT eulerian")
