from .manager import Manager
from algorithms.fordFulkerson import FordFulkerson
from visualizers.fordFulkersonVisualizer import FordFulkersonVisualizer

class FordFulkersonManager(Manager[FordFulkerson]):
    def __init__(self, graph):
        super().__init__(FordFulkerson(graph), FordFulkersonVisualizer())
        

    def run(self):
        source = int(input("Enter the source node: "))
        sink = int(input("Enter the sink node: "))
        max_flow, _ = self.algorithm.run(source, sink)
        self.visualizer.iterations = self.algorithm.iterations

        print(f"Max Flow: {max_flow}")

        print("How would you like to visualize the result?")
        print("1. Export to image files")
        print("2. Visualize interactively")
        visualization = input("Enter the number of the visualization method: ")
        if visualization == "1":
            self.visualizer.export_to_image()
        elif visualization == "2":
            self.visualizer.visualize_result()
        else:
            print("Invalid selection.")

    def _run_algorithm(self):
        pass