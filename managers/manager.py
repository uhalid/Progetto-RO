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
    



    


