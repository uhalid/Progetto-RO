class Node:
    def __init__(self, idd, x, y, extra_info = ""):
        self.id: int = idd
        self.x: int = x
        self.y: int = y
        self.extra_info: str = extra_info 
    
    def add_extra_info(self, extra_info: str):
        self.extra_info = extra_info
