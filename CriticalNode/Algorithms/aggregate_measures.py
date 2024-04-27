import sys
sys.path.append('/Users/dev/University/Experiments/NetworkAnalysis')

import numpy as np
import networkx as nx

from CriticalNode.Algorithms.pagerank import pagerank
from CriticalNode.Algorithms.betweenness_centrality import betweenness_centrality
from CriticalNode.Algorithms.closeness_centrality import closeness_centrality
from CriticalNode.Algorithms.eigenvector_centrality import eigenvector_centrality
from CriticalNode.Algorithms.local_clustering_coefficient import local_clustering_coefficient

def aggregate_measures(adj_matrix, damping_factor=0.85, num_iterations=100, use_rank=False):
    pagerank_scores = pagerank(adj_matrix, damping_factor, num_iterations)
    betweenness_scores = betweenness_centrality(adj_matrix)
    closeness_scores = closeness_centrality(adj_matrix)
    eigenvector_scores = eigenvector_centrality(adj_matrix)
    local_clustering_scores = local_clustering_coefficient(adj_matrix)

    # Adjust weights as needed
    weights = {
        "pagerank": 0.3,
        "betweenness": 0.2,
        "closeness": 0.1,
        "eigenvector": 0.2,
        "local_clustering": 0.2
    }

    aggregated_scores = {}
    for node in range(adj_matrix.shape[0]):
        aggregated_scores[node] = (
            weights["pagerank"] * pagerank_scores[node]
            + weights["betweenness"] * betweenness_scores[node]
            + weights["closeness"] * closeness_scores[node]
            + weights["eigenvector"] * eigenvector_scores[node]
            + weights["local_clustering"] * local_clustering_scores[node]
        )

    if use_rank:
        sorted_nodes = sorted(aggregated_scores, key=aggregated_scores.get)
        final_ranks = {node: rank + 1 for rank, node in enumerate(sorted_nodes)}
        return aggregated_scores, final_ranks
    else:
        return aggregated_scores, None  # Return None for consistency

# Example usage
if __name__ == "__main__":
    # Example adjacency matrix (replace with your own)
    adjacency_matrix = np.array([[0, 1, 1, 0],
                                 [1, 0, 1, 1],
                                 [1, 1, 0, 1],
                                 [0, 1, 1, 0]])

    raw_scores, final_ranks = aggregate_measures(adjacency_matrix, use_rank=True)
    print("Aggregated Raw Scores:")
    for node, score in raw_scores.items():
        print(f"Node {node}: {score:.4f}")

    if final_ranks:
        print("\nFinal Ranks (Lower rank is more critical):")
        for node, rank in final_ranks.items():
            print(f"Node {node}: Rank {rank}")