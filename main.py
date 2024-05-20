

import sys
from graph.graph import Graph
from graph.node import Node  


def read_graph(filename: str) -> Graph:
    graph = Graph()
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()

            # Read the number of nodes and edges from the first line
            n, m = map(int, lines[0].split())

            # Read the edges and add them to the graph
            for line in lines[1:m+1]:
                data = list(map(int, line.split()))
                start, end, capacity = data[0], data[1], data[2]
                cost = data[3] if len(data) > 3 else 0
                graph.add_edge(start, end, capacity, cost)

            # Read the nodes and add them to the graph
            for line in lines[m+1:]:
                node_id, x, y = map(int, line.split())
                graph.add_node(node_id, x, y)
    except FileNotFoundError:
        print(f"File {filename} not found.")
        sys.exit(1)
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)
    return graph

def main(filename: str):
    graph: Graph = read_graph(filename)

    while True:
        print("Which algorithm would you like to run?")
        print("1. Ford-Fulkerson")
        selection = input("Enter the number of the algorithm: ")
        if selection == "1":
            from algorithms.fordFulkerson import FordFulkerson
            ff = FordFulkerson(graph)
            source = int(input("Enter the source node: "))
            sink = int(input("Enter the sink node: "))
            max_flow, _ = ff.run(source, sink)
            print(f"Max Flow: {max_flow}")

            print("How would you like to visualize the result?")
            print("1. Export to image files")
            print("2. Visualize interactively")
            visualization = input("Enter the number of the visualization method: ")
            if visualization == "1":
                ff.export_to_image()
            elif visualization == "2":
                ff.visualize_result()
            else:
                print("Invalid selection.")
        else:
            print("Invalid selection.")






if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please provide the filename as a command-line argument.")
        sys.exit(1)
    filename=sys.argv[1]
    # add a check if the filename exist
    main(filename)