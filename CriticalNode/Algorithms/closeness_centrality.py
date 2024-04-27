import numpy as np
import networkx as nx

def closeness_centrality(adj_matrix):
    """
    Calculates the closeness centrality for each node in the graph.

    Args:
        adj_matrix (np.ndarray): An adjacency matrix representation of the graph.

    Returns:
        dict: A dictionary where keys are nodes and values are their closeness centrality.
    """
    # Create a NetworkX graph from the adjacency matrix
    G = nx.Graph(adj_matrix)

    # Calculate closeness centrality
    closeness_centrality = nx.closeness_centrality(G)

    return closeness_centrality

# Example usage
if __name__ == "__main__":
    # Example adjacency matrix (replace with your own)
    adjacency_matrix = np.array([[0, 1, 1, 0],
                                 [1, 0, 1, 1],
                                 [1, 1, 0, 1],
                                 [0, 1, 1, 0]])

    closeness = closeness_centrality(adjacency_matrix)

    # Print the results
    print("Closeness centrality:")
    for node, centrality in closeness.items():
        print(f"Node {node}: {centrality:.4f}")
