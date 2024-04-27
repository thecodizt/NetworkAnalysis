import numpy as np
import networkx as nx

def betweenness_centrality(adj_matrix):
    """
    Calculates the betweenness centrality for each node in the graph.

    Args:
        adj_matrix (np.ndarray): An adjacency matrix representation of the graph.

    Returns:
        dict: A dictionary where keys are nodes and values are their betweenness centrality.
    """
    # Create a NetworkX graph from the adjacency matrix
    G = nx.Graph(adj_matrix)

    # Calculate betweenness centrality
    betweenness_centrality = nx.betweenness_centrality(G, normalized=True, endpoints=False)

    return betweenness_centrality

# Example usage
if __name__ == "__main__":
    # Example adjacency matrix (replace with your own)
    adjacency_matrix = np.array([[0, 1, 1, 0],
                                 [1, 0, 1, 1],
                                 [1, 1, 0, 1],
                                 [0, 1, 1, 0]])

    betweenness = betweenness_centrality(adjacency_matrix)

    # Print the results
    print("Betweenness centrality:")
    for node, centrality in betweenness.items():
        print(f"Node {node}: {centrality:.4f}")
