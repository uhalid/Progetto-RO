

from node import Node  
def yo():
    N = M = S = E = 0
    nodes = None
    #Add arguments and check if file exists
    with open("input.txt") as f:
        N, M, *SE = f.readline().strip().split()
        S, E = (SE + [0, 0])[:2] if SE else (0, 0)
        N = int(N)
        M = int(M)
        S = int(S)
        E = int(E)
        
    
        edges = [ [int(y) for y in x.strip().split(" ")] for x in f.readlines()]
        nodes = [Node()  for _ in range(N)]
        for edge in edges:
            start, end, capacity = edge
            nodes[start].addEdge(end, capacity)
    
    etichette = [ [None, None] for _ in range(N)]
    etichette[S] = [S, float('inf')]
    expanded = [False for _ in range(N)]

    while True:
        node = list(filter(lambda x: x[0][0] != None and not x[1], zip(etichette, expanded)))
        if len(node) == 0:
            exit()
        print(node)
        exit()



    

        




if __name__ == "__main__":
    yo()