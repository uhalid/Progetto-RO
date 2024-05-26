from typing import Dict, List, Optional
from .node import Node
from .edge import Edge
import copy

class Graph:
    def __init__(self):
        self.nodes: Dict[int, Node] = {}
        self.edges: List[Edge] = []
        self.range_coods: Dict[str, int] = {}

    def add_node(self, node_id: int, x: int, y: int):
        self.nodes[node_id] = Node(node_id, x, y)

    def add_edge(self, from_node: int, to_node: int, capacity: float, cost: float = 0.0):
        edge = Edge(from_node, to_node, capacity, cost)
        self.edges.append(edge)

    def get_edges(self):
        return self.edges

    def get_edges_from(self, node_id: int) -> List[Edge]:
        """Returns all the edges starting from a node with id node_id."""
        return [edge for edge in self.edges if edge.from_node == node_id]

    def get_edges_to(self, node_id: int) -> List[Edge]:
        """Returns all the edges ending in a node with id node_id."""
        return [edge for edge in self.edges if edge.to_node == node_id]

    def get_edge_between(self, from_node: int, to_node: int) -> Optional[Edge]:
        """Returns the edge between from_node and to_node if it exists, otherwise None."""
        for edge in self.edges:
            if edge.from_node == from_node and edge.to_node == to_node:
                return edge
        return None
    
    def add_label(self, node_id: int, label: str):
        self.nodes[node_id].add_label(label)

    def copy(self) -> 'Graph':
        """Returns a deep copy of the graph."""
        new_graph = Graph()
        new_graph.nodes = copy.deepcopy(self.nodes)
        new_graph.edges = copy.deepcopy(self.edges)
        return new_graph

    def __str__(self) -> str:
        """Returns a string representing the graph in a human-comprehensible way."""
        result = ["Graph:"]
        result.append("Nodes:")
        for node_id, node in self.nodes.items():
            result.append(f"  Node {node_id}: (x={node.x}, y={node.y})")

        result.append("Edges:")
        for edge in self.edges:
            result.append(
                f"  Edge from {edge.from_node} to {edge.to_node} with capacity {edge.capacity} and flow {edge.flow}")

        return "\n".join(result)
    def get_max_coords(self) -> List[int]:
        if len(self.range_coods) > 0:
            return self.range_coods
        min_x = float("inf")
        max_x = 0
        min_y = float("inf")
        max_y = 0
        for node in graph:
            min_x = min(min_x, node.x)
            max_x = max(max_x, node.x)
            min_y = min(min_y, node.y)
            max_y = max(max_y, node.y)

        self.range_coods["min_x"] = min_x
        self.range_coods["max_x"] = max_x
        self.range_coods["min_y"] = min_y
        self.range_coods["max_y"] = max_y

        return  self.range_coods
    


if __name__ == "__main__":
    from node import Node
    from edge import Edge

    graph = Graph()
    graph.add_node(0, 0, 0)
    graph.add_node(1, 1, 1)
    graph.add_node(2, 2, 0)
    graph.add_edge(0, 1, 10.0)
    graph.add_edge(1, 2, 5.0)
    graph.add_edge(0, 2, 15.0)

    print(graph)
    print("Edges from node 0:", graph.get_edges_from(0))
    print("Edges to node 2:", graph.get_edges_to(2))
