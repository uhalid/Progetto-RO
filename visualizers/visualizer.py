from abc import ABC, abstractmethod
from typing import Callable, Tuple
from graph.graph import Graph
from graph.node import Node
import matplotlib.pyplot as plt
from matplotlib.widgets import Button
import os, datetime



class Visualizer(ABC):
    def __init__(self, name: str = "Visualizer"):
        self.current_iteration = 0
        self.iterations = []
        self.name = name


    @abstractmethod
    def _visualize_graph(self, graph: Graph, iteration: int, ax: plt.Axes):
        pass

    def export_to_file(self, export_function: Callable):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        folder_name = f"{self.name} - {timestamp}"
        os.makedirs(f"results/{self.name}/{folder_name}", exist_ok=True)

        for i, iteration in enumerate(self.iterations):
            export_function(folder_name, i, iteration)
        return folder_name

    def export_to_image(self):
        """Exports the result of each iteration to separate image files."""
        def write_iteration_to_png(folder_name, i, iteration):
            fig, ax = plt.subplots()
            self._visualize_graph(iteration, i, ax)
            plt.savefig(f"results/{self.name}/{folder_name}/interaction_{i+1}.png")
            plt.close(fig)

        folder_name = self.export_to_file(write_iteration_to_png)
        print(f"Images exported successfully! Check the folder {folder_name}")

    def export_to_latex(self):
        """Exports the result of each iteration to separate image files."""
        def write_iteration_to_latex(folder_name, i, iteration):
            with open(f"results/{self.name}/{folder_name}/interaction_{i+1}.tex", "w") as file:
                file.write(self.to_latex(iteration))

        folder_name = self.export_to_file(write_iteration_to_latex)
        print(f"Latex files exported successfully! Check the folder {folder_name}")

    def export_to_latex_and_image(self):
        """Exports the result of each iteration to separate image files."""
        def write_iteration_to_latex_and_image(folder_name, i, iteration):
            with open(f"results/{self.name}/{folder_name}/interaction_{i+1}.tex", "w") as file:
                file.write(self.to_latex(iteration))
            fig, ax = plt.subplots()
            self._visualize_graph(iteration, i, ax)
            plt.savefig(f"results/{self.name}/{folder_name}/interaction_{i+1}.png")
            plt.close(fig)

        folder_name = self.export_to_file(write_iteration_to_latex_and_image)
        print(f"Latex files and images exported successfully! Check the folder {folder_name}")

        
    def visualize_result(self):
        fig, ax = plt.subplots()
        # Adjust subplot to accommodate buttons
        plt.subplots_adjust(bottom=0.2)

        def next_iteration(event):
            ax.clear()
            self.current_iteration = (
                self.current_iteration + 1) % len(self.iterations)
            current_graph = self.iterations[self.current_iteration]
            self._visualize_graph(current_graph, self.current_iteration, ax)
            fig.canvas.draw_idle()

        def prev_iteration(event):
            ax.clear()
            self.current_iteration = (
                self.current_iteration - 1) % len(self.iterations)
            current_graph = self.iterations[self.current_iteration]
            self._visualize_graph(current_graph, self.current_iteration, ax)
            # plt.xlim(, xmax)
            fig.canvas.draw_idle()

        # Create buttons
        ax_prev = plt.axes([0.7, 0.05, 0.1, 0.075])
        ax_next = plt.axes([0.81, 0.05, 0.1, 0.075])
        b_next = Button(ax_next, 'Next')
        b_next.on_clicked(next_iteration)
        b_prev = Button(ax_prev, 'Previous')
        b_prev.on_clicked(prev_iteration)

        # Visualize the initial iteration
        self._visualize_graph(self.iterations[0], 0, ax)

        plt.show()
        

    def to_latex(self, graph: Graph):
        latex_string = r"""\documentclass{article}
            \usepackage{graphicx}
            \usepackage{tikz}
            \usetikzlibrary{positioning, quotes, shapes.multipart}
            
            \begin{document}
            """
        latex_string += self.to_latex_raw(graph)

        latex_string += "\end{document}"

        return latex_string


    @abstractmethod
    def to_latex_raw():
        pass

    def get_offset_label(self, graph: Graph, node: Node) -> Tuple[float, float]:
        label_position = self.get_label_position(graph, node)
        default_offset = 0.13

        offset = (0, 0)
        if "above" in label_position:
            offset = (0, default_offset)
        elif "below" in label_position:
            offset = (0, -default_offset)
        else:
            offset = (0, default_offset)
        
        return (node.x + offset[0], node.y + offset[1])
        

        
    def get_label_position(self,graph: Graph, node: Node) -> str:
        node_id = node.id
        in_edges = graph.get_edges_to(node_id)
        out_edges = graph.get_edges_from(node_id)

        if not in_edges and not out_edges:
            # No edges, label can be placed anywhere
            return "above"

        # Calculate the number of edges in each direction
        edge_counts = {
            "above": 0,
            "below": 0,
            "right": 0,
            "left": 0,
            "above_right": 0,
            "above_left": 0,
            "below_right": 0,
            "below_left": 0,
        }


        for edge in in_edges + out_edges:
            from_node = graph.nodes[edge.from_node]
            to_node = graph.nodes[edge.to_node]

            node_to_check = to_node if from_node.id == node_id else from_node

            if node_to_check.x == node.x and node_to_check.y > node.y:
                edge_counts["above"] += 1
            elif node_to_check.x == node.x and node_to_check.y < node.y:
                edge_counts["below"] += 1
            elif node_to_check.y == node.y and node_to_check.x < node.x:
                edge_counts["left"] += 1
            elif node_to_check.y == node.y and node_to_check.x > node.x:
                edge_counts["right"] += 1
            elif node_to_check.x < node.x and node_to_check.y > node.y:
                edge_counts["above_left"] += 1
            elif node_to_check.x > node.x and node_to_check.y > node.y:
                edge_counts["above_right"] += 1
            elif node_to_check.x < node.x and node_to_check.y < node.y:
                edge_counts["below_left"] += 1
            elif node_to_check.x > node.x and node_to_check.y < node.y:
                edge_counts["below_right"] += 1

        #first check if there is no edge from that direction
        direction_totals = {
            "above": edge_counts["above"] + edge_counts["above_left"] + edge_counts["above_right"],
            "below": edge_counts["below"] + edge_counts["below_left"] + edge_counts["below_right"],
            "left": edge_counts["left"] + edge_counts["above_left"] + edge_counts["below_left"],
            "right": edge_counts["right"] + edge_counts["above_right"] + edge_counts["below_right"]
        } 

        if any(count == 0 for count in direction_totals.values()):
            return min(direction_totals, key=direction_totals.get)


        #if there is an edge from each direction, choose the one with the least number of edges
        min_count = min(edge_counts.values())
        positions = [position for position,
                    count in edge_counts.items() if count == min_count]


        return positions[0].replace("_", " ")