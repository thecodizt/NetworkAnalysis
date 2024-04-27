import numpy as np

def local_clustering_coefficient(adj_matrix):
    """
    Calculates the local clustering coefficient for each node in the graph.

    Args:
        adj_matrix (np.ndarray): An adjacency matrix representation of the graph.

    Returns:
        dict: A dictionary where keys are nodes and values are their local clustering coefficients.
    """
    num_nodes = adj_matrix.shape[0]
    local_clustering_coefficient = {}

    for node in range(num_nodes):
        neighbors = np.nonzero(adj_matrix[node])[0]
        num_neighbors = len(neighbors)

        if num_neighbors <= 1:
            # Avoid division by zero
            local_clustering_coefficient[node] = 0.0
        else:
            num_connected_pairs = 0
            for i in range(num_neighbors):
                for j in range(i + 1, num_neighbors):
                    if adj_matrix[neighbors[i], neighbors[j]]:
                        num_connected_pairs += 1

            local_clustering_coefficient[node] = 2 * num_connected_pairs / (num_neighbors * (num_neighbors - 1))

    return local_clustering_coefficient

# Example usage
if __name__ == "__main__":
    # Example adjacency matrix (replace with your own)
    adjacency_matrix = np.array([[0, 1, 1, 0],
                                 [1, 0, 1, 1],
                                 [1, 1, 0, 1],
                                 [0, 1, 1, 0]])

    local_clustering = local_clustering_coefficient(adjacency_matrix)

    # Print the results
    print("Local clustering coefficients:")
    for node, coeff in local_clustering.items():
        print(f"Node {node}: {coeff:.4f}")
