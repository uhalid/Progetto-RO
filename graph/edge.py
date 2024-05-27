class Edge:
    def __init__(self, from_node: int, to_node: int, capacity: float, cost: float = 0.0, label: str = ""):
        self.from_node: int = from_node
        self.to_node: int = to_node
        self.capacity: float = capacity
        self.flow: float = 0.0
        self.cost: float = cost
        self.label: str = label
        self.style: str = "solid" # other commons options are dashed, dotted

    def __str__(self) -> str:
        return f"Edge({self.from_node}, {self.to_node}) - capacity: {self.capacity}, flow: {self.flow}, cost: {self.cost}, label: {self.label}"
