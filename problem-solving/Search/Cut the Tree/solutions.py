#!/bin/python3
import os
import sys

sys.setrecursionlimit(1000000)

# simple node class. A node holds a value 'data' and the indices for all nodes its connected to
class Node():
    def __init__(self, data):
        self.data = data
        self.vertices = list()
    def add_vertex(self, v):
        self.vertices.append(v)

# recursively calculates the value of underlying (= not visited) nodes for all nodes in a graph
# adds a "lowersum" attribute to node objects, that holds the sum of underlying values
def lower_sum(nodes, idx, visited):    
    visited[idx] = True
    ls = nodes[idx].data
    for n in nodes[idx].vertices:
        if not visited[n]:
            ls += lower_sum(nodes, n, visited)
    nodes[idx].lowersum = ls
    return ls

# wrapper for lower_sum() function
def fill_lower_sum(nodes):
    visited = [False for _ in range(len(nodes))]
    lower_sum(nodes, 0, visited)

# initializes the graph and calculates the minimum difference
def cutTheTree(data, edges):
    nodes = [Node(d) for d in data]
    for (u, v) in edges:
        nodes[u-1].add_vertex(v-1)
        nodes[v-1].add_vertex(u-1)

    fill_lower_sum(nodes)
    total = nodes[0].lowersum
    minsum = total
    for node in nodes:
        delta = abs(total - 2*node.lowersum)
        minsum = min(minsum, delta)

    return minsum


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    data = list(map(int, input().rstrip().split()))

    edges = []

    for _ in range(n - 1):
        edges.append(list(map(int, input().rstrip().split())))

    result = cutTheTree(data, edges)

    fptr.write(str(result) + '\n')

    fptr.close()
