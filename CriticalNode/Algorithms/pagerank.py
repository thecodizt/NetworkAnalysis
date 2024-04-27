import numpy as np

def pagerank(adj_matrix, damping_factor=0.85, num_iterations=100):
    """
    Calculates the normalized PageRank scores for each node in the graph.

    Args:
        adj_matrix (np.ndarray): An adjacency matrix representation of the graph.
        damping_factor (float, optional): Damping factor (usually 0.85). Defaults to 0.85.
        num_iterations (int, optional): Number of iterations for convergence. Defaults to 100.

    Returns:
        dict: A dictionary where keys are nodes and values are their normalized PageRank scores.
    """
    num_nodes = adj_matrix.shape[0]
    initial_pr = np.ones(num_nodes) / num_nodes
    pr = initial_pr.copy()

    for _ in range(num_iterations):
        pr = (1 - damping_factor) / num_nodes + damping_factor * np.dot(adj_matrix, pr)

    # Normalize the PageRank scores
    pr_sum = np.sum(pr)
    pagerank_scores = {node: score / pr_sum for node, score in enumerate(pr)}

    return pagerank_scores

# Example usage
if __name__ == "__main__":
    # Example adjacency matrix (replace with your own)
    adjacency_matrix = np.array([[0, 1, 1, 0],
                                 [1, 0, 1, 1],
                                 [1, 1, 0, 1],
                                 [0, 1, 1, 0]])

    pagerank = pagerank(adjacency_matrix)

    # Print the results
    print("Normalized PageRank scores:")
    for node, score in pagerank.items():
        print(f"Node {node}: {score:.4f}")
