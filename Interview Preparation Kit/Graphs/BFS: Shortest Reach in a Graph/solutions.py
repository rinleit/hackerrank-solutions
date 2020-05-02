from collections import defaultdict

class Graph:
    def __init__(self, n):
        self.n = n
        self.edges = defaultdict(lambda: [])

    def connect(self,x,y):
        self.edges[x].append(y)
        self.edges[y].append(x)

    def find_all_distances(self, root):
        distances = [-1 for i in range(self.n)]
        queue = [root]
        distances[root] = 0
        visited = [root]
        while queue:
            node = queue.pop(0)
            childs = self.edges[node]
            distance = distances[node]
            for child in childs:
                if child not in visited:
                    visited += [child]
                    queue += [child]
                    distances[child] = distance + 6
        distances.remove(0)
        print(' '.join(map(str, distances)))

t = int(input())
for i in range(t):
    n, m = [int(value) for value in input().split()]
    graph = Graph(n)
    for i in range(m):
        x,y = [int(x) for x in input().split()]
        graph.connect(x-1,y-1) 
    s = int(input())
    graph.find_all_distances(s-1)
