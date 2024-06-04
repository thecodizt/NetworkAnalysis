import numpy as np
import networkx as nx

def percolation_centrality(adj_matrix):
    """
    Calculates the eigenvector centrality for each node in the graph.

    Args:
        adj_matrix (np.ndarray): An adjacency matrix representation of the graph.

    Returns:
        dict: A dictionary where keys are nodes and values are their eigenvector centrality.
    """
    # Create a NetworkX graph from the adjacency matrix
    G = nx.Graph(adj_matrix)

    # Calculate eigenvector centrality
    percolation_centrality = nx.percolation_centrality(G)

    return percolation_centrality

# Example usage
if __name__ == "__main__":
    # Example adjacency matrix (replace with your own)
    adjacency_matrix = np.array([[0, 1, 1, 0],
                                 [1, 0, 1, 1],
                                 [1, 1, 0, 1],
                                 [0, 1, 1, 0]])

    eigenvector = percolation_centrality(adjacency_matrix)

    # Print the results
    print("Eigenvector centrality:")
    for node, centrality in eigenvector.items():
        print(f"Node {node}: {centrality:.4f}")
