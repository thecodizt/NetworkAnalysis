import csv
from io import StringIO
from pyvis.network import Network
import streamlit.components.v1 as components

def parse_csv_string(csv_string):
    """
    Parses a CSV string and creates a matrix.

    Args:
        csv_string (str): A string in CSV format.

    Returns:
        list of lists: A matrix representing the CSV data.
    """
    # Create a StringIO object to read the CSV string
    csv_file = StringIO(csv_string)

    # Initialize an empty matrix
    matrix = []

    # Read the CSV data and create the matrix
    reader = csv.reader(csv_file)
    for row in reader:
        matrix.append([int(r) for r in row])

    return matrix

from pyvis.network import Network
import numpy as np

def visualize_critical_node_graph(adjacency_matrix, score=None, rank=None):
    """
    Visualizes a critical node graph.

    Args:
        adjacency_matrix (list of lists): The adjacency matrix representing the graph.
        score (dict, optional): A dictionary containing node scores. Defaults to None.
        rank (dict, optional): A dictionary containing node ranks. Defaults to None.
    """
    # Create a Network graph
    cn_graph = Network(
        height='400px',
        width='100%',
        bgcolor='white',
        font_color='black',
        directed=True,
        neighborhood_highlight=True
    )

    # Add nodes to the graph
    for i in range(len(adjacency_matrix)):
        label = "Node " + str(i)
        if score:
            label += f" (Score: {score.get(i, 0):.2f})"
        if rank:
            label += f" (Rank: {rank.get(i, 0)})"
        cn_graph.add_node(i, label=label)

    # Add edges to the graph
    for i in range(len(adjacency_matrix)):
        for j in range(len(adjacency_matrix[i])):
            if adjacency_matrix[i][j] == 1:
                cn_graph.add_edge(i, j)

    # Color nodes based on score or rank
    if score:
        scores = np.array(list(score.values()))
        min_score, max_score = np.min(scores), np.max(scores)
        for i in range(len(adjacency_matrix)):
            normalized_score = (score.get(i, 0) - min_score) / (max_score - min_score)
            color = f"rgba(255, 0, 0, {min(normalized_score + 0.1, 1)})"
            cn_graph.nodes[i]["color"] = color
    elif rank:
        ranks = np.array(list(rank.values()))
        min_rank, max_rank = np.min(ranks), np.max(ranks)
        for i in range(len(adjacency_matrix)):
            normalized_rank = (rank.get(i, 0) - min_rank) / (max_rank - min_rank)
            color = f"rgba(0, 0, 255, {min(normalized_rank + 0.1, 1)})"
            cn_graph.nodes[i]["color"] = color

    # Save the graph as an HTML file
    cn_graph.save_graph('./pages/cn_graph.html')
    source_code = open('./pages/cn_graph.html', 'r', encoding='utf-8').read()
    components.html(source_code, height=400)
    
def generate_random_adj_matrix(size):
    """
    Generates a random adjacency matrix of the given size.

    Args:
        size (int): The size of the square adjacency matrix.

    Returns:
        np.ndarray: A random adjacency matrix.
    """
    # Generate a random binary matrix (0s and 1s)
    random_matrix = np.random.randint(2, size=(size, size))

    # Set the diagonal to zeros (no self-loops)
    np.fill_diagonal(random_matrix, 0)

    return random_matrix