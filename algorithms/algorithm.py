from graph import Graph
import datetime
import os
import matplotlib.pyplot as plt
from matplotlib.widgets import Button
import os, datetime

class Algorithm:
    def __init__(self, graph: Graph, name: str ):
        self.graph: Graph = graph
        self.name: str = name
        self.current_iteration = 0

    def run(self):
        raise NotImplementedError("Subclasses should implement this!")

    def _visualize_graph(self, graph: Graph, iteration: int, ax: plt.Axes):
        raise NotImplementedError("Subclasses should implement this!")

    def export_to_image(self):
        """Exports the result of each iteration to separate image files."""
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        folder_name = f"{self.name} - {timestamp}"
        os.makedirs(folder_name, exist_ok=True)
        for i, iteration in enumerate(self.iterations):
            fig, ax = plt.subplots()
            self._visualize_graph(iteration, i, ax)
            plt.savefig(f"{folder_name}/interaction_{i+1}.png")
            plt.close(fig)

    def visualize_result(self):
        fig, ax = plt.subplots()
        # Adjust subplot to accommodate buttons
        plt.subplots_adjust(bottom=0.2)

        def next_iteration(event):
            self.current_iteration = (
                self.current_iteration + 1) % len(self.iterations)
            self._visualize_graph(self.iterations[self.current_iteration], self.current_iteration, ax)
            fig.canvas.draw_idle()

        def prev_iteration(event):
            self.current_iteration = (
                self.current_iteration - 1) % len(self.iterations)
            self._visualize_graph(self.iterations[self.current_iteration], self.current_iteration, ax)
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
        