
from collections import defaultdict


class Graph:
    def __init__(self, V):
        self.V = V
        self.graph = defaultdict(list)
        self.indegree = [0] * self.V

    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.indegree[v] += 1

    def allTopologicalSortUtil(self, res, visited):
        flag = False

        for i in range(self.V):
            if self.indegree[i] == 0 and not visited[i]:
                for j in self.graph[i]:
                    self.indegree[j] -= 1

                res.append(i)
                visited[i] = True
                self.allTopologicalSortUtil(res, visited)

                visited[i] = False
                del res[len(res) - 1]
                for j in self.graph[i]:
                    self.indegree[j] += 1
                flag = True
        
        if not flag:
            print(res)
    
    def allTopologicalSort(self):
        visited = [False] * self.V

        res = []
        self.allTopologicalSortUtil(res, visited)


g = Graph(6)
g.addEdge(5, 2)
g.addEdge(5, 0)
g.addEdge(4, 0)
g.addEdge(4, 1)
g.addEdge(2, 3)
g.addEdge(3, 1)

print("Following is all Topological Sort of the given graph")
g.allTopologicalSort()



    
