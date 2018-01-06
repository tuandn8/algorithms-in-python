from collections import defaultdict
  
#This class represents an undirected graph using adjacency list representation
class Graph:
  
    def __init__(self,vertices):
        self.V= vertices #No. of vertices
        self.graph = defaultdict(list) # default dictionary to store graph
        self.time = 0
  
    # function to add an edge to graph
    def add_edge(self,u,v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def bridgeUtil(self, u, visited, parent, low, disc):
        children = 0
        visited[u] = True

        disc[u] = self.time
        low[u] = self.time
        self.time += 1

        for v in self.graph[u]:
            if visited[v] == False:
                parent[v] = u
                children += 1

                self.bridgeUtil(v, visited, parent, low, disc)

                low[u] = min(low[u], low[v])

                if low[v] > disc[u]:
                    print("%d-%d" % (u, v))

            elif v != parent[u]:
                low[u] = min(low[u], disc[v])

    def bridge(self):
        visited = [False] * (self.V)
        disc = [float("Inf")] * (self.V)
        low = [float("Inf")] * (self.V)
        parent = [-1] * (self.V)

        for i in range(self.V):
            if visited[i] == False:
                self.bridgeUtil(i, visited, parent, low, disc)


# Create a graph given in the above diagram
g1 = Graph(5)
g1.add_edge(1, 0)
g1.add_edge(0, 2)
g1.add_edge(2, 1)
g1.add_edge(0, 3)
g1.add_edge(3, 4)
 
  
print ("Bridges in first graph ")
g1.bridge()
 
g2 = Graph(4)
g2.add_edge(0, 1)
g2.add_edge(1, 2)
g2.add_edge(2, 3)
print ("\nBridges in second graph ")
g2.bridge()
 
  
g3 = Graph (7)
g3.add_edge(0, 1)
g3.add_edge(1, 2)
g3.add_edge(2, 0)
g3.add_edge(1, 3)
g3.add_edge(1, 4)
g3.add_edge(1, 6)
g3.add_edge(3, 5)
g3.add_edge(4, 5)
print ("\nBridges in third graph ")
g3.bridge()
 