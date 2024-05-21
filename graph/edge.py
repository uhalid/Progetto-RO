class Edge:
    def __init__(self, from_node: int, to_node: int, capacity: float, cost: float = 0.0, label: str = ""):
        self.from_node: int = from_node
        self.to_node: int = to_node
        self.capacity: float = capacity
        self.flow: float = 0.0
        self.cost: float = cost
        self.label: str = label
