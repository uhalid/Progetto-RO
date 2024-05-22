from typing import Tuple, List, Dict
from .algorithm import Algorithm
from graph import Graph
import heapq
class FordFulkerson(Algorithm):
    def __init__(self, graph: Graph, name: str = "Ford-Fulkerson"):
        super().__init__(graph, name)

    def run(self, source: int, sink: int) -> Tuple[float, List[Graph]]:
        # Step 1: Initialize flow and max flow
        max_flow = 0.0
        for edge in self.graph.edges:
            edge.flow = 0.0

        def bfs_find_augmenting_path() -> Tuple[bool, Dict[int, Tuple[int, float]]]:
            """Perform BFS to find an augmenting path and return the path as a dictionary."""
            parent = {source: (None, float('inf'))}
            min_heap = [source]
            while min_heap:
                current = heapq.heappop(min_heap)

                for edge in self.graph.get_edges_from(current):
                    residual_capacity = edge.capacity - edge.flow
                    if edge.to_node not in parent and residual_capacity > 0:  # forward edge
                        parent[edge.to_node] = (current, min(
                            parent[current][1], residual_capacity))
                        if edge.to_node == sink:
                            return True, parent
                        heapq.heappush(min_heap, edge.to_node)
                for edge in self.graph.get_edges_to(current):
                    if edge.from_node not in parent and edge.flow > 0:  # backward edge
                        parent[edge.from_node] = (
                            -current, min(parent[current][1], edge.flow))
                        if edge.from_node == sink:
                            return True, parent
                        # queue.append(edge.from_node)
                        heapq.heappush(min_heap, edge.from_node)
            return False, parent

        def augment_flow(path: Dict[int, Tuple[int, float]]):
            """Augment the flow along the found path."""
            flow = path[sink][1]
            current = sink
            while current != source:
                prev, _ = path[abs(current)]
                if edge:= self.graph.get_edge_between(abs(prev), abs(current)):
                    edge.flow += flow
                if edge:= self.graph.get_edge_between(abs(current), abs(prev)):
                    edge.flow -= flow
                current = prev
            return flow

        while True:
            found, path = bfs_find_augmenting_path()
            if not found:
                break
            delta = augment_flow(path)
            max_flow += delta
            # Record the state of the graph
            copy_graph = self.graph.copy()
            
            for node_id, (parent, flow) in path.items():
                if parent is not None:
                    copy_graph.add_label(node_id, f"[{parent}, {flow}]")
                else:
                    copy_graph.add_label(node_id, f"[ - , - ]")
            for edge in copy_graph.edges:
                edge.label = f"{edge.flow}/{edge.capacity}"

            self.iterations.append(copy_graph)

        return max_flow, self.iterations






        
if __name__ == "__main__":
    from graph import Node, Edge, graph

    g = Graph()
    g.add_node(0, 0, 3)
    g.add_node(1, 1, 5)
    g.add_node(2, 2, 5)
    g.add_node(3, 1, 0)
    g.add_node(4, 2, 0)
    g.add_node(5, 3, 3)
    g.add_node(6, 3, 0)
    g.add_node(7, 3, 5)
    g.add_node(8, 4, 3)

    g.add_edge(0, 1, 14)  # Node 1 -> Node 2
    g.add_edge(0, 3, 23)  # Node 1 -> Node 4
    g.add_edge(1, 2, 10)  # Node 2 -> Node 3
    g.add_edge(1, 3, 9)   # Node 2 -> Node 4
    g.add_edge(2, 4, 12)  # Node 3 -> Node 5
    g.add_edge(2, 7, 18)  # Node 3 -> Node 8
    g.add_edge(3, 4, 26)  # Node 4 -> Node 5
    g.add_edge(4, 1, 11)  # Node 5 -> Node 4
    g.add_edge(4, 5, 25)  # Node 5 -> Node 6
    g.add_edge(4, 6, 4)   # Node 5 -> Node 7
    g.add_edge(5, 7, 8)   # Node 6 -> Node 8
    g.add_edge(5, 6, 7)   # Node 6 -> Node 7
    g.add_edge(6, 8, 15)   # Node 7 -> Node 9
    g.add_edge(7, 8, 20)  # Node 8 -> Node 9

    ff = FordFulkerson(g)
    max_flow, iterations = ff.run(0, 8)

    ff.export_to_image()
    ff.visualize_result()
    print(f"Max Flow: {max_flow}")
    for i, iteration in enumerate(iterations):
        print(f"Iteration {i}:")
        print(iteration)
