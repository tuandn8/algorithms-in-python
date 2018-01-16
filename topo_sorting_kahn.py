# Algorithm:
# Steps involved in finding the topological ordering of a DAG:

# Step 1: Compute in-degree(number of incoming edges) for each of the vertex present in the DAG and initialize the count of visited nodes as 0.
# Step 2: Pick all the vertices with in-degree as 0 and add them into a queue(Enqueue operation)
# Step 3: Remove a vertex from the queue(Dequeue operation) and then.
#           Increment count of visited nodes by 1.
#           Decrease in-degree by 1 for all its neighboring nodes.
#           If in-degree of a neighboring nodes is reduced to zero, then add it to the queue.
# Step 4: Repeat Step 3 until the queue is empty.

# Step 5: If count of visited nodes is not equal to the number of nodes in the graph then the topological sort is not possible for the given graph.


from collections import defaultdict


class Graph:
    def __init__(self, V):
        self.V = V
        self.graph = defaultdict(list)
        self.indegree = [0] * self.V

    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.indegree[v] += 1

    def topologicalSort(self):
        S = []
        L = []

        for u in range(self.V):
            if self.indegree[u] == 0:
                S.insert(0, u)
        
        while len(S) > 0:
            u = S.pop()
            L.append(u)

            for v in self.graph[u]:
                self.indegree[v] -= 1
                if self.indegree[v] == 0:
                    S.insert(0, v)

        if len(L) < self.V:
            print("Graph has a cycle and cannot sort")
        else:
            print(L)


g = Graph(6)
g.addEdge(5, 2)
g.addEdge(5, 0)
g.addEdge(4, 0)
g.addEdge(4, 1)
g.addEdge(2, 3)
g.addEdge(3, 1)

print("Following is a Topological Sort of the given graph")
g.topologicalSort()
