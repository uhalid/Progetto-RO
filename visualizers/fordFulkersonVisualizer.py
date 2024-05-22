from typing import List
from .visualizer import Visualizer
from graph.graph import Graph
import networkx as nx
import matplotlib.pyplot as plt



class FordFulkersonVisualizer(Visualizer):
    def __init__(self, name: str = "Ford-Fulkerson Visualizer"):
        super().__init__(name)

    def _visualize_graph(self, graph: Graph, iteration: int, ax: plt.Axes):
        """Helper function to visualize a graph."""
        G = nx.DiGraph()

        for node_id, node in graph.nodes.items():
            G.add_node(node_id, pos=(node.x, node.y))

        for edge in graph.edges:
            G.add_edge(edge.from_node, edge.to_node,
                       weight=edge.flow, capacity=edge.capacity)

        pos = nx.get_node_attributes(G, 'pos')
        

        nx.draw_networkx_nodes(G, pos, node_size=500,
                               node_color='lightblue', ax=ax)
        nx.draw_networkx_labels(
            G, pos, font_size=10, font_color='black', ax=ax)


        nx.draw_networkx_edges(
            G, pos, edge_color='black', arrows=True, ax=ax)
        edge_labels = {
            (u, v): f"{d['weight']}/{d['capacity']}" for u, v, d in G.edges(data=True)}
        nx.draw_networkx_edge_labels(
            G, pos, edge_labels=edge_labels, font_size=8, ax=ax)


        ax.set_title(f"Ford-Fulkerson Iteration {iteration + 1}")
        ax.axis('off')


