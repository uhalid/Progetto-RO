from .manager import Manager
from algorithms.fordFulkerson import FordFulkerson
from visualizers.fordFulkersonVisualizer import FordFulkersonVisualizer
from graph.graph import Graph

class FordFulkersonManager(Manager[FordFulkerson]):
    def __init__(self, graph: Graph):
        self.graph: Graph = graph
        super().__init__(FordFulkerson(graph), FordFulkersonVisualizer())
        

    def run(self):
        source = input("Enter the source node: ")
        while not source.isdigit() or not self.graph.nodes.get(int(source)):
            source = input("Invalid node. Enter the source node: ")
        source = int(source)

        sink = input("Enter the sink node: ")
        while not sink.isdigit() or not self.graph.nodes.get(int(sink)):
            sink = input("Invalid node. Enter the sink node: ")
        sink = int(sink)

        max_flow, _ = self.algorithm.run(source, sink)
        self.visualizer.iterations = self.algorithm.iterations

        print(f"Max Flow: {max_flow}")

        while True:
            print("How would you like to visualize the result?")
            print("0. Exit")
            print("1. Visualize Results")
            print("2. Export to Image")
            print("3. Export to LaTeX")
            print("4. Export to Image and LaTeX")
            visualization = input("Enter the number of the visualization method: ")
            if visualization == "1":
                self.visualizer.visualize_result()
            elif visualization == "2":
                self.visualizer.export_to_image()
            elif visualization == "3":
                self.visualizer.export_to_latex()
            elif visualization == "4":
                self.visualizer.export_to_latex_and_image()
            elif visualization == "0":
                break
            else:
                print("Invalid selection.")

