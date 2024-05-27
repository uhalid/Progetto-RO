from graph import Graph
from abc import ABC, abstractmethod
class Algorithm(ABC):
    def __init__(self, graph: Graph, name: str ):
        self.graph: Graph = graph
        self.name: str = name
        self.current_iteration = 0
        self.iterations = [graph.copy()]

    @abstractmethod
    def run(self):
        pass

