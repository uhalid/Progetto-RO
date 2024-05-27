from typing import List
from .visualizer import Visualizer
from graph.graph import Graph
import networkx as nx
import matplotlib.pyplot as plt



class FordFulkersonVisualizer(Visualizer):
    def __init__(self, name: str = "Ford-Fulkerson"):
        super().__init__(name)

    def _visualize_graph(self, graph: Graph, iteration: int, ax: plt.Axes):
        """Helper function to visualize a graph."""
        G = nx.DiGraph()

        for node_id, node in graph.nodes.items():
            G.add_node(node_id, pos=(node.x, node.y))

        for edge in graph.edges:
            G.add_edge(edge.from_node, edge.to_node,
                       weight=edge.flow, capacity=edge.capacity, style=edge.style)

        pos = nx.get_node_attributes(G, 'pos')
        

        nx.draw_networkx_nodes(G, pos, node_size=500,
                               node_color='lightblue', ax=ax)
        nx.draw_networkx_labels(
            G, pos, font_size=10, font_color='black', ax=ax)


        solid_edges = [(edge.from_node, edge.to_node)
                    for edge in graph.edges if edge.style == 'solid']
        dashed_edges = [(edge.from_node, edge.to_node)
                        for edge in graph.edges if edge.style == 'dashed']


        nx.draw_networkx_edges(G, pos, edgelist=solid_edges,
                            edge_color='gray', style='-', arrows=True, ax=ax)

        # Draw dashed edges
        nx.draw_networkx_edges(G, pos, edgelist=dashed_edges,
                            edge_color='gray', style='--', arrows=True, ax=ax)

        # nx.draw_networkx_edges(
        #     G, pos, edge_color='gray', arrows=True, ax=ax)
        edge_labels = {
            (u, v): f"{d['weight']}/{d['capacity']}" for u, v, d in G.edges(data=True)}
        nx.draw_networkx_edge_labels(
            G, pos, edge_labels=edge_labels, font_size=8, ax=ax)

        pos_label = {node_id: self.get_offset_label(graph, graph.nodes[node_id]) for node_id in pos.keys()}

        nx.draw_networkx_labels(G, pos_label, labels={node_id: graph.nodes[node_id].label for node_id in G.nodes()}, font_color="black", ax=ax, font_size=8)

        ax.set_title(f"Ford-Fulkerson Iteration {iteration + 1}")
        ax.axis('off')

    def to_latex_raw(self, graph: Graph):
        latex_string = r"""\begin{tikzpicture}[scale = 3, font = \Large, node distance = 15mm and 15mm,
                                            V/.style= {circle, draw, fill = gray!30},
                                            every edge quotes/.style= {auto, font =\footnotesize, sloped}
                                            ]""" + "\n"

        latex_string += r"\begin{scope}[nodes=V]" + "\n"
        for node_id, node in graph.nodes.items():
            node_id = str(node_id)
            if node.label:
                latex_string += f"\\node[label={self.get_label_position(graph, node)}:{{{node.label}}}]  ({node_id}) at ({node.x}, {node.y}) {{{node_id}}};\n"
            else:
                latex_string += f"\\node ({node_id}) at ({node.x}, {node.y}) {{{node_id}}};\n"
        latex_string += r"\end{scope}" + "\n"

        latex_string += r"\begin{scope}[->]" + "\n"
        for edge in graph.edges:
            if edge.label:
                latex_string += f"\\draw ({edge.from_node}) edge[\"{edge.label}\", {edge.style}] ({edge.to_node});\n"
            else:
                latex_string += f"\\draw ({edge.from_node}) edge["", {edge.style}] ({edge.to_node});\n"
        latex_string += r"\end{scope}" + "\n"

        latex_string += r"\end{tikzpicture}" + "\n"

        return latex_string

