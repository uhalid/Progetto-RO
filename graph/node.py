class Node:
    def __init__(self, idd, x, y, label = ""):
        self.id: int = idd
        self.x: int = x
        self.y: int = y
        self.label: str = label 
    
    def add_label(self, label: str):
        self.label = label
