from algorithms.algorithm import Algorithm 
from visualizers.visualizer import Visualizer
from graph.graph import Graph
from abc import ABC, abstractmethod
from typing import TypeVar, Generic

A = TypeVar('A', bound=Algorithm)

class Manager(ABC, Generic[A]):
    def __init__(self, algorithm: A, visualizer: Visualizer):
        self.algorithm = algorithm
        self.visualizer = visualizer
    
    @abstractmethod
    def run(self):
        pass
    
    @abstractmethod
    def _run_algorithm(self):
        pass
        # self.algorithm.run()
        # self.visualizer.iterations = self.algorithm.iterations

    def _export_to_image(self):
        self.visualizer.export_to_image()
    
    def _visualize_result(self):
        self.visualizer.visualize_result()

    def _export_to_latex(self):
        self.visualizer.export_to_latex()

    


