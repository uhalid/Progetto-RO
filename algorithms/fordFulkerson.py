from typing import Tuple, List, Dict
from .algorithm import Algorithm
from graph import Graph



class FordFulkerson(Algorithm):
    def __init__(self, graph: Graph, name: str = "Ford Fulkerson"):
        super().__init__(graph, name)
        self.iterations = []

    def run(self, source: int, sink: int) -> Tuple[float, List[Graph]]:
        # Step 1: Initialize flow and max flow
        max_flow = 0.0
        for edge in self.graph.get_edges():
            edge.flow = 0.0

        def bfs_find_augmenting_path() -> Tuple[bool, Dict[int, Tuple[int, float]]]:
            """Perform BFS to find an augmenting path and return the path as a dictionary."""
            parent = {source: (None, float('inf'))}
            queue = [source]
            while queue:
                current = queue.pop(0)
                for edge in self.graph.get_edges_from(current):
                    residual_capacity = edge.capacity - edge.flow
                    if edge.to_node not in parent and residual_capacity > 0:  # forward edge
                        parent[edge.to_node] = (current, min(
                            parent[current][1], residual_capacity))
                        if edge.to_node == sink:
                            return True, parent
                        queue.append(edge.to_node)
                for edge in self.graph.get_edges_to(current):
                    if edge.from_node not in parent and edge.flow > 0:  # backward edge
                        parent[edge.from_node] = (
                            current, min(parent[current][1], edge.flow))
                        if edge.from_node == sink:
                            return True, parent
                        queue.append(edge.from_node)
            return False, parent

        def augment_flow(path: Dict[int, Tuple[int, float]]):
            """Augment the flow along the found path."""
            flow = path[sink][1]
            current = sink
            while current != source:
                prev, _ = path[current]
                if edge:= self.graph.get_edge_between(prev, current):
                    edge.flow += flow
                if edge:= self.graph.get_edge_between(current, prev):
                    edge.flow -= flow
                current = prev
            return flow

        i = 0 
        while True:
            found, path = bfs_find_augmenting_path()
            if not found:
                break
            delta = augment_flow(path)
            print(found, path, delta)
            max_flow += delta
            # Record the state of the graph
            self.iterations.append(self.graph.copy())
            # print(self.graph)
            # if i == 0:
            #     exit()
            # print("-" * 5 + f"{i}" + "-" * 5 )
            # i += 1

        return max_flow, self.iterations


if __name__ == "__main__":
    from graph import Node, Edge, graph

    # g = Graph()
    # g.add_node(0, 0, 0)
    # g.add_node(1, 1, 1)
    # g.add_node(2, 2, 0)
    # g.add_node(3, 3, 1)

    # g.add_edge(0, 1, 10.0)
    # g.add_edge(0, 2, 5.0)
    # g.add_edge(1, 2, 15.0)
    # g.add_edge(1, 3, 10.0)
    # g.add_edge(2, 3, 10.0)

    # ff = FordFulkerson(g)
    # max_flow, iterations = ff.run(0, 3)

    # print(f"Max Flow: {max_flow}")
    # for i, iteration in enumerate(iterations):
    #     print(f"Iteration {i}:")
    #     print(iteration)

    g = Graph()
    g.add_node(0, 0, 0)
    g.add_node(1, 0, 0)
    g.add_node(2, 0, 0)
    g.add_node(3, 0, 0)
    g.add_node(4, 0, 0)
    g.add_node(5, 0, 0)
    g.add_node(6, 0, 0)
    g.add_node(7, 0, 0)
    g.add_node(8, 0, 0)

    g.add_edge(0, 1, 14)  # Node 1 -> Node 2
    g.add_edge(0, 3, 23)  # Node 1 -> Node 4
    g.add_edge(1, 2, 10)  # Node 2 -> Node 3
    g.add_edge(1, 3, 9)   # Node 2 -> Node 4
    g.add_edge(4, 1, 11)  # Node 2 -> Node 5
    g.add_edge(2, 4, 12)  # Node 3 -> Node 5
    g.add_edge(3, 4, 26)  # Node 4 -> Node 5
    g.add_edge(4, 5, 25)  # Node 5 -> Node 6
    g.add_edge(4, 6, 4)   # Node 5 -> Node 7
    g.add_edge(5, 7, 7)   # Node 6 -> Node 8
    g.add_edge(6, 8, 15)   # Node 7 -> Node 9
    g.add_edge(7, 8, 20)  # Node 8 -> Node 9

    ff = FordFulkerson(g)
    max_flow, iterations = ff.run(0, 8)

    print(f"Max Flow: {max_flow}")
    for i, iteration in enumerate(iterations):
        print(f"Iteration {i}:")
        print(iteration)
