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

    def DFSUtil(self, u, visited):
        visited[u] = True
        for v in self.graph[u]:
            if visited[v] == False:
                self.DFSUtil(v, visited)

    def isConnected(self):
        """
        Method to check all non-zero degree vertices are connected by DFS or BFS
        """
        visited = [False] * self.V

        # find a vertex will non-zero degree
        for i in range(self.V):
            if len(self.graph[i]) > 1:
                break
        
        # if there are no edges in the graph return True
        if i == self.V - 1:
            return True

        # start DFS to check connected
        self.DFSUtil(i, visited)

        # check if all non-zero degree vertices are visited
        if i in range(self.V):
            if visited[i] == False and len(self.graph[i]) > 0 :
                return False

        return True

    def isEulerian(self):
        if self.isConnected() == False:
            return 0
        else:
            # count vertices with odd degree
            odd = 0

            for i in range(self.V):
                if len(self.graph[i]) %2 != 0:
                    odd += 1
            
            # if odd == 2 then semi-eulerian
            # if odd == 0 then eulerian
            # if odd > 2 then graph is not Eulerian
            # Note that odd count can not be 1 in undirected graph
            if odd == 0:
                return 2
            elif odd == 2:
                return 1
            elif odd > 2:
                return 0
    
    def test(self):
        odd = self.isEulerian()
        if odd == 2:
            print("Graph is eulerian")
        elif odd == 1:
            print("Graph is semi-eulerian")
        elif odd == 0:
            print("Graph is not-eulerian")

    

#Let us create and test graphs shown in above figures
g1 = Graph(5);
g1.add_edge(1, 0)
g1.add_edge(0, 2)
g1.add_edge(2, 1)
g1.add_edge(0, 3)
g1.add_edge(3, 4)
g1.test()
 
g2 = Graph(5)
g2.add_edge(1, 0)
g2.add_edge(0, 2)
g2.add_edge(2, 1)
g2.add_edge(0, 3)
g2.add_edge(3, 4)
g2.add_edge(4, 0)
g2.test();
 
g3 = Graph(5)
g3.add_edge(1, 0)
g3.add_edge(0, 2)
g3.add_edge(2, 1)
g3.add_edge(0, 3)
g3.add_edge(3, 4)
g3.add_edge(1, 3)
g3.test()
 
#Let us create a graph with 3 vertices
# connected in the form of cycle
g4 = Graph(3)
g4.add_edge(0, 1)
g4.add_edge(1, 2)
g4.add_edge(2, 0)
g4.test()
 
# Let us create a graph with all veritces
# with zero degree
g5 = Graph(3)
g5.test()