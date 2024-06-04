import streamlit as st
import numpy as np

from utils import parse_csv_string, visualize_critical_node_graph, generate_random_adj_matrix

from CriticalNode.Algorithms import aggregate_measures, betweenness_centrality, closeness_centrality, eigenvector_centrality, local_clustering_coefficient, pagerank, coreness_centrality, degree_centrality, percolation_centrality, katz_centrality, clusterrank_centrality, mnc_centrality, semilocal_centrality, load_centrality, laplacian_centrality
def ui_input():
    st.subheader("Input")
    
    matrix = None
    
    option = st.selectbox(label="Choose the input mechanism", options=["Adjacency Matrix", "Random Adjacency Matrix"])
    
    if option == "Adjacency Matrix":
        t_matrix = st.text_area("Enter the adjacency matrix in CSV format")
        matrix = parse_csv_string(t_matrix)
        st.code(matrix)
    elif option == "Random Adjacency Matrix":
        size = st.slider("Enter number of nodes")
        matrix = generate_random_adj_matrix(max(1,int(size)))
        st.code(matrix)
    
    return matrix
        
if __name__ == "__main__":
    st.title("Network Analysis")
    
    adj_matrix = ui_input()
    
    adj_matrix = np.array(adj_matrix)
    
    use_rank = st.checkbox("Use Rank instead of raw score?")
    
    if len(adj_matrix)>0 and len(adj_matrix[0]) > 0 and len(adj_matrix) == len(adj_matrix[0]):
    
        st.subheader("Critical Node Analysis")
        
        critical_node_algorithms = [
                "Aggregate Measure", 
                "Betweenness Centrality",
                "Closeness Centrality",
                "Eigenvector Centrality",
                "Local Cluserting Coefficient",
                "Pagerank",
                "Coreness Centrality",
                "Degree Centrality",
                "Percolation Centrality",
                "Katz Centrality",
                "Cluster Rank Centrality",
                "Maximum Neighborhood Component",
                "Semi Local Centrality",
                "Load Centrality",
                "Laplacian Centrality",
            ]
        
        critical_node_algorithm_option = st.selectbox(
            label="Select the algorithm to be used for Critical Node analysis", 
            options=critical_node_algorithms
        )
        
        if critical_node_algorithm_option == critical_node_algorithms[0]:
            node, score = aggregate_measures(adj_matrix, use_rank=use_rank)
            st.write(node)
            st.write(score)
            
            visualize_critical_node_graph(adjacency_matrix=adj_matrix, score=node, rank=score)
            
        elif critical_node_algorithm_option == critical_node_algorithms[1]:
            result = betweenness_centrality(adj_matrix=adj_matrix)
            st.code(result)
            visualize_critical_node_graph(adjacency_matrix=adj_matrix, score=result)
            
        elif critical_node_algorithm_option == critical_node_algorithms[2]:
            result = closeness_centrality(adj_matrix=adj_matrix)
            st.code(result)
            visualize_critical_node_graph(adjacency_matrix=adj_matrix, score=result)
            
            
        elif critical_node_algorithm_option == critical_node_algorithms[3]:
            result = eigenvector_centrality(adj_matrix=adj_matrix)
            st.code(result)
            visualize_critical_node_graph(adjacency_matrix=adj_matrix, score=result)
            
            
        elif critical_node_algorithm_option == critical_node_algorithms[4]:
            result = local_clustering_coefficient(adj_matrix=adj_matrix)
            st.code(result)
            visualize_critical_node_graph(adjacency_matrix=adj_matrix, score=result)
            
            
        elif critical_node_algorithm_option == critical_node_algorithms[5]:
            result = pagerank(adj_matrix=adj_matrix)
            st.code(result)
            visualize_critical_node_graph(adjacency_matrix=adj_matrix, score=result)
            
        elif critical_node_algorithm_option == critical_node_algorithms[6]:
            result = coreness_centrality(adj_matrix=adj_matrix)
            st.code(result)
            visualize_critical_node_graph(adjacency_matrix=adj_matrix, score=result)

        elif critical_node_algorithm_option == critical_node_algorithms[7]:
            result = degree_centrality(adj_matrix=adj_matrix)
            st.code(result)
            visualize_critical_node_graph(adjacency_matrix=adj_matrix, score=result)
        
        elif critical_node_algorithm_option == critical_node_algorithms[8]:
            result = percolation_centrality(adj_matrix=adj_matrix)
            st.code(result)
            visualize_critical_node_graph(adjacency_matrix=adj_matrix, score=result)
        
        elif critical_node_algorithm_option == critical_node_algorithms[9]:
            result = katz_centrality(adj_matrix=adj_matrix)
            st.code(result)
            visualize_critical_node_graph(adjacency_matrix=adj_matrix, score=result)

        elif critical_node_algorithm_option == critical_node_algorithms[10]:
            result = clusterrank_centrality(adj_matrix=adj_matrix)
            st.code(result)
            visualize_critical_node_graph(adjacency_matrix=adj_matrix, score=result)

        elif critical_node_algorithm_option == critical_node_algorithms[11]:
            result = mnc_centrality(adj_matrix=adj_matrix)
            st.code(result)
            visualize_critical_node_graph(adjacency_matrix=adj_matrix, score=result)

        elif critical_node_algorithm_option == critical_node_algorithms[12]:
            result = semilocal_centrality(adj_matrix=adj_matrix)
            st.code(result)
            visualize_critical_node_graph(adjacency_matrix=adj_matrix, score=result)

        elif critical_node_algorithm_option == critical_node_algorithms[13]:
            result = load_centrality(adj_matrix=adj_matrix)
            st.code(result)
            visualize_critical_node_graph(adjacency_matrix=adj_matrix, score=result)

        elif critical_node_algorithm_option == critical_node_algorithms[14]:
            result = laplacian_centrality(adj_matrix=adj_matrix)
            st.code(result)
            visualize_critical_node_graph(adjacency_matrix=adj_matrix, score=result)
            
        