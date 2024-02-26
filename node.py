class Node:
    edges = []


    def addEdge(self, to:int, capaciy: int):
        self.edges.append([to, capaciy, 0])
    def findCapacityTo(self, to:int) -> list | None :
        return filter(lambda edge: edge[0] == to, self.edges)

