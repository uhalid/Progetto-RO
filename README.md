# Progetto RO

## Description

The main goal of this project is to implent a Ford-Fulkerson algortithm, but I designed it to allow multpliple algorithms to be run without changing the existing code base.
The program allows users to run the algorithm and choose from various output options, including visualization, exporting to json, images, LaTeX files, or both.

## Prerequisites

- Python 3.x
- `pip` for installing dependencies

## Installation

First, clone the repository and navigate into the project directory:

```bash
git clone https://github.com/uhalid/Progetto-RO.git
cd Progetto-RO
```

Then install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

To run the program, execute the following command:

```bash
python3 main.py [inputFile]
```

- `[inputFile]` is the path to the input file and is mandatory.

### Example Input File

The input file should be formatted as follows:

```
N M
From To Capacity Cost
Node_ID X Y
```

- `N`: Number of nodes
- `M`: Number of edges

After `N M`, there should be `M` rows, each containing the start node, end node, capacity, and cost of an edge. Following these `M` rows, there should be `N` rows indicating the coordinates of the nodes, used for rendering purposes.

### Sample Input

```
8 14
1 2 14 0
1 4 23 0
2 3 10 0
2 4 9 0
3 5 12 0
3 8 18 0
4 5 26 0
5 2 11 0
5 6 25 0
5 7 4 0
6 8 8 0
6 7 7 0
7 9 15 0
8 9 20 0
1 0 1
2 1 2
3 2 2
4 1 0
5 2 0
6 3 1
7 3 0
8 3 2
9 4 1
```

### Running the Program

After launching the program, you will be prompted to choose which algorithm to run. Currently, only the Ford-Fulkerson algorithm is available. For this algorithm, you will need to specify the source and sink nodes.

### Output Options

You can choose from the following output options:

1. **Visualize Results**: Opens a Matplotlib window showing all the different interactions.
2. **Export to Image**: Exports images of each interaction to the `results/FordFulkerson` folder.
3. **Export to LaTeX**: Exports a LaTeX file of each interaction to the `results/FordFulkerson` folder.
4. **Export to Image and LaTeX**: Exports both PNG files and a LaTeX files to the `results/FordFulkerson` folder
5. **Export to Json**: Exports a json file of each interaction to the `results/FordFulkerson` folder
