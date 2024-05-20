from graph import Graph

class Algorithm:
    def __init__(self, graph: Graph, name: str ):
        self.graph: Graph = graph
        self.name: str = name

    def run(self):
        raise NotImplementedError("Subclasses should implement this!")
