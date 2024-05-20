

import sys
from graph.graph import Graph
from graph.node import Node  


def main():
    # Reading input from standard input or from a file
    input = sys.stdin.read
    data = input().splitlines()

    # First line: N (number of nodes) and M (number of edges)
    N, M = map(int, data[0].split())

    # Next M lines: edges (start, end, capacity, cost)
    edges = []
    for i in range(1, M + 1):
        start, end, capacity, cost = map(float, data[i].split())
        edges.append((int(start), int(end), capacity, cost))

    # Next N lines: nodes (node_id, x, y)
    nodes = []
    for i in range(M + 1, M + 1 + N):
        node_id, x, y = map(float, data[i].split())
        nodes.append((int(node_id), x, y))

    # Create graph and add nodes and edges
    graph = Graph()
    for node_id, x, y in nodes:
        graph.add_node(node_id, x, y)

    for start, end, capacity, cost in edges:
        graph.add_edge(start, end, capacity, cost)
    

        




if __name__ == "__main__":
    main()